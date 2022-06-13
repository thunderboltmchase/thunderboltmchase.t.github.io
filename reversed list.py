def my_reverse(l):
    output = []
    index = len(l) - 1
    while(index>= 0):
        output.append(l[index])
        print(l[index])
        index -= 1
    return output

print(my_reverse([9,6,5,5]))