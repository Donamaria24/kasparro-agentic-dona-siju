from langgraph.graph import StateGraph
from agents.state import AgentState
from agents.faq_agent import faq_agent
from agents.product_agent import product_agent
from agents.comparison_agent import comparison_agent

graph = StateGraph(AgentState)

graph.add_node("faq_agent", faq_agent)
graph.add_node("product_agent", product_agent)
graph.add_node("comparison_agent", comparison_agent)

graph.set_entry_point("faq_agent")
graph.add_edge("faq_agent", "product_agent")
graph.add_edge("product_agent", "comparison_agent")

app = graph.compile()
