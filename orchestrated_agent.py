import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from tools.products_display_tool import ProductsDisplayTool
from tools.search_product_by_category import SearchProductByCategory


class OrchestratedAgent:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Initialize OpenAI with API key from environment
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_model = os.getenv("OPENAI_MODEL")

        with open("agent_instructions.json", "r") as f:
            self.instructions = json.load(f)

        # Initialize tools
        self.tools = {
            "products_display": ProductsDisplayTool(),
            "search_products": SearchProductByCategory()
        }

    def get_response(self, prompt: str) -> str:
        """Route prompt to OpenAI using the API."""
        try:
            # Make the API call to OpenAI for chat completions
            completion = OpenAI(api_key=self.openai_api_key).chat.completions.create(
                model=self.openai_model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=150
            )
            return completion['choices'][0]['message']['content']
        except Exception as e:
            return f"An error occurred while processing the request: {str(e)}"
