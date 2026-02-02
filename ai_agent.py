from dotenv import load_dotenv
load_dotenv()

import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, SystemMessage

# API Keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):

    # Select LLM
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, groq_api_key=GROQ_API_KEY)
    else:
        raise ValueError("Only Groq provider is currently supported.")

    # Enable tools conditionally
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # Create ReAct agent (NO state_modifier)
    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Build messages with System Prompt
    messages = [SystemMessage(content=system_prompt)]

    if isinstance(query, str):
        messages.append({"role": "user", "content": query})
    elif isinstance(query, list):
        for q in query:
            messages.append({"role": "user", "content": q})

    state = {"messages": messages}

    # Invoke agent
    response = agent.invoke(state)

    # Extract final AI message
    ai_messages = [
        msg.content for msg in response.get("messages", [])
        if isinstance(msg, AIMessage)
    ]

    return {"response": ai_messages[-1] if ai_messages else "No response generated."}

