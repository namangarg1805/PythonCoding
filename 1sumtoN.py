# Hello Everyone in this we will be covering:
#     1.What is Algorithm
#     2.How to sum numbers till N
#     3.Inbuilt timeit method of python
    
# A1.Algorithm is basically a procedure or formulae to solve a particular problem

# A2.We have to build a function that sums up all numbers till N(given NUmber)

# A3.With timeit method you can have the time taken by the function to run

def sum1(n):
    sums=0
    for i in range(1,n+1):
        sums=sums+i
    return sums

def sum2(n):
    return (n*(n+1))/2

%timeit -n10 sum1(10)
%timeit -n10 sum2(10)

#So sum2 function is faster than sum1
#Note:This also depends on the harware of the system so this method can't be choosen to 
#calculate complexity or efficiency of algorithm thus we use method another called Big-O Notation.


