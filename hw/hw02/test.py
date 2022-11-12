def ratio(x, y):
    """
    >>> ratio(1, 2)
    >>> '1 / 2' <== prints this
    >>>  <== return this
    """

    return {"neum": x, "denom": y}


def neum(ratio):
    return ratio["neum"]


def denom(ratio):
    return ratio["denom"]


def mul_ratio(ratio1, ratio2):
    nx, ny = neum(ratio1), neum(ratio2)
    dx, dy = denom(ratio2), denom(ratio2)
    return ratio(nx * ny, dx * dy)


r1 = ratio(1, 2)
r2 = ratio(3, 4)

r3 = mul_ratio(r1, r2)

r4 = mul_ratio(r2, r3)

print(neum(r4))

r5 = mul_ratio(ratio(denom(r2), neum(r1)))
