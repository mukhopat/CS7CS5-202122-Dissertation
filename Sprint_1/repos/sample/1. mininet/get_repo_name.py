def get_repo_name ( target_string ):

	import re
	result = re.search ( r"^[0-9]+\.\s(.*)", target_string )
	return ( result.group(1) )
