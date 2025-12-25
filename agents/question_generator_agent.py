class QuestionGeneratorAgent:
    def run(self, product: dict) -> list:
        return [
            {"category": "Informational", "question": "What is this product?"},
            {"category": "Usage", "question": "How should it be applied?"},
            {"category": "Safety", "question": "Are there any side effects?"},
            {"category": "Ingredients", "question": "What are the key ingredients?"},
            {"category": "Purchase", "question": "What is the price?"}
        ]
