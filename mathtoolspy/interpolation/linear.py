

def interpolation_linear(x, x1, x2, y1, y2):
    """
    Linear interpolation
    returns (y2 - y1) / (x2 - x1) * (x - x1) + y1
    """
    m = (y2 - y1) / (x2 - x1)
    t = (x - x1)
    return m * t + y1
