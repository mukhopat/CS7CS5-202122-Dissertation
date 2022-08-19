def calc_perc ( idx, length ):
    
    perc = (idx + 1) / length * 100
    return perc


def get_equilibrium_pc ( lst ):
    
    lst.sort ( reverse = True )
    
    for idx in range ( len(lst) ):
        if ( sum(lst[0:idx+1]) >= sum(lst[idx+1:]) ):
            perc = calc_perc ( idx, len(lst) )
            if perc > 50:
                perc = 50 - ( perc - 50 )
                
            perc = "{:.1f}".format(perc)
            return perc