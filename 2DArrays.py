def main():
    arr = [
           [1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 9, 2, -4, -4, 0],
           [0, 0, -1, -2, -4, 0],
           [0, 0, 1, 2, 4, 0]
    ]
    horizontal_len = len(arr[0]) - 2
    vertical_len = len(arr) - 2
    maximum = -9 * 7
    for y in range(horizontal_len):
        for x in range(vertical_len):
            top = arr[y][x] + arr[y][x+1] + arr[y][x+2]
            middle = arr[y+1][x+1]
            bottom = arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
            counter = sum_hourglass(top, middle, bottom)
            if counter > maximum:
                maximum = counter
    print(maximum)



def sum_hourglass(top, middle, bottom):
    return top + middle + bottom


main()