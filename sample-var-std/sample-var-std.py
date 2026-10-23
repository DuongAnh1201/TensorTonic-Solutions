import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    n = len(x)
    x = np.asarray(x)
    total = sum((x-np.mean(x))**2)
    s_2 = 1/(n-1)*total
    return {"variance": float(s_2), "standard_deviation": float(s_2**0.5)}
    