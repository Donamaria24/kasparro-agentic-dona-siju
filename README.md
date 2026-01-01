Kasparro Agentic Content Generation System

This project implements an agentic content generation pipeline using LangGraph and LangChain-style agents to generate structured product content such as:

- Product Page
- FAQs (≥15 enforced)
- Product Comparison Page

The system is designed to work with an LLM provider (Gemini) and includes deterministic fallback logic to ensure reliability when LLM access is unavailable.

Architecture Overview

The system uses LangGraph to orchestrate multiple independent agents:

Product Input
│
▼
Product Agent ──▶ Product Page JSON
│
▼
FAQ Agent ──────▶ FAQ JSON (≥15 enforced)
│
▼
Comparison Agent ▶ Comparison Page JSON

Each agent:
- Receives shared state
- Performs validation and transformation
- Uses LLM if available
- Falls back to deterministic logic if LLM fails

Agents

1. Product Agent
- Generates a structured product page
- Validates required fields
- Guarantees non-empty `product_name`
- Output: `output/product_page.json`

2. FAQ Agent
- Generates at least 15 FAQs
- Uses LLM or deterministic fallback
- Enforces schema
- Output: `output/faq.json`

3. Comparison Agent
- Produces structured comparison content
- Ensures valid JSON output
- Output: `output/comparison_page.json`

LLM Fallback Strategy

If the LLM fails due to:
- Missing API key
- Rate limits
- Provider errors

The system automatically switches to deterministic logic.

This behavior is:
- Logged clearly in the terminal
- Fully documented
- Intentional and test-covered

⚠️ This ensures reliability without silent failures.

Project Structure

kasparro-agentic-dona-maria-siju/
├── agents/
│ ├── product_agent.py
│ ├── faq_agent.py
│ ├── comparison_agent.py
│ ├── graph.py
│ └── state.py
│
├── schemas/
│ ├── product_schema.py
│ ├── faq_schema.py
│ └── comparison_schema.py
│
├── data/
│ └── product_input.py
│
├── output/
│ ├── product_page.json
│ ├── faq.json
│ └── comparison_page.json
│
├── tests/
│ ├── test_product_page.py
│ ├── test_faq.py
│ └── test_comparison.py
│
├── docs/
│ └── projectdocumentation.md
│
├── main.py
├── requirements.txt
└── README.md

Installation

python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt

Run the System
python -B main.py

Expected output:
📁 Output written to /output
✅ Content generation completed successfully

Run Tests
python -m pytest

All tests must pass:
Schema validation
FAQ count enforcement
Product name validation
Output existence

Design Tradeoffs
This system prioritizes reliability over external dependency availability. When LLM access is unavailable, deterministic fallbacks ensure consistent outputs while preserving structural guarantees. Advanced features such as caching, rate limiting, and security hardening were intentionally scoped out to focus on correctness, validation, and agent orchestration.