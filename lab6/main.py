import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = 'https://api.github.com'
TOKEN = os.getenv('GITHUB_TOKEN')


def list_user_repos():
    headers = {'Authorization': f'Bearer {TOKEN}'}
    response = requests.get(f'{API_URL}/user/repos', headers=headers)

    #print(f"Status Code: {response.status_code}")
    #print(f"Response Text: {response.text}")

    return response.json()


if __name__ == "__main__":
    repos = list_user_repos()

    if isinstance(repos, list):
        for repo in repos:
            print(repo['name'])
    else:
        print("Не удалось получить список репозиториев.")
