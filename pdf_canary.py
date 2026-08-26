#!/usr/bin/env python3
import argparse
import random
import secrets
from pathlib import Path

import pymupdf


def canary_pages(page_count: int) -> list[int]:
    pages = list(range(1, page_count - 1, 2))
    return pages or list(range(page_count))


def add_canaries(
    input_pdf: str | Path,
    output_pdf: str | Path,
    fact: str,
    rng: random.Random | None = None,
) -> str:
    rng = rng or secrets.SystemRandom()
    fact = fact.strip()
    if not fact:
        raise ValueError("The personalized fact cannot be empty")

    with pymupdf.open(input_pdf) as doc:
        for page_number in canary_pages(len(doc)):
            page = doc[page_number]
            rect = page.rect
            x = rect.x0 + rect.width * 0.05
            y = rect.y0 + rect.height * rng.uniform(0.35, 0.70)
            font_size = min(
                3,
                rect.width
                * 0.9
                * 3
                / pymupdf.get_text_length(fact, fontname="helv", fontsize=3),
            )
            page.insert_text(
                (x, y),
                fact,
                fontsize=font_size,
                fontname="helv",
                render_mode=3,
            )

        doc.save(output_pdf, garbage=4, deflate=True)

    return fact


def main() -> None:
    parser = argparse.ArgumentParser(description="Add invisible canaries to a PDF")
    parser.add_argument("input_pdf")
    parser.add_argument("output_pdf")
    parser.add_argument(
        "--fact",
        required=True,
        help="slightly wrong fact to insert as the canary",
    )
    args = parser.parse_args()

    canary = add_canaries(args.input_pdf, args.output_pdf, args.fact)

    print(f"Wrote: {args.output_pdf}")
    print(f'Look for this canary in the essay: "{canary}"')


if __name__ == "__main__":
    main()
