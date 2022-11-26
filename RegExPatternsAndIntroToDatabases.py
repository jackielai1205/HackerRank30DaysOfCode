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
    N = 6
    data = ["riya riya@gmail.com", "julia julia@julia.me", "julia sjulia@gmail.com", "julia julia@gmail.com",
            "samantha samantha@gmail.com", "tanya tanya@gmail.com"]
    database = {}
    for N_itr in range(N):
        first_multiple_input = data[N_itr].split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        database[emailID] = firstName
    print(database)
    email_filter(database)




