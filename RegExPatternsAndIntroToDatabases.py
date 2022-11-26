import re


def email_filter(table):
    output = []
    for key in table:
        result = re.search("[a-z]+@gmail.com", key)
        if result:
            output.append(table[key])

    for element in sorted(output):
        print(element)



if __name__ == '__main__':
    N = int(input().strip())
    database = dict()
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        database[emailID] = firstName
    email_filter(database)




