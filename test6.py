def func():
    start = 10000
    end = 99999
    
    for i in range(start,end): 
        for j in range(2,i): 
            if(i % j==0): 
                break
        else: 
            print(i) 
            
if __name__ == "__main__":
    func();