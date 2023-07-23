test_cases = int(input()) # getting the test case input

for test in range(test_cases):
    row, col = input().split(" ") # getting n,m value for each test case
    shape = 0
    for r in range(int(row)):
        cell_value = input() # getting cell value for each row
        # replacing dot with empty string, so we have only hashes
        cell_value = cell_value.replace(".","") 
        if(len(cell_value) > shape):
            shape = len(cell_value)
    print(shape)


# ---------------------------------*******------------------------------------

test_cases = int(input()) # getting the test case input

def find_shape(arr):
    count = 0
    shape_count = 0
    for ele in arr:
        if(ele == "#"):
            count += 1
            if(count > shape_count):
                shape_count = count
        else:
            count = 0
    return shape_count

def convert_row_to_col(arr, prev_col):
    temp_col = prev_col.copy()
    for i in range(len(arr)):
        if(len(temp_col) != 0):
            prev_col[i].append(arr[i])
        else:
            prev_col.append([arr[i]])
    return prev_col

for test in range(test_cases):
    row, col = input().split(" ") # getting n,m value for each test case
    shape = 0
    row_shape = 0
    col_shape = 0
    col_value_list = [] # list of lists
    for r in range(int(row)):
        row_value = input() # getting cell value for each row
        row_value_list = list(row_value)
        r_shape = find_shape(row_value_list)
        if(r_shape > row_shape):
            row_shape = r_shape
        col_value_list = convert_row_to_col(row_value_list, col_value_list)
    for c_value in col_value_list:
        c_shape = find_shape(c_value)
        if(c_shape > col_shape):
            col_shape = c_shape
    shape = max(row_shape, col_shape)
    print(shape)

