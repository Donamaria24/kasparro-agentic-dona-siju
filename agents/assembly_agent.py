import json
import os

class AssemblyAgent:
    def save(self, data: dict, filename: str):
        os.makedirs("output", exist_ok=True)
        with open(f"output/{filename}", "w") as f:
            json.dump(data, f, indent=2)
