def main():
    S = "uuhwei12"
    #Your code goes here
    print(any(i.isalnum() for i in S))
    print(any(i.isalpha() for i in S))
    print(any(i.isdigit() for i in S))
    print(any(i.islower() for i in S))
    print(any(i.isupper() for i in S))
    
    return 0

if __name__ == '__main__':
    main()