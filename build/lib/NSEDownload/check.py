from fuzzywuzzy import fuzz


def check_name(arr, values, name):
    """Checking for proper Name and suggesting closest alternative.

    Args:
        arr (list): List of stocks or indices
        values (list): List of stocks or indices
        name (str): Name of stock or index

    Raises:
        ValueError: If the name is not in the list then raises error and suggests alternative
    """
    flag = 0
    for i in range(len(arr)):
        if(arr[i] == name or values[i] == name):
            name = arr[i]
            print(name)
            flag = 1

    maxi = 0
    maxVal = values[0]
    for compare in values:
        str1 = name
        str2 = compare

        Ratio = fuzz.ratio(str1.lower(), str2.lower())
        if(Ratio > maxi):
            maxVal = compare
            maxi = Ratio

    if(flag == 0):
        raise ValueError(
            "Please check symbol provided. Try {} as name.".format(maxVal))
