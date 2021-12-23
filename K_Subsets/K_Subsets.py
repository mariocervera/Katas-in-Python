def all_k_subsets(input_list):
    result = []

    N = len(input_list) + 1
    for k in range(N):
        for k_subset in k_subsets(input_list, k):
            result.append(k_subset)

    return result

def k_subsets(input_list, k):
    result = []

    if(k == 0):
        result.append([])
    else:
        for element in input_list:
            input_list = remove_first_element_from(input_list)
            subsets = k_subsets(input_list, k-1)
            for subset in subsets:
                result.append(join_as_list(element, subset))

    return result

def remove_first_element_from(input_list):
    return input_list[1:]

def join_as_list(head, tail):
    l = [head]
    l.extend(tail)
    return l