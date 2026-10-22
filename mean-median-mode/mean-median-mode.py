from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    hash_check = {}
    for i in x:
        if i in hash_check:
            hash_check[i] += 1
        else:
            hash_check[i] = 1
    biggest = 0
    most_fre = 0
    for i in hash_check:
        if hash_check[i]> biggest:
            biggest = hash_check[i]
            most_fre = float(i)
            
    x = np.asarray(x)
    d = {"mean": float(np.mean(x)), "median": float(np.median(x)), "mode": most_fre}
    return d