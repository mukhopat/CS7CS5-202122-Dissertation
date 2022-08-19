def calc_and_compare_means ( df1, df2, colStart, colEnd ):
    
    print ( 'Pre and Post-Covid Mean Comparisons:' )
    
    for idx in range(colStart, colEnd):
        
        pre_mean = get_mean ( df1[df1.columns[idx]] )
        post_mean = get_mean ( df2[df2.columns[idx]] )
        mean_trend = get_trend ( pre_mean, post_mean )
        print ( df1.columns[idx].replace('_',' '), ': ', 
            pre_mean, ' vs ', post_mean, ' -> ', mean_trend )