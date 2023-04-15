from bcpu import *

def Abs(inx:r1) -> r2:
    outy:r2 = inx
    if inx < 0:
        outy = -inx
    return outy 

absf="""
#> Abs(inx:r1) -> r2:
    #: inx = r1
    #: outy = r2
    Move(outy,inx)  #outy:r2 = inx
    #if inx < 0: (if inx>= 0 goto endif)
    Addi(ar,pc, ?endif)
    Movep(pc,ar,inx)
        #outy = -inx
        Not(outy,inx)
        Addi(outy,outy,1)
    #>endif
    #return outy 
 
"""

# testing

if __name__ == "__main__":
    test = -5
    op= Abs(test)
    setr(r1,test)
    start(absf)
    outa = getr(r2)
    print("py op: ",op)
    print("asm: ",outa)
    