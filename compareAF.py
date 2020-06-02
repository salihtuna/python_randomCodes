import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def abline(intercept, slope):
    x = np.array([0,1])
    y = slope * x + intercept
    plt.plot(x, y, '--', c='red')
    
    
def compare_AF(tb1,tb2):
    """ Compare AF between the two sets and plot """
    t1 = pd.read_table(tb1, header=None)
    t1.columns = ['pos','AF']
    t2 = pd.read_table(tb2,header=None)
    t2.columns = ['pos', 'AF']
    merged_table = pd.merge(t1, t2, on = 'pos', how = 'left', suffixes=('_t1','_t2'))
    plt.scatter(merged_table['AF_t1'], merged_table['AF_t2'], c='blue')
    plt.xlabel("AF_Tb1")
    plt.ylabel("AF_Tb2")
    abline(0,1)
    plt.show()

def filter_by_AF():
    merged_table['diff'] = merged_table["AF_t1"] - merged_table["AF_t2"]
    merged_table_filtered = merged_table[merged_table['diff'] < 0.1]
    merged_table_filtered
    plt.scatter(merged_table_filtered['AF_t1'], merged_table_filtered['AF_t2'], c='blue')
    plt.xlabel("AF_Tb1")
    plt.ylabel("AF_Tb2")
    abline(0,1)
    plt.show()


