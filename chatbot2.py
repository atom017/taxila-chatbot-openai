import os
from langchain_openai import ChatOpenAI  # Use ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize ChatOpenAI with your API key
llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key, model="gpt-4")

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the question as best as you can: {question}",
)


def answer_question(question):
    response = llm.generate([prompt_template.format(question=question)])
    return response.generations[0][0].text.strip()


# Example usage
if __name__ == "__main__":
    question = "What scholarships are available for international students?"
    answer = answer_question(question)
    print(answer)
