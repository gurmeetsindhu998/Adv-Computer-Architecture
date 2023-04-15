from bcpu import *
#HW
"""
# r3 = r1 * r2 

# for now, where r1 and r2 are positive numbers. 

outp:r3 = 0
"""

def mul(ina: r1, inb: r2)-> r3:
    outp:r3 = 0
    while inb>0:
        outp += ina
        inb -=1
    return outp

mulf = """
#>mul(ina: r1, inb: r2) ->r3:
    #: ina = r1
    #: inb = r2
    #: outy = r3
    Set(outy,0)  #outy: r3 = 0
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
    #return outy
"""

if __name__ == "__main__":
    test1 = 3
    test2= 1
    op= mul(test1, test2)
    setr(r1,test1)
    setr(r2,test2)
    startfast(mulf)
    outa = getr(r3)
    print("py op: ",op)
    print("asm: ",outa) 