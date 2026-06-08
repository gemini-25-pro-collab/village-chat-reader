import requests
from bs4 import BeautifulSoup
import json

def get_village_chat():
    """Fetches and scrapes the village chat data from the specified URL."""
    url = "https://theaidigest.org/village" 
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'lxml')
        
        # This is a placeholder for the actual scraping logic.
        # I will need to inspect the HTML of the village chat page
        # to determine the correct selectors.
        messages = []
        for item in soup.select("div.chat-message"): # Example selector
            author = item.select_one("span.author").text
            content = item.select_one("p.content").text
            messages.append({"author": author, "content": content})
            
        return messages
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching chat data: {e}")
        return None

def main():
    """Main function to fetch and display chat data."""
    chat_data = get_village_chat()
    if chat_data:
        print(json.dumps(chat_data, indent=2))

if __name__ == "__main__":
    main()
