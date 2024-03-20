from crewai import Crew
from textwrap import dedent

from crypto_tasks import CryptocurrencyAnalysisTasks
from crypto_agents import CryptocurrencyAnalysisAgents

from dotenv import load_dotenv

load_dotenv()


class CryptoCrew:
    def __init__(self, crypto):
        agents = CryptocurrencyAnalysisAgents()

        self.crypto = crypto
        self.crypto_financial_analyst = agents.crypto_financial_analyst()
        self.crypto_research_analyst = agents.crypto_research_analyst()
        self.crypto_investment_advisor = agents.crypto_investment_advisor()

    def run(self):
        tasks = CryptocurrencyAnalysisTasks()
        research_task = tasks.market_research(self.crypto_financial_analyst, self.crypto)
        financial_task = tasks.tokenomics_analysis(self.crypto_research_analyst)
        blockchain_task = tasks.blockchain_analysis(self.crypto_research_analyst)
        recommend_task = tasks.investment_recommendation(self.crypto_investment_advisor)

        crew = Crew(agents=[self.crypto_financial_analyst,
                            self.crypto_research_analyst,
                            self.crypto_investment_advisor

                            ],
                    tasks=[research_task,
                           financial_task,
                           blockchain_task,
                           recommend_task],
                    verbose=True
                    )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Bem-vindo à Equipe de Análise Cripto IA")
    print('-------------------------------')
    crypto = input(
        dedent("""
           Qual é a criptomoeda que você deseja analisar?
        """))

    cripto_crew = CryptoCrew(crypto)
    result = cripto_crew.run()
    print("\n\n########################")
    print("## Aqui está o Relatório")
    print("########################\n")
    print(result)
