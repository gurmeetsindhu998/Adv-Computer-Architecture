from bcpu import *
"""
def mul(ina:r1, inb:r2)->r3:

# where r1 and r2 could be + or -

outp:r3 = 0
"""

def mul(ina: r1, inb: r2)-> r3:
    outp:r3 = 0
    br4 = 0
    if inb <0:
        inb= -(inb)
        br4 = 1

    while inb>0:
        outp += ina
        inb -=1

    if br4==1:
        outp = -(outp)  
    return outp

mulf = """
#>mul(ina: r1, inb: r2) ->r3:
    #: ina = r1
    #: inb = r2
    #: outy = r3
    Set(outy,0)  #outy: r3 = 0

    #if inb < 0: (if inb>= 0 goto endif)
    Addi(ar,pc, ?endif1)
    Movep(pc,ar,inb)
        #inb = -inb
        Not(inb,inb)
        Addi(inb,inb,1)
        Set(r4,1)
    #>endif1

    #>while inb >0: (if inb <=0 goto endwhile)
    Addi(ar,pc,?endwhile)
    Set(cr,0)
    Sub(cr,cr,inb)
    Movep(pc,ar,cr)
        Add(outy,outy,ina)   #outy += 2
        Subi(inb,inb,1)   #inb -=1
        #jump back up to while
        Subi(pc,pc,?while)
    #>endwhile

    #if r4 =1 : (if r4 != 1 goto endif)
    Addi(ar,pc, ?endif)
    Movez(pc,ar,r4)
        #outy = -outy
        Not(outy,outy)
        Addi(outy,outy,1)
    #>endif

    #return outy
"""

if __name__ == "__main__":
    test1 = 4
    test2= -2
    op= mul(test1, test2)
    setr(r1,test1)
    setr(r2,test2)
    startfast(mulf)
    outa = getr(r3)
    print("py op: ",op)
    print("asm: ",outa) 

