import numpy as np

year_pre_covid_ym = '2019-03'
pre_covid_ym = '2020-02'
covid_ym = '2020-03'
year_post_covid_ym = '2021-02'


def calc_perc ( idx, length ):
    
    perc = round ( (idx + 1) / length * 100 )
    return perc


def get_equilibrium_pc ( lst ):
    
    lst.sort ( reverse = True )
    
    for idx in range ( len(lst) ):
        if ( sum(lst[0:idx+1]) >= sum(lst[idx+1:]) ):
            perc = calc_perc ( idx, len(lst) )
            if perc > 50:
                perc = 50 - ( perc - 50 )
            return perc

			
def get_pareto_pc ( lst ):
    
    lst.sort ( reverse = True )
    total = sum(lst)
    
    for idx in range ( len(lst) ):
        if ( sum(lst[0:idx+1]) >= (0.8 * total) ):
            perc = calc_perc ( idx, len(lst) )
            if perc > 80:
                perc = 80
            return perc


def get_mean ( series ):
    
    array = np.array ( series ).astype ( int )
    mean = np.mean ( array )
    mean = int ( round(mean) )
    return mean


def get_trend ( before, after ):
    
    if before < after:
        if before == 0:
            return f'Up from {before} to {after}'
        change = ( after - before ) * 100 / before
        change = "{:.1f}".format(change)
        return f'Up ({change}%)'
    
    if before > after:
        if before == 0:
            return f'Down from {before} to {after}'
        change = ( before - after ) * 100 / before
        change = "{:.1f}".format(change)
        return f'Down ({change}%)'
    
    if before == after:
        return 'No change'

    
def calc_and_compare_means ( df1, df2 ):
    
    print ( 'Pre and Post-Covid Mean Comparisons:' )
    
    for idx in range(1, 7):
        
        pre_mean = get_mean ( df1[df1.columns[idx]] )
        post_mean = get_mean ( df2[df2.columns[idx]] )
        mean_trend = get_trend ( pre_mean, post_mean )
        print ( df1.columns[idx].replace('_',' '), ': ', pre_mean, ' vs ', post_mean, ' -> ', mean_trend )


def generate_ordinal_encoding_map ( series ):
    enc_map = series.unique()
    enc_map = dict ( enumerate( enc_map.flatten(), 1 ) )
    enc_map = { val: key for key, val in enc_map.items() }
    enc_map['None'] = 0
    return enc_map
