import os
from git import Repo
from git.exc import GitCommandError
from datetime import datetime

now = datetime.now().isoformat("@", "seconds")
commit_message = "backup " + str(now)
# remember to export env variable
repo_token = os.getenv("GIT_TOKEN")
repo_folder = "."
repo = Repo(repo_folder)
repo_url = repo.remotes.origin.url.split('https://')[1]
#repo_token_url = "https://" + repo_token + "@" + repo_url
# test borken push
repo_token_url = "https://" + "@" + repo_url

def git_push(local_repo, msg, repourl_w_token):
    try:
        local_repo.git.add(".")
        local_repo.git.commit(m=msg)
        local_repo.git.push(repourl_w_token)
        print("Committed")
    except GitCommandError:
        print("nothing to commit, working tree clean")
    except Exception as e:
        print(e)
        #print('Some error occured while pushing the code')


git_push(repo, commit_message, repo_token_url)
