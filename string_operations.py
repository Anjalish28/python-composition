# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(0, 8, 3)
# print(a[x])

def main():
    S = "Hello SolarSystem"
    
    #Print length of the string S
    print(len(S))
    
    #Print the first occurence of the letter 'a' in S
    print(S.index("a"))
    #Note it is guaranteed that letter a is present in the string S
    
    #Print all the characters with even index in S
    evn_chr= [] 
    for i in range(len(S)):
        if i%2 == 0:
            evn_chr.append(S[i])
    s=""
    print(s.join(evn_chr))
    return 0

if __name__ == '__main__':
    main()