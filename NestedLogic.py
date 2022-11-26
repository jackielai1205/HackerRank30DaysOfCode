def main():
    return_data = "12 12 2014"
    due_data = "1 12 2014"
    print(calculate_fine(return_data, due_data))


def calculate_fine(return_data, due_data):
    return_data = return_data.split()
    due_data = due_data.split()
    return_data_day = int(return_data[0])
    return_data_month = int(return_data[1])
    return_data_year = int(return_data[2])
    due_data_day = int(due_data[0])
    due_data_month = int(due_data[1])
    due_data_year = int(due_data[2])
    if due_data_year < return_data_year:
        return 10000
    elif due_data_year > return_data_year:
        return 0
    if due_data_month < return_data_month:
        return 500 * (return_data_month - due_data_month)
    elif due_data_month > return_data_month:
        return 0
    if due_data_day < return_data_day:
        return 15 * (return_data_day - due_data_day)
    return 0



main()