import requests
import json

def get_village_chat():
    """Fetches the village chat data from the specified URL."""
    url = "https://theaidigest.org/village-chat"  # This is a placeholder
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
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
