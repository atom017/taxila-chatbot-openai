import json
import os
import requests
from bs4 import BeautifulSoup
from langchain_community.llms import OpenAI  # For LLM
from langchain_openai import ChatOpenAI  # Use ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


openai_api_key = os.getenv('OPENAI_API_KEY')


llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)

#  prompt template
prompt_template = PromptTemplate(
    input_variables=["question", "scholarships"],
    template="You are a helpful assistant for the University of Taxila. You help users by giving scholarship information from Scholarship Corner. Answer the question based on the available scholarships data: {question} \nScholarships data: {scholarships}"
)

# Function to scrape scholarship data from the website
def scrape_scholarships():
    url = "https://scholarshipscorner.website/scholarships/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    scholarships = []

    # Find all scholarship articles
    articles = soup.find_all('article')
    for article in articles:
        title_tag = article.find('h2', class_='entry-title')
        title = title_tag.get_text()
        link = title_tag.find('a')['href']
        published_date = article.find('span', class_='published').get_text()

        # Append the scholarship details to the list
        scholarships.append({
            'title': title,
            'link': link,
            'published_date': published_date
        })

    return scholarships

# Load scholarships data by scraping
scholarships = scrape_scholarships()

def answer_question(question):
    formatted_scholarships = json.dumps(scholarships, indent=2)  
    response = llm.generate([prompt_template.format(question=question, scholarships=formatted_scholarships)])
    return response.generations[0][0].text.strip()

# Example usage
if __name__ == "__main__":
    question = "What scholarships are available for international students?"
    answer = answer_question(question)
    print(answer)
