def func():
    s = input("Input a upper limit of Fibonacci series: ")
    x,y=0,1

    while y<50:
        print(y)
        x,y = y,x+y

if __name__ == "__main__":
    func();