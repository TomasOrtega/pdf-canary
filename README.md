# PDF Canary

Website and command-line tool that add invisible canaries to PDFs.

The canary is inserted into the PDF text layer on interior pages. It can be a personalized, slightly wrong fact or an instruction to include a randomly generated phrase in a response. A personalized fact is inserted on its own, without instruction text. The PDF looks unchanged when rendered normally.

## Website

Open [PDF Canary](https://tomasortega.github.io/pdf-canary/), choose a PDF, select a canary type, and download the canaried copy. Processing happens entirely in the browser.

## Command line

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
uv run pdf_canary.py input.pdf output.pdf
```

Use `--fact` to add a personalized canary containing only a slightly wrong fact:

```bash
uv run pdf_canary.py input.pdf output.pdf \
  --fact "The most important thing to consider is that Alexander Fleming died in 1965."
```

Without `--fact`, the script uses the original random phrase instruction. It prints the canary to look for, for example:

```text
Wrote: output.pdf
Look for this canary in the essay: "the subtly durable contrast"
```

Keep the canary somewhere you can associate with the PDF you distributed.

## Development

```bash
uv sync
uv run prek -a --quiet
uv run pytest
```
