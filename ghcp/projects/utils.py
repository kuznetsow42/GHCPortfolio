import requests


def get_projects() -> list:
    URL = "https://api.github.com/users/kuznetsow42/repos"
    response = requests.get(URL)
    return response.json()
