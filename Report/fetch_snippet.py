commit_data = []

from pydriller import Repository

commit_data = [ [
        commit.hash, 
        commit.author.name, 
        commit.author.email,
        commit.committer_date,
        commit.merge,
        file.filename, 
        file.change_type, 
        file.added_lines, 
        file.deleted_lines,
        file.nloc,
        file.complexity,
        file.token_count
    ] for commit in Repository(repo_path).traverse_commits() 
    for file in commit.modified_files 
]
