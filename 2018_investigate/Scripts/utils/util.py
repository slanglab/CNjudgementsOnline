import numpy as np


def reject_outliers(data, m = 2.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s<m]

def getPercentileList(data, p):
    percentile = np.percentile(data, p, axis=0)
    newList = []
    for d in data:
        if d < percentile:
            newList.append(d)
    return newList