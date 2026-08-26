# PDF Canary

A tiny script that adds an invisible AI canary prompt to a PDF.

The canary is inserted into the PDF text layer on interior pages. It asks an AI system using copied text from the PDF to include a randomly generated phrase in its response. The PDF looks unchanged when rendered normally.

## Install

```bash
python -m pip install -r requirements.txt
```

## Use

```bash
python pdf_canary.py input.pdf output.pdf
```

The script prints the phrase to look for, for example:

```text
Wrote: output.pdf
Look for this phrase in the essay: "the subtly durable contrast"
```

Keep that phrase somewhere you can associate with the PDF you distributed.

## Note

A matching phrase is evidence that the PDF text may have been supplied to an AI system, not conclusive proof by itself. PDF extraction and model behavior can vary.
