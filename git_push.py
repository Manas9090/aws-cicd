import git
import os

# Define the local repository path
repo_path = "C:\\AWS_CICD"  # Change this to your project path

# Define GitHub repository URL (use SSH or HTTPS)
github_repo_url = "https://github.com/Manas9090/aws-cicd.git"  # Change this

try:
    # Initialize the repository object
    repo = git.Repo(repo_path)

    # Check if the remote exists
    if "origin" not in [remote.name for remote in repo.remotes]:
        repo.create_remote("origin", github_repo_url)

    # Add all files to staging
    repo.git.add(A=True)

    # Commit changes
    repo.index.commit("Initial commit from Python script")

    # Push changes to GitHub
    repo.remotes.origin.push("main")  # Change "main" if your default branch is different

    print("Successfully pushed to GitHub!")
except Exception as e:
    print(f"Error: {e}")
