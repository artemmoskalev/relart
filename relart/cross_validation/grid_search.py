# @kwargs - extendable parameter list of the form var1=[a1, a2, .., an], var2=[b1, b2, ..., bn], ...
# @value - list of parameter permutations of the form [(a1, b1, ...), (a1, b2, ...), (a2, b1, ...), ...]
def cv_grid(**kwargs):
    """Returns a list of parameter tuples from the grid. 
    Each tuple is a unique permutation of parameters specified in kwargs"""
    key_list = list(kwargs.keys())
    return __assemble(key_list, kwargs, 0)

# Recursively called function which traverses the parameter tree to compose the list of all possible permutations
# @key_list - list of variable names, for which we need a cv-grid
# @param_select-dict - map of parameters matched with the lists of possible values,
#                      {var1: [a1, a2, .., an], var2:[b1, b2, ..., bn], ...}
# @key_inx - indicator variable for bookkeeping the variable which is currently processed.
#            If it is the same as the number of parameters, it means we have composed 1 unique permutations, 
#            and the lowest recursion level (last variable) returns
# @value - returns a list, which represents a partial permutation of CV-grid parameters 
#          (includes either some of them, or all of them if the whole tree has been traversed)
def __assemble(key_list, param_select_dict, key_inx):
    if key_inx < (len(key_list) - 1):
        f_combination_list = __assemble(key_list, param_select_dict, key_inx + 1)
    else:
        f_combination_list = []
        for param in param_select_dict[key_list[key_inx]]:
            f_combination_list.append({key_list[key_inx]: param})
        return f_combination_list
       
    c_combination_list = []
    for param in param_select_dict[key_list[key_inx]]:
        for f_dict in f_combination_list:
            c_dict = {key_list[key_inx]: param}
            c_dict.update(f_dict)
            c_combination_list.append(c_dict)
    
    return c_combination_list