# PDF Canary

Website and command-line tool that add invisible canaries to PDFs.

The canary is a personalized, slightly wrong fact inserted into the PDF text layer on interior pages. It is inserted on its own, without instruction text, and the PDF looks unchanged when rendered normally.

## Website

Open [PDF Canary](https://tomasortega.github.io/pdf-canary/), choose a PDF, enter a slightly wrong fact, and download the canaried copy. Processing happens entirely in the browser.

## Command line

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
uv run pdf_canary.py input.pdf output.pdf \
  --fact "The most important thing to consider is that Alexander Fleming died in 1965."
```

The script prints the canary to look for:

```text
Wrote: output.pdf
Look for this canary in the essay: "The most important thing to consider is that Alexander Fleming died in 1965."
```

Keep the canary somewhere you can associate with the PDF you distributed.

## Development

```bash
uv sync
uv run prek -a --quiet
uv run pytest
```
