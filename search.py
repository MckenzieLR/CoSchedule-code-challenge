import requests

def search_api(query):
    url = " https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"  # Replace with the actual API endpoint URL
    
    params = {
        'q': query,
        'limit': 10,  # Number of results to retrieve
    }

    headers = {
        'User-Agent': 'Your-App-Name/1.0'  # Replace with your app's name and version
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:  # Successful request
        data = response.json()
        # Process the API response data here
        for result in data['results']:
            print(result)
    else:
        print("Error: Request failed with status code", response.status_code)

# Example usage
search_query = input("Enter search query: ")
search_api(search_query)