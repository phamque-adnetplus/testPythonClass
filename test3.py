def func():
    s = input("Input a string: ")
    s = int(s)
    d=l=0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass
    print("Letters", l)
    print("Digits", d)

if __name__ == "__main__":
    func();