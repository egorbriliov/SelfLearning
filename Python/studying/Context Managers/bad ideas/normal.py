def main():
    my_file = open('books.txt', 'w')

    try:
        my_file.write('If Tomorrow Comes by Sidney Sheldon')
    except Exception as e:
        print(f'writing to file failed: {e}')
    finally:
        my_file.close()


if __name__ == "__main__":
    main()
