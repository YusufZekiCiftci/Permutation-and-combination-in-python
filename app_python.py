def factorial(f):

    intf=int(f)
    fact=intf

    while 1 < (intf):
        intf=intf-1
        fact=intf*fact
    return(fact)

def permutation(x,y):

    intx =int(x)
    inty =int(y)

    print(factorial(intx)/factorial(inty))
    return

def combination(x,y):
    
    intx =int(x)
    inty =int(y)

    print(factorial(intx)/(factorial(inty)*factorial(intx-inty)))
    
    return

processf = input("Permutation: 1 ;\nCombination: 2 ;\nWhich process do you prefer?\n") 
process=int(processf)

if  process==1:
    print("for p(a,b)")
    a = input("a:")
    b = input("b:")
    permutation(a,b)
elif process==2:
    print("for c(a,b)")
    a = input("a:")
    b = input("b:")
    combination(a,b)
else:
    print("You didn't entered the correct values!")
 
