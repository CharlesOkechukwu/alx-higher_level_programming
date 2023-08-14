#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    add tupules together
    """
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    if (a_len >= 2) and (b_len >= 2):
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif (a_len >= 2) and (b_len < 2):
        if (b_len <= 0):
            return tuple_a
        else:
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    elif (a_len < 2) and (b_len >= 2):
        if (a_len <= 0):
            return tuple_b
        else:
            return (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
    else:
        if (len_a <= 0) and (len_b <= 2):
            return tuple_b
        elif (len_b <= 0) and (len_a <= 2):
            return tuple_a
        elif (len_b <= 0) and (len_a <= 0):
            return (0, 0)
        else:
            return (tuple_a[0] + tuple_b[0], 0 + 0)
