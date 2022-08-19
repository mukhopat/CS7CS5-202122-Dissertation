#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pydriller import Repository
from time import time
from datetime import timedelta
import os
from get_repo_name import get_repo_name

repo_name = get_repo_name ( os.path.basename ( os.getcwd() ) )
repo_path = f'./clone/{repo_name}'

commit_data = []

start_time = time()

commit_data = [ [
        commit.hash, 
        commit.author.name, 
        commit.author.email,
        commit.committer_date,
        commit.merge,
        commit.dmm_unit_size,
        commit.dmm_unit_complexity,
        commit.dmm_unit_interfacing,
        file.filename, 
        file.change_type, 
        file.added_lines, 
        file.deleted_lines,
        file.nloc,
        file.complexity,
        file.token_count
    ] for commit in Repository(repo_path).traverse_commits() for file in commit.modified_files 
]
   
print( f'Execution time = { str ( timedelta ( seconds = time() - start_time ) ) }' )


# In[ ]:


import pandas as pd

df = pd.DataFrame(commit_data)

df.columns = [
    'commit_hash', 
    'commit_author_name', 
    'commit_author_email',
    'commit_datetime', 
    'commit_merge',
    'dmm_unit_size',
    'dmm_unit_complexity',
    'dmm_unit_interfacing',
    'file_name', 
    'file_change_type', 
    'file_lines_added',
    'file_lines_deleted',
    'file_loc',
    'file_complexity',
    'file_token_count'
]

df


# In[ ]:


df.to_csv ( f'datasets/{repo_name}_modfiles.csv', index = False )


# In[ ]:

print ( 'Done!' )


