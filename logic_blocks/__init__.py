Kasparro – Multi-Agent Content Generation System
1. Problem Statement

The objective of this project is to design and implement a modular, agent-based automation system that takes a small, structured product dataset as input and automatically generates machine-readable content pages.

The system must:

Operate entirely on the provided input data

Use multiple agents, not a monolithic script

Generate structured content using reusable logic blocks and templates

Output clean, valid JSON files

Be designed with maintainability, clarity, and extensibility in mind

This project does not focus on domain expertise or model training, but instead evaluates system design, automation flow, and agent orchestration.

2. Solution Overview

The solution is implemented as a Python-based multi-agent system where each agent has a single, clearly defined responsibility.

The system follows a pipeline-style orchestration flow, where:

Raw product data is parsed into a normalized internal representation

Content is generated using reusable logic blocks

Structured templates assemble final content pages

Outputs are saved as machine-readable JSON files

The system intentionally avoids machine learning models to keep the pipeline:

Deterministic

Explainable

Easy to test

Production-friendly

3. Scope & Assumptions
Scope

Input is limited strictly to the provided product dataset

Output includes:

FAQ Page

Product Description Page

Comparison Page (with a fictional Product B)

The system runs locally as a Python project

No UI, API, or deployment layer is included

Assumptions

External research or additional facts are not permitted

Product B used in comparison is fictional but structured

JSON outputs are intended for downstream consumption by other systems

4. System Design (Most Important Section)
4.1 Architecture Overview

The system is designed as a multi-agent pipeline with clear boundaries and no shared global state.

Input Data
   ↓
Data Parser Agent
   ↓
Content Logic Blocks
   ↓
Template Agent
   ↓
Assembly Agent
   ↓
JSON Outputs


Each stage operates independently and passes structured data to the next stage.

4.2 Agents & Responsibilities
Orchestrator Agent

Controls the execution flow

Ensures agents run in the correct order

Acts as the single entry point for the system

Data Parser Agent

Converts raw input data into a normalized internal format

Ensures consistent field naming and structure

Question Generator Agent

Generates categorized user questions

Provides structured inputs for FAQ generation

Content Logic Agents

Apply deterministic transformation rules

Examples:

Benefit extraction

Usage instructions

Safety notices

Ingredient summaries

Implemented as pure, stateless functions

Template Agent

Defines the structure of each page

Specifies required fields and formatting rules

Separates content structure from business logic

Assembly Agent

Collects final structured data

Writes clean, formatted JSON files to disk

4.3 Reusable Logic Blocks

Logic blocks are implemented as independent, reusable functions.
They:

Perform a single transformation

Do not depend on external state

Can be reused across multiple templates

This design allows new pages to be added without modifying existing logic.

4.4 Templates

Templates define what a page looks like, not how data is generated.

Implemented templates:

FAQ Page Template

Product Description Page Template

Comparison Page Template

Each template depends on logic blocks instead of embedding logic directly, improving maintainability and clarity.

4.5 Why No Machine Learning Model Was Used

No machine learning model was built because:

The assignment evaluates system design, not predictive modeling

Deterministic logic ensures explainability and correctness

Templates and rule-based logic are sufficient for structured content generation

This approach mirrors real-world production automation systems

This decision was intentional and aligned with the problem requirements.

5. Data & Output Structure

All final outputs are:

Valid JSON

Machine-readable

Deterministically generated

Directly traceable to input data

Generated files:

faq.json

product_page.json

comparison_page.json

6. Extensibility & Maintainability

The system is designed to be easily extended:

Adding a new page type requires only a new template

Existing agents and logic blocks remain unchanged

Each component can be tested independently

The codebase follows the principle:

“Write code as if someone else will maintain it tomorrow.”

7. Conclusion

This project demonstrates a clean, production-style agentic automation system built with:

Clear agent boundaries

Reusable logic blocks

Template-driven content generation

Deterministic, machine-readable outputs

The design prioritizes clarity, correctness, and maintainability, aligning closely with real-world systems used for scalable content generation.