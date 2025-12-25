from data.product_input import PRODUCT_DATA
from agents.orchestrator_agent import OrchestratorAgent

if __name__ == "__main__":
    orchestrator = OrchestratorAgent()
    orchestrator.run(PRODUCT_DATA)
