def flatten(iterable):
    ret = []
    print(iterable)
    for elem in iterable:
        if isinstance(elem, list):
            ret.extend(flatten(elem))
        elif elem is None:
            continue
        else:
            ret.append(elem)
    return ret
