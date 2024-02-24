import requests

def check_repositories_exist(url):
    try:
        response = requests.get(url)
        data = response.json()
        repositories = data if isinstance(data, list) else []
        if len(repositories) >= 5:
            print("There are at least 5 repositories available.")
        else:
            print("There are not enough repositories available.")
    except Exception as e:
        print("Error occurred while fetching repositories:", e)

api_url = "https://api.github.com/users/avielb/repos"
check_repositories_exist(api_url)