import json
from langchain import OpenAI, ConversationChain
from langchain.prompts import PromptTemplate
import os

# Load OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI with your API key
llm = OpenAI(temperature=0.7)

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["question", "scholarships"],
    template="You are a helpful assistant for the University of Taxila's scholarship program. Answer the question based on the available scholarships data: {question} \nScholarships data: {scholarships}"
)

# Create a conversation chain
conversation = ConversationChain(llm=llm, prompt=prompt_template)

# Load scholarships data
with open('data/scholarships.json') as f:
    scholarships = json.load(f)

def answer_question(question):
    response = conversation.predict(question=question, scholarships=scholarships)
    return response
