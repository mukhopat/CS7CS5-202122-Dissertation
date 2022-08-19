meanString = [
"commit count :  2  vs  2  ->  No change",
"additions :  66  vs  5  ->  Down (92.4%)",
"deletions :  68  vs  2  ->  Down (97.1%)",
"agg loc :  7  vs  13  ->  Up (85.7%)",
"agg complexity :  1  vs  2  ->  Up (100.0%)",
"agg token count :  46  vs  78  ->  Up (69.6%)"
]

preEqString = [
"commit_count = 7.1",
"additions = 0.2",
"deletions = 0.3",
"agg_loc = 0.2",
"agg_complexity = 0.2",
"agg_token_count = 0.2"
]
    
postEqString = [
"commit_count = 12.6",
"additions = 0.1",
"deletions = 0.3",
"agg_loc = 0.1",
"agg_complexity = 0.1",
"agg_token_count = 0.1"
]

pre80String = [
"commit_count = 51.8",
"additions = 0.3",
"deletions = 0.3",
"agg_loc = 0.2",
"agg_complexity = 0.2",
"agg_token_count = 0.2"
]
    
post80String = [
"commit_count = 59.8",
"additions = 10.9",
"deletions = 1.2",
"agg_loc = 0.1",
"agg_complexity = 0.1",
"agg_token_count = 0.1"
]

tab = '\t'

for idx in range ( len ( meanString ) ):
    print ( 
        meanString[idx].split("->  ",1)[1],
        tab,
        preEqString[idx].split("= ",1)[1],
        tab,
        postEqString[idx].split("= ",1)[1],
        tab,
        pre80String[idx].split("= ",1)[1],
        tab,
        post80String[idx].split("= ",1)[1]
    )
