import csv

def read_file(file_path,expenses):
    """
    Creates a dictionary containing all expenses for the Semester. Each category is how the Credit Card defines
    each expense; Will be going in and changing

    :param file_path:
    :param expenses:
    :return:
    """
    fp = open(file_path, 'r')
    csv_reader = csv.reader(fp)
    header = next(csv_reader)

    for row in csv_reader:
        if len(row) > 0 and row[4] != "Payment/Credit":
            if row[3] == "JONNAS 2 GO" or row[3] == "HARPERS RESTAURANT & B" or row[3] == "THE RIV":
                if "Activities" not in expenses:
                    expenses["Activities"] = float(row[5])
                else:
                    expenses["Activities"] += float(row[5])

            elif row[4] not in expenses:
                expenses[row[4]] = float(row[5])

            else:
                expenses[row[4]] += float(row[5])

    return expenses


def write_dict_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in data.items():
            writer.writerow([key, value])

def main():
    expenses = dict()
    file1 = "Sep14-Oct14.csv"
    file2 = "Oct15-Nov13.csv"
    file3 = "Nov14-Dec14.csv"

    read_file(file1, expenses)
    read_file(file2, expenses)
    read_file(file3, expenses)

    print(expenses)
    total = 0
    for i in expenses.values():
        total += i

    print("Semester total: ", total)

   # write_dict_to_csv(expenses, "Sem_cc_expenses.csv")

if __name__ == '__main__':
    main()