from bcpu import *

def whileloop(inx: r1) -> r2:
    outy: r2 = 0
    while inx >=0:
        outy += 2
        inx -=1
    return outy


whileloopf=""" 
#>whileloop(inx: r1) -> r2:
    #: inx = r1
    #: outy = r2
    Set(outy,0)  #outy: r2 = 0
    #>while inx >=0: (if inx < 0 goto endwhile)
    Addi(ar,pc,?endwhile)
    Moven(pc,ar,inx)
        Addi(outy,outy,2)   #outy += 2
        Subi(inx,inx,1)   #inx -=1
        #jump back up to while
        Subi(pc,pc,?while)
    #>endwhile
    #return outy
"""

if __name__ == "__main__":
    test = 1
    op= whileloop(test)
    setr(r1,test)
    start(whileloopf)
    outa = getr(r2)
    print("py op: ",op)
    print("asm: ",outa) 