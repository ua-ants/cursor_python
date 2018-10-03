# Create matrix based on first given element, number of rows and number of columns.
#
# Print that matrix to console creating border around it from "#" symbol.

def create_matrix(start:int, row:int, col:int):
    max_digit_size = len(str(start + row * col))
    print(max_digit_size)
    col_len = max_digit_size * col + col + 3
    print(col_len)
    print("#" * col_len)
    for j in range(row):
        print("# ", end="")
        for i in range(col):
            print_num = start + i
            print("{:^{width}}".format(print_num, width = max_digit_size),  end=" ")
        print_num += 1
        start = print_num
        print("#")
    print("#" * col_len)

