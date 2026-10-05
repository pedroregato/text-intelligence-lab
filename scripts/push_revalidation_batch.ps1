param(
    [switch]$StatusOnly
)

$ErrorActionPreference = "Stop"

$batch = @(
    @{ Lesson = "02"; Path = "course\02-tokenization-and-normalization"; Id = "pedrogentil/til-02-tokenization-and-normalization" },
    @{ Lesson = "03"; Path = "course\03-bag-of-words"; Id = "pedrogentil/til-03-bag-of-words" },
    @{ Lesson = "04"; Path = "course\04-tfidf"; Id = "pedrogentil/til-04-tfidf" },
    @{ Lesson = "05"; Path = "course\05-first-text-classifier"; Id = "pedrogentil/til-05-first-text-classifier" },
    @{ Lesson = "06"; Path = "course\06-classification-evaluation"; Id = "pedrogentil/til-06-classification-evaluation" },
    @{ Lesson = "07"; Path = "course\07-model-selection-and-tuning"; Id = "pedrogentil/til-07-model-selection-and-tuning" },
    @{ Lesson = "09"; Path = "course\09-word-embeddings"; Id = "pedrogentil/til-09-word-embeddings" },
    @{ Lesson = "10"; Path = "course\10-contextual-embeddings-and-transformers"; Id = "pedrogentil/til-10-contextual-embeddings-and-transformers" },
    @{ Lesson = "11"; Path = "course\11-bert-text-classification"; Id = "pedrogentil/til-11-bert-text-classification" },
    @{ Lesson = "12"; Path = "course\12-strong-classical-baselines"; Id = "pedrogentil/til-12-strong-classical-baselines" },
    @{ Lesson = "14"; Path = "course\14-llm-foundations"; Id = "pedrogentil/til-14-llm-foundations" },
    @{ Lesson = "15"; Path = "course\15-retrieval-semantic-search-grounding"; Id = "pedrogentil/til-15-retrieval-semantic-search-grounding" },
    @{ Lesson = "16"; Path = "course\16-rag"; Id = "pedrogentil/til-16-retrieval-augmented-generation" },
    @{ Lesson = "17"; Path = "course\17-tool-use-function-calling"; Id = "pedrogentil/til-17-tool-use-function-calling-and-contracts" },
    @{ Lesson = "18"; Path = "course\18-deterministic-workflows"; Id = "pedrogentil/til-18-deterministic-workflows" },
    @{ Lesson = "19"; Path = "course\19-model-context-protocol"; Id = "pedrogentil/til-19-model-context-protocol" }
)

Write-Host ""
Write-Host "TIL — Reengineering Validation Batch"
Write-Host "===================================="
Write-Host ""

foreach ($item in $batch) {
    Write-Host ("Aula {0} — {1}" -f $item.Lesson, $item.Id)

    if (-not $StatusOnly) {
        kaggle kernels push -p $item.Path

        if ($LASTEXITCODE -ne 0) {
            throw "Falha no push da Aula $($item.Lesson)"
        }
    }

    kaggle kernels status $item.Id
    Write-Host ""
}

Write-Warning @"
Aula 13C não foi incluída automaticamente.

Motivo:
- o notebook está em:
  course\13-metrics-and-indicators\13c-model-routing-and-orchestration.ipynb
- o kernel-metadata.json desse diretório pertence à Aula 13;
- não há metadata Kaggle dedicado à 13C no estado atual do repositório.

Não execute:
  kaggle kernels push -p course\13-metrics-and-indicators

esperando publicar a 13C, pois isso aponta para o kernel da Aula 13.

Valide/publice a 13C separadamente até que seja criado um wrapper Kaggle dedicado.
"@
