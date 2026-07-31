import requests

from langchain_core.tools import tool

@tool
def github_user(username: str) -> str:
    """Get github profile"""

    response = requests.get(f"https://api.github.com/users/{username}")

    if response.status_code != 200:
        return f"User not found: {username}"
    
    data = response.json()

    return f"""
Username: {data["login"]}
Followers: {data["followers"]}
Repositories: {data["public_repos"]}
Bio: {data["bio"]}
"""