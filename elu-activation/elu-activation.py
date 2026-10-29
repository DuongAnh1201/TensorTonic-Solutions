import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    result = []
    for i in range(len(x)):
        if x[i]>0:
            result.append(x[i])
        else:
            a = alpha*(math.exp(x[i])-1)
            result.append(a)
    return result