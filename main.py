import json
import csv


def main():
    with open('books-39204-271043.csv') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',', fieldnames=['Title', 'Author', 'Genre', 'Height', 'Publisher'])
        books = []
        for row in reader:
            books.append(row)
    del books[0]

    for elem in books:
        keys_needed = ['Title', 'Author', 'Height']
        for key, values in list(elem.items()):
            if key not in keys_needed:
                del elem[key]

    with open('users-39204-8e2f95.json') as json_file:
        reader = json.load(json_file)
        users = []
        for elem in reader:
            users.append(elem)

    ticker = 0
    for elem in users:
        elem['books'] = []
        elem['books'].append(books[ticker])
        ticker += 1
        keys_needed = ['name', 'gender', 'address', 'books']
        for key, values in list(elem.items()):
            if key not in keys_needed:
                del elem[key]

    with open("new_users.json", "w") as outfile:
        json.dump(users, outfile)


if __name__ == '__main__':
    main()
