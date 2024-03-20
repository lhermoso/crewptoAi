from crewai import Agent

from tools.quote_tools import QuoteTool

from crewai_tools import (

    SerperDevTool,
    WebsiteSearchTool
)


quote_tool = QuoteTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool


class StockAnalysisAgents():
  def crypto_financial_analyst(self):
    return Agent(
      role='Top Cryptocurrency Financial Analyst',
      goal="""Impress all customers with your cutting-edge cryptocurrency market 
      insights and trend analysis""",
      backstory="""The most seasoned financial analyst specializing in the 
      cryptocurrency market, with extensive expertise in digital asset analysis 
      and investment strategies tailored for the volatile crypto market, now 
      serving a high-profile client.""",
      verbose=True,
      tools=[
        quote_tool,
        search_tool,
        web_rag_tool,
        YahooFinanceNewsTool()
      ]
    )
