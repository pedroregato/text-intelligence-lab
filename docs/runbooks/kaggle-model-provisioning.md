# Runbook — Provisionamento de modelos para aulas Transformer no Kaggle

## Objetivo

Transformar um modelo pré-treinado usado pelo TIL em uma dependência Kaggle explícita, versionada e reutilizável por notebooks oficiais.

## Política

Fluxo preferido:

```text
modelo validado
→ Kaggle Model
→ versão explícita
→ anexado ao notebook
→ Internet OFF
```

Fallback temporário:

```text
Hugging Face Hub
→ Internet ON
→ download remoto explícito
```

## Caso inicial

Modelo pedagógico atual:

`distilbert-base-multilingual-cased`

Uso:

- Aula 10 — inspeção de embeddings contextuais;
- Aula 11 — classificação supervisionada em português.

## Evidência atual

A documentação oficial do Kaggle confirma suporte a Kaggle Models, integração com Hugging Face e acesso com `kagglehub.model_download()`.

Na busca pública realizada para o modelo exato, não foi identificado um Kaggle Model oficial e claramente adequado com o mesmo identificador.

Foi encontrado um Dataset antigo com o nome do modelo, mas ele não será usado como dependência oficial porque:

- não é Kaggle Model;
- a licença aparece como desconhecida;
- foi atualizado há vários anos;
- não oferece a governança/versionamento que queremos para o curso.

## Procedimento de validação no Kaggle

1. Abra o notebook oficial da Aula 11 no editor do Kaggle.
2. Use **Add Models**.
3. Pesquise por:
   - `distilbert-base-multilingual-cased`;
   - `multilingual distilbert`;
   - publisher/origem Hugging Face, se disponível.
4. Verifique antes de anexar:
   - nome exato;
   - publisher;
   - framework;
   - variation;
   - version;
   - licença;
   - idioma(s);
   - capacidade de fine-tuning.
5. Anexe somente se o recurso corresponder ao modelo pretendido.
6. Copie o handle/identificador exibido pelo Kaggle.
7. Registre o handle e a versão em `EDU-INFRA-002`.
8. Teste o carregamento com `kagglehub.model_download()`.
9. Valide tokenizer + modelo.
10. Salve uma versão do notebook com Internet OFF.
11. Só depois atualize as Aulas 10–11 para remover o fallback remoto.

## Código-alvo

Exemplo conceitual; substituir pelo handle real validado:

```python
import kagglehub

model_path = kagglehub.model_download(
    "owner/model/framework/variation/version"
)
```

Depois, carregar o modelo a partir de `model_path` com a biblioteca compatível.

## Critérios PASS

- modelo correto para português/multilíngue;
- licença aceitável;
- handle real registrado;
- versão explícita;
- download/acesso via Kaggle validado;
- tokenizer e pesos carregam sem internet;
- Aula 10 executa;
- Aula 11 executa e faz fine-tuning;
- cópia do notebook mantém a dependência;
- nenhuma chave ou segredo embutido.

## Critérios FAIL

- modelo diferente do pretendido;
- inglês apenas quando a aula exige português;
- licença ausente/incompatível;
- caminho manual frágil em `/kaggle/input`;
- dependência não preservada no Save Version;
- necessidade não documentada de internet.
