import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    num = np.dot(a,b)
    a_den = np.linalg.norm(a)
    b_den = np.linalg.norm(b)
    if a_den == 0 or b_den == 0:
        return float(0)
    den = np.dot(a_den, b_den)
    return float(num/den)