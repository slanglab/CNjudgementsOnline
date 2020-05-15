import pandas as pd
import numpy as np
import math

#to assign the numerical value of blood content to bins,10mg/ml per bin

def getBloodContentBin(df):
    baContent = df['bloodAlcoholContent'].tolist()
    baBin = []
    numericalBin = []
    
    for ba in baContent:
        bin_ = math.ceil(ba/10)
        baBin.append('bin{}'.format(bin_))
        numericalBin.append(bin_)
    
    return baBin,numericalBin

        