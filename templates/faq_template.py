def faq_template(product: dict) -> dict:
    return {
        "page_type": "FAQ",
        "product": product["name"],
        "faqs": [
            {
                "question": "What is this product?",
                "answer": f"{product['name']} is a skincare serum."
            },
            {
                "question": "What are the key benefits?",
                "answer": ", ".join(product["benefits"])
            },
            {
                "question": "Who can use this product?",
                "answer": "It is suitable for oily and combination skin types."
            },
            {
                "question": "How do I use it?",
                "answer": product["usage"]
            },
            {
                "question": "Are there any side effects?",
                "answer": product["side_effects"]
            }
        ]
    }
