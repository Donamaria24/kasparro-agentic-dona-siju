Kasparro Agentic Content Generation System
1. Objective
The goal of this project is to design and implement a multi-agent content generation system that can dynamically produce structured product-related content using an agent-based architecture.

The system focuses on clarity, maintainability, robustness, and deterministic execution, rather than model complexity.

2. Design Decisions

2.1 Agent-Based Architecture
The system is built using LangGraph, where each agent is responsible for a single, well-defined task. This design:
- Improves modularity
- Enables easier debugging and extension
- Mirrors real-world multi-agent workflows

2.2 Shared State Management
A shared `AgentState` object is passed between agents, allowing:
- Controlled data flow
- Stateless agent functions
- Predictable orchestration behavior

2.3 LLM Integration
The system integrates Google Gemini via LangChain to generate content dynamically.

Each agent:
- Attempts to generate content using the LLM
- Parses structured JSON output
- Writes results back to the shared state

3. Robustness & Fallback Strategy
External LLM providers may be unavailable due to:
- API quota limits
- Model access restrictions
- Network or provider-side issues

To ensure uninterrupted execution, the system implements a graceful fallback mechanism:
- If an LLM call fails, deterministic fallback logic generates valid structured content
- Output constraints (e.g., minimum FAQ count) are still enforced
- The pipeline never crashes due to external dependencies

This approach reflects production-grade engineering practices.

4. Output Constraints
The system enforces several constraints:
- FAQs must contain at least 15 entries
- All outputs must be valid JSON
- Agents must return structured, schema-consistent data

Constraint violations raise explicit errors to prevent silent failures.

5. Orchestration Flow
1. The FAQ agent generates or falls back to FAQ content
2. The product agent generates a structured product page
3. The comparison agent generates competitor comparison data
4. Outputs are persisted to disk as JSON files

6. Testing & Validation
- End-to-end pipeline execution tested locally
- JSON outputs validated for structure and completeness
- Error handling verified by simulating LLM failures

7. Conclusion
This project demonstrates:
- Correct use of LangGraph for agent orchestration
- Real LLM integration with graceful degradation
- Deterministic, constraint-driven output generation
- Clean and maintainable system design

The architecture is extensible and can be enhanced with additional agents, schemas, or validation layers as needed.
