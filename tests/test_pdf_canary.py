import random

import pymupdf

from pdf_canary import add_canaries, canary_pages


def make_pdf(path, page_count: int) -> None:
    with pymupdf.open() as document:
        for page_number in range(page_count):
            page = document.new_page()
            page.insert_text((72, 72), f"Page {page_number + 1}")
        document.save(path)


def test_canary_pages_prefers_alternating_interior_pages() -> None:
    assert canary_pages(5) == [1, 3]
    assert canary_pages(2) == [0, 1]
    assert canary_pages(1) == [0]


def test_add_canaries_adds_invisible_prompt_to_selected_pages(tmp_path) -> None:
    source = tmp_path / "source.pdf"
    output = tmp_path / "output.pdf"
    make_pdf(source, 5)

    phrase = add_canaries(source, output, random.Random(0))

    with pymupdf.open(source) as original, pymupdf.open(output) as canaried:
        assert phrase == "the unexpectedly delicate distinction"
        for page_number in range(5):
            text = canaried[page_number].get_text()
            if page_number in (1, 3):
                assert phrase in text
                assert "AI instruction:" in text
            else:
                assert "AI instruction:" not in text

        assert original[1].get_pixmap().samples == canaried[1].get_pixmap().samples
