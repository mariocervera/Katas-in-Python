# In this program, sets are represented as lists because the order of the elements is important.

def all_k_subsets(input_set):
    result = []

    N = len(input_set) + 1
    for k in range(N):
        for k_subset in k_subsets(input_set, k):
            result.append(k_subset)

    return result

def k_subsets(input_set, k):
    result = []

    if k == 0:
        result.append([])
    else:
        for element in input_set:
            input_set = __remove_first_element(input_set)
            for subset in k_subsets(input_set, k-1):
                result.append(__join(element, subset))

    return result

def __remove_first_element(input_set):
    return input_set[1:]

def __join(head, tail):
    result = [head]
    result.extend(tail)
    return result