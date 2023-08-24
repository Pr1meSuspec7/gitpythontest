import os
from git import Repo
from datetime import datetime

now = datetime.now().isoformat("@", "seconds")
commit_message = "backup " + str(now)
repo_token = "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"
repo_folder = "."
repo = Repo(repo_folder)
repo_url = repo.remotes.origin.url.split('https://')[1]
repo_token_url = "https://" + repo_token + "@" + repo_url

#repo.git.add(".")
#repo.git.commit(m=commit_message)
#repo.git.push(repo_token_url)


def git_push(local_repo, msg, repourl_w_token):
    try:
        local_repo.git.add(".")
        local_repo.git.commit(m=msg)
        local_repo.git.push(repourl_w_token)
        print("Backup committed")
    except:
        print('Some error occured while pushing the code')    

git_push(repo, commit_message, repo_token_url)
