"""return words from one string that are in the second one"""

def in_array(array1, array2):
    """
    return words from one string that are in the second one

    Args:
        array1 (array[string]): array of string
        array2 (array[string]): array of string

    Returns:
        array: array of strings
    """
    final = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and a1 not in final:
                final.append(a1)
    return sorted(final)

print(in_array(["arp", "live", "strong"],["lively", "alive", "harp", "sharp", "armstrong"]))
