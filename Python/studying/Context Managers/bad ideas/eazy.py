# This program is functional, but it has a big flaw.
# If the program fails to close the file, it will remain open until the program itself closes.


def main():
    my_file = open('books.txt')
    my_file.write('If Tomorrow Comes by Sidney Sheldon')
    my_file.close()


if __name__ == "__main__":
    main()
