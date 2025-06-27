from dotenv import load_dotenv
load_dotenv()

#Setup API Keys for Groq and Tavily
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

#Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

groq_llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=GROQ_API_KEY)
search_tool = TavilySearchResults(max_results=2)

#Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt = "Act as an AI chatbot who is smart and friendly."


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, groq_api_key=GROQ_API_KEY)
    else:
        raise ValueError("Only Groq provider is currently supported.")

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    if isinstance(query, str):
        query = [{"role": "user", "content": query}]
    elif isinstance(query, list):
        query = [{"role": "user", "content": q} for q in query]

    state = {"messages": query}
    response = agent.invoke(state)

    from langchain_core.messages.ai import AIMessage
    messages = response.get("messages", [])
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

    return {"response": ai_messages[-1] if ai_messages else "No response generated."}
