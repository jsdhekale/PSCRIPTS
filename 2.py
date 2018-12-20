import random
# Number of Integers in FIle : 5 Million (10^6)
# The amount of Space required = (Integer Size)*(Number of Integers)
#                              = 32*5000000 bits (38 MBytes)
# Therefore We can use an array to easily store the Numbers.
# If we use quick sort The number of Computations is O(N*lg(N))
# The Number of Computations is 5000000*lg(5000000) ~ O(111 Million Comparisons)
# THis will take less than 15-20 seconds in any of the Modern Computers
# While Testing The code ran in lest than 12 secs.

def sort_file(filename):
    f = open(filename,'r')
    text = f.read()
    lines = text.split('\n')
    lines = [x for x in lines if x != '']
    array = []
    for line in lines:
        array.append(int(line))

    array.sort()
    f_sorted = open(filename+str('_sorted'),'w')
    for x in array:
        f_sorted.write(str(x)+'\n')
    f_sorted.close()
    f.close()

sort_file('input')