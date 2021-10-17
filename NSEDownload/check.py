from fuzzywuzzy import fuzz

# Checking for proper IndexName and suggesting closest alternative.


def check_name(arr, values, indexName):

    flag = 0
    for i in range(len(arr)):
        if(arr[i] == indexName or values[i] == indexName):
            indexName = arr[i]
            print(indexName)
            flag = 1

    maxi = 0
    maxVal = values[0]
    for compare in values:
        str1 = indexName
        str2 = compare

        Ratio = fuzz.ratio(str1.lower(), str2.lower())
        if(Ratio > maxi):
            maxVal = compare
            maxi = Ratio

    if(flag == 0):
        raise ValueError(
            "Please check symbol provided. Try {} as name.".format(maxVal))
