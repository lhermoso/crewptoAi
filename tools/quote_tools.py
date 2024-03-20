from crewai_tools import BaseTool

import requests
import dotenv

dotenv.load_dotenv()
import os


class QuoteTool(BaseTool):
    name: str = "Download quote data"
    description: str = "Retrieves OHLC (Open, High, Low, Close) data and trading volume for a specified ticker symbol."

    def _run(self, ticker: str) -> str:

        params = {
            'coin': ticker,
            'currency': 'USD',
            'token': os.getenv("BRAP_API_KEY"),
        }

        response = requests.get("https://brapi.dev/api/v2/crypto", params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
