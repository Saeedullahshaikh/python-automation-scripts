import requests

def fetch_api(url, params=None, headers=None):
    """
    Fetch data from an API endpoint.

    url: the API URL
    params: optional query parameters
    headers: optional HTTP headers

    Returns JSON data if successful, or None if there's an error.
    """
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()  # raise exception for bad responses
        print(f"Successfully fetched data from {url}")
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")
    
    return None
