import json
import os


def test_faq_output_exists():
    assert os.path.exists("output/faq.json"), "faq.json was not generated"


def test_faq_count():
    with open("output/faq.json", "r", encoding="utf-8") as f:
        faqs = json.load(f)

    assert isinstance(faqs, list), "FAQ output must be a list"
    assert len(faqs) >= 15, "FAQ count must be at least 15"


def test_faq_structure():
    with open("output/faq.json", "r", encoding="utf-8") as f:
        faqs = json.load(f)

    for faq in faqs:
        assert "question" in faq
        assert "answer" in faq
        assert isinstance(faq["question"], str)
        assert isinstance(faq["answer"], str)
