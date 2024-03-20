from crewai import Task
from textwrap import dedent
from datetime import datetime

class CryptocurrencyAnalysisTasks:
    def market_research(self, agent, cryptocurrency):
        return Task(description=dedent(f"""
        Collect and summarize recent news articles, blog posts,
        and analyses related to the cryptocurrency, its underlying
        technology, and its ecosystem.
        Focus on market sentiment, technological advancements, 
        regulatory news, and significant events within the 
        cryptocurrency community.

        Your final answer MUST be a report that includes a
        comprehensive summary of the latest developments, any notable
        shifts in sentiment, and potential impacts on the 
        cryptocurrency's value.
        Also, include the cryptocurrency's ticker or symbol.

        {self.__tip_section()}

        Use the most recent and reliable data available.

        Selected cryptocurrency by the customer: {cryptocurrency}
      """),
                    agent=agent,
                    expected_output="A comprehensive report including a summary of recent news, technological "
                                    "advancements, regulatory changes, and significant community events related to "
                                    "the specified cryptocurrency. The report should analyze market sentiment, "
                                    "its potential impact on the cryptocurrency's value, and include the "
                                    "cryptocurrency's ticker or symbol."
                    )

    def tokenomics_analysis(self, agent):
        return Task(description=dedent(f"""
        Perform a detailed analysis of the cryptocurrency's 
        tokenomics, including its supply dynamics, distribution
        scheme, utility, and incentives within the ecosystem.
        Compare these aspects with similar projects in the space
        to gauge its competitiveness and potential for growth.

        Your final report MUST elaborate on the tokenomics and 
        provide a clear assessment of its strengths and weaknesses,
        and its position in the broader cryptocurrency market.

        {self.__tip_section()}

        Ensure the use of up-to-date and accurate data.
      """),
                    agent=agent,
                    expected_output="A detailed report on the cryptocurrency's tokenomics, comparing supply dynamics, "
                                    "distribution scheme, utility, and ecosystem incentives with similar projects. "
                                    "The report should assess the strengths, weaknesses, and market position of the "
                                    "cryptocurrency's tokenomics."
                    )

    def blockchain_analysis(self, agent):
        return Task(description=dedent(f"""
        Analyze the blockchain data for the cryptocurrency, focusing
        on transaction volumes, wallet activities, and on-chain metrics.
        Evaluate the network's health, security, and activity levels
        to infer potential trends or concerns.

        Your final answer must include insights from blockchain analysis,
        highlighting any noteworthy patterns or indicators that might 
        affect the cryptocurrency's future trajectory.

        {self.__tip_section()}        
      """),
                    agent=agent,
                    expected_output="An analytical report based on blockchain data analysis, including transaction "
                                    "volumes, wallet activities, and on-chain metrics. The report should provide "
                                    "insights into the network's health, security, activity levels, and identify "
                                    "significant patterns or indicators influencing the cryptocurrency's future."
                    )

    def investment_recommendation(self, agent):
        return Task(description=dedent(f"""
        Integrate insights from the market research, tokenomics analysis,
        and blockchain analysis tasks.
        Formulate a comprehensive investment recommendation based on
        a holistic view of the cryptocurrency's prospects.

        Your recommendation MUST include considerations of market
        sentiment, technical and fundamental analysis, and potential
        future developments. 

        Provide a well-structured and detailed report, offering a clear
        investment perspective with substantiated reasoning.

        {self.__tip_section()}
      """),
                    agent=agent,
                    expected_output="An in-depth investment recommendation report integrating insights from market "
                                    "research, tokenomics, and blockchain analysis. The report should offer a clear "
                                    "investment perspective based on market sentiment, technical and fundamental "
                                    "analysis, and anticipated developments. After finalizing the report, "
                                    "it should be translated into Brazilian Portuguese to make it accessible to "
                                    "Portuguese-speaking stakeholders."
                    )

    def __tip_section(self):
        return (f"""Remember, excellence in your analysis could earn you a significant bonus!
                
                Current Year: {datetime.now().year}
                """)
