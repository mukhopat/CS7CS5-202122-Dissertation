df.insert ( 
    loc=1, 
    'year_month', 
    pd.to_datetime(df['commit_datetime'], 
                   utc=True).dt.to_period('M') )
df