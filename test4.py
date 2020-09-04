def func():
    s = input("Input a upper limit of Fibonacci series: ")
    s = int(s)
    x,y=0,1

    while y<s:
        print(y)
        x,y = y,x+y

if __name__ == "__main__":
    func();