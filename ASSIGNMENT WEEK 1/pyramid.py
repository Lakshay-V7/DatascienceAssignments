n = int(input("Enter number of rows: ")) #THIS CODE IS TO PRINT PYRAMID PATTERN BY TAKING INPUT FROM USER

for i in range(1, n + 1):
    spaces = "  " * (n - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)
