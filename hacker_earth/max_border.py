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

