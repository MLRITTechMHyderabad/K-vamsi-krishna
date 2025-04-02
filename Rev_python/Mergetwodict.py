def merge_dictionaries(dict1, dict2):
    merged = {}
    for key in dict1:
        merged[key] = dict1[key]
    for key in dict2:
        merged[key] = dict2[key]
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)