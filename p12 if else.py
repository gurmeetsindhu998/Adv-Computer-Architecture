from bcpu import *
# HW 
def Abs (inx:r1) -> r2: # get the absolute value
    outy:r2 = inx
    if inx < 0:
        outy = -inx
    else:
        outy = inx
    return outy # amsembly will get the return value from r2
absf2 = """
#> Abs (inx:r1) -> r2: # get the absolute value
    #: inx = r1
    #: outy = r2
    #if inx < 0: (if inx >= 0 goto else)
    Addi(ar,pc,?else)
    Movep (pc, ar, inx)
        #outy = -inx
        Not (outy, inx)
        Addi (outy, outy, 1)
        Addi (pc,pc,?endif)

    # store the address of else in ar
    # if inx is >= 0 go to else otherwise execute the code below
    # negate inx and put it in outy.
    # Add 1 to outy so that linx| == loutyl
    # store the address of endif in pc; unconditional jump
    #>else  #else:     # execute this part of the code if inx >=0
    #outy = inx
    Move(outy, inx) # Move inx to outy
    #>endif
   
    
    #return outy # ansembly will get the return value from r2
"""

if __name__ == "__main__":
    test = -1
    op= Abs(test)
    setr(r1,test)
    start(absf2)
    outa = getr(r2)
    print("py op: ",op)
    print("asm: ",outa) 