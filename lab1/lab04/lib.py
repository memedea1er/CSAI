def count_common_elements(*lists):
    common_elements = set(lists[0]).intersection(*lists[1:])

    return len(common_elements)