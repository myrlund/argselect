
def argselect(fn, params, result_selector_fn):
    items = [(fn(p), p) for p in set(params)]
    result = result_selector_fn(map(lambda item: item[0], items))
    return map(lambda item: item[1], filter(lambda item: item[0] == result, items))

def argmax(fn, params):
    """
    Returns the parameter maximizing fn.
    """
    return argselect(fn, params, max)

def argmin(fn, params):
    """
    Returns the parameter minimizing fn.
    """
    return argselect(fn, params, min)

if __name__ == '__main__':
    import sys
    
    print "Using the square function."
    fn = lambda x: x ** 2
    
    params = map(int, sys.argv[1:])
    
    result_max = argmax(fn, params)
    print "argmax of %s: %s" % (", ".join(map(str, set(params))), ", ".join(map(str, result_max)))
    
    result_min = argmin(fn, params)
    print "argmin of %s: %s" % (", ".join(map(str, set(params))), ", ".join(map(str, result_min)))
