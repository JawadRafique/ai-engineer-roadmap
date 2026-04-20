from langchain_ollama import OllamaLLM
from langchain_classic.agents import AgentType, initialize_agent, load_tools


# Initialize Ollama LLM (ensure Ollama server is running and llama3 model is pulled)
llm = OllamaLLM(model="llama3", base_url="http://localhost:11434")
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True # Set to True to see the agent's thought process in the console logs
)

def generateChatResponse(chatInput):
    response = agent.run(chatInput)
    return response