from pydantic import BaseModel
from typing import List


class FAQ(BaseModel):
    question: str
    answer: str


class FAQList(BaseModel):
    faqs: List[FAQ]
