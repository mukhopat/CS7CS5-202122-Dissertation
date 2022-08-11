import git
import os
from get_repo_name import get_repo_name
import winsound

repo_name = get_repo_name ( os.path.basename ( os.getcwd() ) )

clone_dir_path = 'clone/'
url_suffix = '_url.txt'
url_file_path = clone_dir_path + repo_name + url_suffix

with open ( url_file_path ) as url_file:
  url = url_file.readline()

git.Repo.clone_from ( url, clone_dir_path + repo_name )

print ( 'Done!' )
winsound.MessageBeep ( type = -1 )
