import requests

def check_url(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except:
        return False
