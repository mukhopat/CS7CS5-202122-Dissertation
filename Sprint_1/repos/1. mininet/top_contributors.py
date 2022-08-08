def get_equilibrium_pc ( lst ):
    
    lst.sort(reverse=True)
    
    for idx in range ( len(lst) ):
        if ( sum(lst[0:idx]) >= sum(lst[idx:]) ):
            perc = round ( ( (idx + 1) / ( len(lst) + 1) ) * 100 )
            return perc
			
def get_pareto_pc ( lst ):
    
    lst.sort(reverse=True)
    total = sum(lst)
    
    for idx in range ( len(lst) ):
        if ( sum(lst[0:idx]) >= (0.8 * total) ):
            perc = round ( ( (idx + 1) / ( len(lst) + 1) ) * 100 )
            return perc
