def find_duplicate_arr(array):
    #Using Hash Table, the duplicates can be found in O(n) time.
    hash_table = {}
    ans = -1
    found = 0
    for x in array:
        if x in hash_table.keys():
            hash_table[x]+= 1
        else:
            hash_table[x] = 1
        if hash_table[x] > 1:
            found = 1
            ans = x
            break
    #Returns 2 variables, 1st is flag if 0 no duplicates, 2nd is the value
    return found,ans

def find_duplicate_dict(dictionary):
    #Using Hash Table, the duplicates can be found in O(n) time.
    hash_table = {}
    ans = -1
    found = 0
    for x in dictionary.keys():
        y = dictionary[x]
        if y in hash_table.keys():
            hash_table[y] += 1
        else:
            hash_table[y] = 1
        if hash_table[y] > 1:
            found = 1
            ans = y
            break
    #Returns 2 variables, 1st is flag if 0 no duplicates, 2nd is the value
    return found,ans
x,y = find_duplicate_arr([1,2,3,1,4,5])
print y
x,y = find_duplicate_dict({'0':1,'1':2,'3':5,'4':5})
print y