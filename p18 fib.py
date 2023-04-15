from bcpu import *
##HW
"""
def fib(n:r1)->ans:
    if n < 2:
        f:ans = 1
    else:
        f = fib(n-1) + fib(n-2)
    return f
"""
def fibc(n:r1)->ans:
    if n < 2:
        f:ans = 1
    else:
        f = fibc(n-1) + fibc(n-2)
    return f

def fib(n:r1)-> ans:
    a, b = 0,1
    ans= 0
    while n>=0:
        if n==1:
            ans +=1
            n -= 1
        else:
            ans = a + b
            a = b
            b = ans         
            n -= 1
    return ans 

fibf = f"""
#>fib(n:r1)-> r5:

    Set(r5,0)  #outy: r5 = 0
    Set(r3,0)
    Set(r4,1)

    #>while n>=0
    Set(r8,0)
    #: a_ = r1
    #: b_ = r8
    #: end_ = endwhile
    {a_ge_b_}  #a>=b
        #if n==1:
            Set(r9,1)
            #: a_ = r1
            #: b_ = r9
            #: end_ = endif
            {a_eq_b_}  #a==b
                Addi(r5,r5,1)
                Subi(r1,r1,1)
                #: to_ = endel
                {go_to_}
            #>endif
        #>else #else:
            #: end_ = endel
            Add(r5,r3,r4)
            Move(r3,r4)
            Move(r4,r5)
            Subi(r1,r1,1)
        #>endel
        
    #: up_ = while
    {go_up_}
#>endwhile

"""

if __name__=="__main__":
    z=15
    Set(r1,z)
    startfast(fibf)
    print(fibc(z),": choi's")
    print(fib(z),": mine")
    printr(5)