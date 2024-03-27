import re
import sys


def main():
    # Get the commit message
    with open(sys.argv[1], "r") as file:
        commit_message = file.read()

    # Define the pattern
    same_repo_pattern = r"(frontend|backend|workspace|shared) #\d*:"
    different_repo_pattern = r"(uzh-ase-fs24\/)(frontend|backend|workspace|shared)#\d*:"

    # Check if the commit message matches the pattern
    if not re.match(same_repo_pattern, commit_message) and not re.match(
        different_repo_pattern, commit_message
    ):
        print("ERROR: Commit message does not match the required format.")
        print("Examples:")
        print("uzh-ase-fs24/workspace#27: small fix")
        print(different_repo_pattern)
        print("or")
        print("frontend #21: fixing bug")
        print(same_repo_pattern)
        print(commit_message)
        sys.exit(1)


if __name__ == "__main__":
    main()
