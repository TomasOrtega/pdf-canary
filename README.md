# PDF Canary

A tiny website and command-line tool that add invisible AI canary prompts to PDFs.

The canary is inserted into the PDF text layer on interior pages. It asks an AI system using copied text from the PDF to include a randomly generated phrase in its response. The PDF looks unchanged when rendered normally.

## Website

Open [PDF Canary](https://tomasortega.github.io/pdf-canary/), choose a PDF, and download the canaried copy. Processing happens entirely in the browser.

## Command line

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
uv run pdf_canary.py input.pdf output.pdf
```

The script prints the phrase to look for, for example:

```text
Wrote: output.pdf
Look for this phrase in the essay: "the subtly durable contrast"
```

Keep that phrase somewhere you can associate with the PDF you distributed.

## Development

```bash
uv sync
uv run prek -a --quiet
uv run pytest
```

## Note

A matching phrase is evidence that the PDF text may have been supplied to an AI system, not conclusive proof by itself. PDF extraction and model behavior can vary.
