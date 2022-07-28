from urllib.parse import quote

search_query = u"GitHub Octocat in:readme user:defunkt"
print ( quote(search_query.encode("utf-8")) )
