string_list = [
    "commit count :  1006  vs  863  ->  Down (14.2%)",
    "additions :  120629  vs  99765  ->  Down (17.3%)",
    "deletions :  78363  vs  58480  ->  Down (25.4%)",
    "agg loc :  373344  vs  399552  ->  Up (7.0%)",
    "agg complexity :  45031  vs  39634  ->  Down (12.0%)",
    "agg token count :  1884715  vs  1877377  ->  Down (0.4%)"
]

for string in string_list:
    print( string.split("->",1)[1] )
