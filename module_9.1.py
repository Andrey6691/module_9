def apply_all_func(int_list, *functions):
    results={}
    for function in functions:
        result = function(int_list)
        results[function.__name__]= result
    return results


def min_(args):
    return min(args)


def max_(args):
    return max(args)


def len_(args):
    return len(args)


def sum_(args):
    return sum(args)

def sorted_(args):
    return sorted(args)


print(apply_all_func([6, 20, 15, 9], max_, min_))
print(apply_all_func([6, 20, 15, 9], len_, sum_, sorted_))
