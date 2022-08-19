def calc_perc ( idx, length ):
    
    perc = (idx + 1) / length * 100
    return perc

			
def get_pareto_pc ( lst ):
    
    lst.sort ( reverse = True )
    total = sum(lst)
    
    for idx in range ( len(lst) ):
        if ( sum(lst[0:idx+1]) >= (0.8 * total) ):
            perc = calc_perc ( idx, len(lst) )
            if perc > 80:
                perc = 80
                
            perc = "{:.1f}".format(perc)
            return perc