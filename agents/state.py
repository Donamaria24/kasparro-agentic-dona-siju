from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    product: Dict
    faqs: List[Dict]
    product_page: Dict
    comparison_page: Dict
