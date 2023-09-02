# GitHub Repository Downloader

This Python script allows you to download all your own public GitHub repositories without the need for a personal access token. It's a convenient way to clone all your public repositories to your local machine for studying purposes.

## Prerequisites

Before you can use this script, make sure you have the following installed:

- Python 3.x
- Git (for cloning repositories)

## Usage

1. **Clone or download this repository**
    
    First, you need to obtain the script. You can either clone this repository or download the script directly.
    
    ```bash
    git clone https://github.com/itzreqle/github-repository-downloader.git
    ```
    
- **Navigate to the script's directory**
    
    Change your current directory to the one where you cloned or downloaded the script.
    
    ```bash
    cd github-repository-downloader
    ```
    
2. **Run the script**
    
- Run the Python script by providing your GitHub username as a command-line argument:
    
    ```bash
    python downloader.py your_username
    ```
    
3. **Wait for the script to complete**
    
    The script will fetch your public repositories from GitHub and clone each one to your local machine. You'll see progress messages indicating which repositories are being cloned.
    
4. **Access your repositories**
    
    Once the script has finished running, you'll find all your public repositories in your current directory.
    

## Note

- This script only downloads your own public repositories, and it doesn't require a personal access token. It respects GitHub's terms of service and access policies.
    
- If you have a large number of repositories, the script may take some time to complete, as it clones each repository one by one.
    
- Make sure you have Git installed on your machine to clone the repositories.
    

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.
