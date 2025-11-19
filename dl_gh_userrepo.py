# download all repo of someone (for archival reasons)

import requests
import os
import subprocess

def download_all_repos(username, save_path="repos"):
    
    if not os.path.exists(save_path): os.makedirs(save_path)

    url = f"https://api.github.com/users/{username}/repos?per_page=200"

    print(f"[+] Fetching repositories for user: {username}")
    response = requests.get(url)

    if response.status_code != 200:
        print("[-] Failed to fetch repositories:", response.text)
        return

    repos = response.json()

    if not repos:
        print("No repo found.")
        return

    for repo in repos:
        name = repo['name']
        clone_url = repo['clone_url']
        repo_path = os.path.join(save_path, name)

        if os.path.exists(repo_path):
            print(f"Skipping: {name}")
            continue

        print(f"[+] Cloning {name} ...")
        subprocess.run(["git", "clone", clone_url, repo_path])

if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()
    download_all_repos(username)
