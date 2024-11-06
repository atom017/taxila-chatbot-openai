import os
from dotenv import load_dotenv
import anthropic
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Load Anthropic API key from environment variable
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=anthropic_api_key)

# Create a prompt template for the chatbot
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the question as best as you can: {question}",
)


def answer_question(question):
    prompt = prompt_template.format(question=question)

    # Send a message to the Claude model via the Anthropic client
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",  # You can replace this with the correct model if necessary
        max_tokens=100,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["completion"].strip()


# Example usage for testing (can be removed later)
if __name__ == "__main__":
    question = "What is the capital of France?"
    print(answer_question(question))
