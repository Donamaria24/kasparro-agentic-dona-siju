from agents.data_parser_agent import DataParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.assembly_agent import AssemblyAgent
from templates.faq_template import faq_template
from templates.product_template import product_template
from templates.comparison_template import comparison_template

class OrchestratorAgent:
    def run(self, raw_data: dict):
        parser = DataParserAgent()
        product = parser.run(raw_data)

        assembler = AssemblyAgent()

        assembler.save(faq_template(product), "faq.json")
        assembler.save(product_template(product), "product_page.json")
        assembler.save(comparison_template(product), "comparison_page.json")
