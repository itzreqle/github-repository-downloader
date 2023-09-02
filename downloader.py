import argparse
import requests
import os

def download_public_repositories(username):
    base_url = f'https://api.github.com/users/{username}/repos'

    response = requests.get(base_url)

    if response.status_code == 200:
        repositories = response.json()
        
        # Create a directory with the username if it doesn't exist
        if not os.path.exists(username):
            os.makedirs(username)

        os.chdir(username)  # Change to the directory for saving repositories
        
        for repo in repositories:
            repo_name = repo['name']
            repo_url = repo['html_url']
            repo_clone_url = repo['clone_url']

            # Clone the repository using Git
            os.system(f'git clone {repo_clone_url}')

            print(f"Cloned {repo_name} from {repo_url}")
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download public GitHub repositories for a user.')
    parser.add_argument('username', type=str, help='GitHub username')

    args = parser.parse_args()

    download_public_repositories(args.username)
