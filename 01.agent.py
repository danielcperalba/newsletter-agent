from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model = OpenAIChat(id="gpt-4.1-mini"),
    tools = [TavilyTools()],
    debug_mode = True
)

agent.print_response("Use suas ferramentas para pesquisar possíveis oportunidades de investimento em startups de tecnologia no Brasil. Forneça uma lista das 5 principais startups, incluindo uma breve descrição de cada uma e o motivo pelo qual elas são promissoras.")