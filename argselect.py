
def argselect(fn, params, result_selector_fn):
    """
    Returns the params selected by result_selector_fn, after applying fn.
    """
    
    # Apply fn to param set
    param_set = set(params)
    results = map(fn, param_set)
    
    # Select desired result
    selected_result = result_selector_fn(results)
    
    # Get the list indices matching the selected result
    filtered_results = filter(lambda item: item[1] == selected_result, enumerate(results))
    relevant_indices = map(lambda item: item[0], filtered_results)
    
    # Get the corresponding params
    params_with_indices = filter(lambda item: item[0] in relevant_indices, enumerate(param_set))
    params = map(lambda item: item[1], params_with_indices)
    
    return params

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
