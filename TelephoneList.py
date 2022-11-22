def get_input():
    input()


def main():
    contact_book = dict()
    input_number = int(input())
    for x in range(input_number):
        contact_info = input().split()
        contact_book[contact_info[0]] = contact_info[1]

    for x in range(input_number):
        key = input()
        if key in contact_book.keys():
            print(key + "=" + contact_book[key])
        else:
            print("Not found")


main()
