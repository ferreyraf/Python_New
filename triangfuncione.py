def triangulorec(n):
    if n > 0:  
        for i in range(n, 0, -1):
            print(i, end=" ")
        print() 
       
        triangulorec(n - 1)

triangulorec(5)
a=" "
def ejercicio10(p):
    global a
    for i in range(p,0,-1):
    
        print(f"{a}  ")
        a=" "
        for n in range (i-1,0,-1):
           a += str(n)
ejercicio10(9)



def funcionmal(f):
        
    return f==4
print()
print(funcionmal(5))