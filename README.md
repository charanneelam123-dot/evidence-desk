# Evidence Desk

[![Checks](https://github.com/charanneelam123-dot/evidence-desk/actions/workflows/tests.yml/badge.svg)](https://github.com/charanneelam123-dot/evidence-desk/actions/workflows/tests.yml)

Document question answering with BM25 retrieval, source citations, abstention, and optional live generation.

A focused retrieval example. For the larger deployed application, see [financial-document-intelligence](https://github.com/charanneelam123-dot/financial-document-intelligence).

Project by Charan Neelam. Python 3.11+; no third-party packages required.
All bundled business data is fictional.

## Quick start

```bash
git clone https://github.com/charanneelam123-dot/evidence-desk.git
cd evidence-desk
python app.py "What is the vacation allowance?"
python -m unittest discover -s tests -v
```

## Optional live model

Set environment variables in your shell; `.env.example` documents the names
but `.env` files are not automatically loaded. Choose a chat/tool-compatible
model available to your API account.

```powershell
$env:OPENAI_API_KEY = "your-key"
$env:OPENAI_MODEL = "your-model-id"
```

Append `--live` to the demo command. Live mode sends question/context data to
OpenAI and incurs API usage. Missing credentials cause an explicit error.
The adapter uses the [Chat Completions API](https://developers.openai.com/api/reference/resources/chat).

## How it works

```mermaid
flowchart LR
    A[Markdown and text] --> B[Overlapping chunks]
    B --> C[BM25 ranking]
    Q[Question] --> C
    C --> D[Extractive response or LLM]
    D --> E[Citation validation]
```

The default mode returns real retrieved excerpts with stable chunk IDs. `--live`
adds model generation and checks that citation IDs belong to retrieved evidence.
Use `--docs path/to/folder` for your own UTF-8 Markdown or text documents.

## Design decisions and limitations

BM25 is an inspectable baseline with no embedding download or database setup.
It does not handle semantic paraphrases well. A positive lexical score only
indicates overlap, so unrelated questions sharing common terms can retrieve weak
evidence. Citation validation checks references, not factual entailment. Prompt
injection defenses are best effort. PDF parsing, semantic embeddings, persisted
indexes, and a labeled retrieval benchmark are future extensions.

## Interview walkthrough

Compare a vacation question with `quantum zebras` to demonstrate retrieval and
abstention. Explain why valid citations alone do not prove grounded answers.

## Validation

Unit tests run without API credentials and include mocked provider behavior.
GitHub Actions runs tests on Python 3.11–3.14. See `docs/validation.md` for the
local validation record. Live provider behavior has not been validated with a
paid API call.

## Portfolio talking point

See `docs/linkedin-draft.md` for an editable project announcement. Use only
results you have reproduced and can explain. Licensed under MIT.
