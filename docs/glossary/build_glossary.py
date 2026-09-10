"""Generate TIL glossary views from canonical glossary sources.

Requires:
    pip install pyyaml

Usage:
    python docs/glossary/build_glossary.py

The main source is glossary.yaml. Small curricular additions may live in
`glossary.extensions.yaml`; the generator merges them and rejects duplicate IDs.
"""
from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "glossary.yaml"
EXTENSIONS = ROOT / "glossary.extensions.yaml"
WEB = ROOT / "web"

CATEGORY_NAMES = {
    "core": {"pt-BR": "Conceitos fundamentais", "en": "Core concepts"},
    "text-intelligence": {"pt-BR": "Text Intelligence", "en": "Text Intelligence"},
    "engineering": {"pt-BR": "Experimentação e engenharia", "en": "Experimentation and engineering"},
    "machine-learning": {"pt-BR": "Machine Learning e estatística", "en": "Machine Learning and statistics"},
    "evaluation": {"pt-BR": "Avaliação", "en": "Evaluation"},
    "production": {"pt-BR": "Produção e operação", "en": "Production and operations"},
}


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_data():
    data = load_yaml(SOURCE)
    data.setdefault("terms", [])

    if EXTENSIONS.exists():
        extension_data = load_yaml(EXTENSIONS)
        extension_terms = extension_data.get("terms", [])

        existing_ids = {item["id"] for item in data["terms"]}
        duplicate_ids = sorted(
            item["id"] for item in extension_terms if item["id"] in existing_ids
        )
        if duplicate_ids:
            raise ValueError(
                "Duplicate glossary term IDs found in extensions: "
                + ", ".join(duplicate_ids)
            )

        data["terms"].extend(extension_terms)

    ids = [item["id"] for item in data["terms"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Glossary contains duplicate term IDs.")

    unknown_categories = sorted(
        {item["category"] for item in data["terms"]}
        - set(CATEGORY_NAMES)
    )
    if unknown_categories:
        raise ValueError(
            "Unknown glossary categories: " + ", ".join(unknown_categories)
        )

    return data


def markdown(data, lang):
    title = "# Glossário Vivo do TIL — PT-BR" if lang == "pt-BR" else "# TIL Living Glossary — EN"
    note = (
        "> Gerado a partir de `glossary.yaml` + extensões curriculares. Não edite manualmente como fonte primária."
        if lang == "pt-BR"
        else "> Generated from `glossary.yaml` + curriculum extensions. Do not edit manually as the primary source."
    )
    lines = [title, "", note, ""]
    for item in data["terms"]:
        x = item[lang]
        lines.extend([f"## {x['term']}", ""])
        if lang == "pt-BR":
            lines.extend([f"**English:** {x.get('english_term', item['en']['term'])}", ""])
        lines.extend([
            x["definition"], "",
            f"**{'No TIL' if lang == 'pt-BR' else 'In TIL'}:** {x['til_context']}", "",
            f"**{'Exemplo' if lang == 'pt-BR' else 'Example'}:** {x['example']}", "",
            f"**{'Primeira aula' if lang == 'pt-BR' else 'First lesson'}:** {item['lesson_first_seen']}", "",
        ])
    return "\n".join(lines)


def html_page(data):
    payload = json.dumps(data["terms"], ensure_ascii=False)
    categories = json.dumps(CATEGORY_NAMES, ensure_ascii=False)
    template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TIL Interactive Glossary</title>
<style>
:root { font-family: Inter, system-ui, sans-serif; color:#17202a; background:#f7f8fa; }
* { box-sizing:border-box; }
body { margin:0; }
header { padding:28px 22px 18px; background:#fff; border-bottom:1px solid #e5e7eb; position:sticky; top:0; z-index:2; }
.wrap, main { max-width:1100px; margin:auto; }
h1 { margin:0 0 6px; }
.sub { color:#667085; margin:0; }
.controls { display:grid; grid-template-columns:1fr auto auto; gap:10px; margin-top:18px; }
input, select, button { font:inherit; border:1px solid #d8dde5; border-radius:10px; padding:10px 12px; background:#fff; }
button { cursor:pointer; }
main { padding:24px 22px 50px; }
#count { color:#667085; margin-bottom:14px; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:14px; }
.card { background:#fff; border:1px solid #e4e7ec; border-radius:14px; padding:18px; }
.term { font-size:20px; font-weight:700; }
.alt { font-size:13px; color:#667085; margin:2px 0 10px; }
.badge { display:inline-block; font-size:12px; background:#eef2f6; border-radius:999px; padding:3px 8px; }
.label { font-weight:700; margin-top:12px; font-size:13px; }
.text { line-height:1.5; color:#344054; }
.related a { margin-right:8px; text-decoration:none; }
@media(max-width:700px){ .controls{grid-template-columns:1fr;} }
</style>
</head>
<body>
<header>
<div class="wrap">
<h1>TIL Interactive Glossary</h1>
<p class="sub">Glossário vivo bilíngue do Text Intelligence Lab</p>
<div class="controls">
<input id="search" type="search" placeholder="Buscar conceito, definição ou exemplo...">
<select id="category"><option value="">Todas as categorias</option></select>
<button id="lang">EN</button>
</div>
</div>
</header>
<main>
<div id="count"></div>
<div id="cards" class="grid"></div>
</main>
<script>
const terms = __TERMS__;
const categories = __CATEGORIES__;
let lang = "pt-BR";
const search = document.getElementById("search");
const category = document.getElementById("category");
const langButton = document.getElementById("lang");
const cards = document.getElementById("cards");
const count = document.getElementById("count");

Object.keys(categories).forEach(function(id){
  const option = document.createElement("option");
  option.value = id;
  option.textContent = categories[id]["pt-BR"];
  category.appendChild(option);
});

function displayName(t){ return lang === "pt-BR" ? t["pt-BR"].term : t.en.term; }

function render(){
  const q = search.value.trim().toLowerCase();
  const cat = category.value;
  const filtered = terms.filter(function(t){
    const x = t[lang];
    const alt = lang === "pt-BR" ? (x.english_term || t.en.term) : t["pt-BR"].term;
    const hay = [x.term, alt, x.definition, x.til_context, x.example].join(" ").toLowerCase();
    return (!q || hay.includes(q)) && (!cat || t.category === cat);
  });

  count.textContent = lang === "pt-BR" ? filtered.length + " conceito(s)" : filtered.length + " concept(s)";
  cards.innerHTML = "";

  filtered.forEach(function(t){
    const x = t[lang];
    const alt = lang === "pt-BR" ? (x.english_term || t.en.term) : t["pt-BR"].term;
    const article = document.createElement("article");
    article.className = "card";
    article.id = t.id;

    const related = (t.related || []).map(function(id){
      const target = terms.find(function(z){ return z.id === id; });
      return target ? '<a href="#' + id + '">' + displayName(target) + '</a>' : "";
    }).join("");

    article.innerHTML =
      '<div class="term">' + x.term + '</div>' +
      '<div class="alt">' + alt + '</div>' +
      '<span class="badge">' + categories[t.category][lang] + ' · ' + (lang === "pt-BR" ? "Aula " : "Lesson ") + t.lesson_first_seen + '</span>' +
      '<div class="label">' + (lang === "pt-BR" ? "Definição" : "Definition") + '</div>' +
      '<div class="text">' + x.definition + '</div>' +
      '<div class="label">' + (lang === "pt-BR" ? "No TIL" : "In TIL") + '</div>' +
      '<div class="text">' + x.til_context + '</div>' +
      '<div class="label">' + (lang === "pt-BR" ? "Exemplo" : "Example") + '</div>' +
      '<div class="text">' + x.example + '</div>' +
      '<div class="label">' + (lang === "pt-BR" ? "Relacionados" : "Related") + '</div>' +
      '<div class="related">' + related + '</div>';

    cards.appendChild(article);
  });
}

search.addEventListener("input", render);
category.addEventListener("change", render);
langButton.addEventListener("click", function(){
  lang = lang === "pt-BR" ? "en" : "pt-BR";
  langButton.textContent = lang === "pt-BR" ? "EN" : "PT-BR";
  search.placeholder = lang === "pt-BR" ? "Buscar conceito, definição ou exemplo..." : "Search concept, definition, or example...";
  category.options[0].textContent = lang === "pt-BR" ? "Todas as categorias" : "All categories";
  for(let i=1;i<category.options.length;i++){
    const id = category.options[i].value;
    category.options[i].textContent = categories[id][lang];
  }
  render();
});
render();
</script>
</body>
</html>"""
    return template.replace("__TERMS__", payload).replace("__CATEGORIES__", categories)


def main():
    data = load_data()
    (ROOT / "glossary.pt-BR.md").write_text(markdown(data, "pt-BR"), encoding="utf-8")
    (ROOT / "glossary.en.md").write_text(markdown(data, "en"), encoding="utf-8")
    WEB.mkdir(exist_ok=True)
    (WEB / "index.html").write_text(html_page(data), encoding="utf-8")
    print("Generated glossary.pt-BR.md, glossary.en.md and web/index.html")


if __name__ == "__main__":
    main()
