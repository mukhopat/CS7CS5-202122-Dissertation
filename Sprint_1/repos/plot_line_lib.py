import matplotlib.pyplot as plt
import matplotlib.dates as dates
import seaborn as sb
import numpy as np


def plot_line ( yplot, idx, df, folder_path, plot_name, major_locator ):

    covid_proxy_ym = '2020-03'
    fig, ax = plt.subplots ( figsize = (24, 8) )
    ax.scatter ( df['year_month'], df[yplot], color = 'y', label = yplot.replace('_',' ') )
    ax.plot ( df['year_month'], df['ma_' + yplot], color = 'b', label = 'Moving Average' )
    ax.axvline ( x = covid_proxy_ym, linewidth=2, color='r', label = 'Initial Covid-19 Lockdowns' )
    
    ax.set_title ( plot_name + ': month vs ' + yplot, fontsize = 20 )
    ax.set_xlabel ( 'month', fontsize = 15 )
    ax.set_ylabel ( yplot, fontsize = 15 )
    ax.legend()
    
    plt.setp ( ax.get_xticklabels(), fontsize = 12 )
    plt.setp ( ax.get_yticklabels(), fontsize = 12 )
    
    locator = dates.MonthLocator()
    if ( major_locator ):
        plt.gca().xaxis.set_major_locator(locator)
    plt.gcf().autofmt_xdate()
    plt.savefig ( f'{folder_path}{idx}. {plot_name}_{yplot}.jpg', bbox_inches = 'tight' )
