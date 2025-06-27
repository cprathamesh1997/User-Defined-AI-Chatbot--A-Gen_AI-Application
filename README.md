# User-Defined-AI-Chatbot :computer: A-Gen_AI-Application
A production-ready, agentic AI chatbot using LangGraph and Groq-backed LLMs with user defined search capabilities. It features a FastAPI backend and a Streamlit frontend, enabling users to interact with customizable large language model agents.

![Top-Industries-Using-AI-Chatbots-_1_-scaled___](https://github.com/user-attachments/assets/17372972-f781-4f04-bb7a-a4e5bd0d2d63)

## Techniques Used :arrow_right:

* __LangGraph Agents__ using create_react_agent to define AI behaviors with tool support.

* __Environment Variable__ Management via python-dotenv to manage API keys securely.

* __Model-specific__ instantiation of LLMs with conditionally enabled tools.

* __FastAPI Routing__ with Pydantic models for request validation and Swagger UI exposure.

* __Frontend-Backend__ Communication using requests.post() from Streamlit to FastAPI.

* __Conditional Tool Injection__ for search functionality.  __Tavily Search Results__ Enables real-time web-enhanced answers.

* __Streamlit UI widgets__ for model/provider selection, system prompts, and input handling.

* __Uvicorn__ as the ASGI server for local FastAPI hosting.

## Project Structure :arrow_right:

* __ai_agent.py__: Defines the core AI logic, integrates model selection, and search tool.

* __backend.py__: FastAPI app serving chat endpoints, handles agent invocation logic.

* __frontend.py__: Streamlit-based UI allowing interactive queries and model control.

