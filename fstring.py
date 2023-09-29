#write a format string which prints out the data using the following syntax:
#  Hello Robin. You are currently left with 10 chocolates.
def main():
    data=("Robin",10, "chocolates")
    format_string= None
    print(f"Hello {data[0]}. You are currently left with {data[1]} {data[2]}.")

    return 0

if __name__ == '__main__':
    main()