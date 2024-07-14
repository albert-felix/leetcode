def insertion_sort(unsorted_arr):
    sorted_arr = []
    for a in unsorted_arr:
        if(len(sorted_arr)) == 0:
            sorted_arr.append(a)
            continue
        for b_idx, b in enumerate(sorted_arr):
            flag = True
            if(a <= b):
                sorted_arr.insert(b_idx, a)
                flag = False
                break
        if(flag):
            sorted_arr.append(a)
    return sorted_arr


sorted_values = insertion_sort([9,8,7,4,3,1,98,1343,9,10])
print(sorted_values)
