# Create matrix based on first given element, number of rows and number of columns.
#
# Print that matrix to console creating border around it from "#" symbol.

def create_matrix(start:int, row:int, col:int):
    print("#" * (3 * col + 4))
    for j in range(row):
        print("# ", end="")
        for i in range(col):
            print_num = start + i
            print(print_num,  end=" ")
        start = print_num
        print(" #")
    print("#" * (3 * col + 4))
