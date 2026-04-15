from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.llm import LLMChain
from langchain_classic.chains.sequential import SequentialChain

# Initialize Ollama LLM (ensure Ollama server is running and llama3 model is pulled)
llm = OllamaLLM(model="llama3", base_url="http://localhost:11434")

# Prompt template for restaurant name generation
restaurant_prompt = PromptTemplate(
    input_variables=["cuisine"],
    template=(
        "I want to open a restaurant for a {cuisine} cuisine. "
        "Respond only with a single creative restaurant name, no explanation, no list, just the name."
    )
)

menu_prompt = PromptTemplate(
    input_variables=["restaurant_name", "cuisine"],
    template=(
        "Suggest 5 unique dishes for a {cuisine} restaurant named {restaurant_name}. "
        "Respond only with a comma-separated list of dish names, no explanation, no numbering, just the names."
    )
)

def generate_restaurant_name_and_menu(cuisine):
	# chain1
  restaurantNameChain = LLMChain(llm=llm, prompt=restaurant_prompt, output_key="restaurant_name")
  print("Generating restaurant name...", restaurantNameChain)

  # chain2
  menuChain = LLMChain(llm=llm, prompt=menu_prompt, output_key="menu")
  print("Generating menu...", menuChain)

  # Combine chains into a sequential chain
  chain = SequentialChain(chains=[restaurantNameChain, menuChain], input_variables=["cuisine"], output_variables=["restaurant_name", "menu"])
  
  response = chain({"cuisine": cuisine})

  print("Generated restaurant name and menu:", response)
  return response