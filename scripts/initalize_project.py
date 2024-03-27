import os
import subprocess

REPOSITORIES = ["frontend", "backend", "workspace.wiki", "shared"]
ORGANIZATION = "uzh-ase-fs24"


def configure_git(first_name, last_name, email):
    # Set the user.name configuration value
    subprocess.run(
        ["git", "config", "--global", "user.name", f"{first_name} {last_name}"]
    )

    # Set the user.email configuration value
    subprocess.run(["git", "config", "--global", "user.email", email])


def main():
    print("please enter your details for your git configuration:")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")

    for repo in REPOSITORIES:
        base_dir = os.getcwd()
        assert base_dir.endswith("workspace")
        repo_dir = os.path.join(base_dir, repo)

        # Check if the repository already exists
        if os.path.isdir(repo_dir):
            print(f"The directory {repo_dir} already exists. Skipping...")
            continue

        # Clone the repository
        subprocess.run(
            ["git", "clone", f"https://github.com/{ORGANIZATION}/{repo}.git"],
            cwd=base_dir,
        )

        # install pre-commit hooks
        if repo != "workspace.wiki":
            # Change the current working directory to the newly cloned repository
            os.chdir(repo_dir)

            # Run the pre-commit install command
            subprocess.run(["pre-commit", "install"])

            # configure git user
            configure_git(first_name, last_name, email)
            # Change the current working directory back to the base directory
            os.chdir(base_dir)


if __name__ == "__main__":
    main()
