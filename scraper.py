from langchain.scrapers import WebBaseLoader
import json

def scrape_scholarships():
    urls = [
        'https://scholarships.com/',
        'https://scholarshipscorner.website/scholarships/'
    ]
    
    all_scholarships = []

    for url in urls:
        loader = WebBaseLoader(url)
        data = loader.load()
        
        # Process data to extract relevant information
        for item in data:
            title = item.get('title', 'No title')
            link = item.get('link', 'No link')
            description = item.get('description', 'No description')
            all_scholarships.append({'title': title, 'link': link, 'description': description})

    # Save to JSON file
    with open('data/scholarships.json', 'w') as f:
        json.dump(all_scholarships, f)

if __name__ == '__main__':
    scrape_scholarships()
