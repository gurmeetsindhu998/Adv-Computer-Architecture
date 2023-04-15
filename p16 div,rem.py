from bcpu import*
"""
def div(ina:r1, inb:r2)->(ans, res):

    # where r1 and r2 are positive numbers

    # ans = r1 // r2

    # res = r1 % r2
"""

def div(ina:r1, inb:r2)->(ans, res):

    # where r1 and r2 are positive numbers
    ans = 0
    res= 0
    if(inb !=0):
        while ina >= 0:
            ans += 1
            ina -= inb
        res += ina
        res += inb
        ans -=1
    return ans,res

divf="""

    #: ina = r1
    #: inb = r2
    #: ans = r3
    #: res = r4

    #if inb != 0: (if inb = 0 goto endif)
    Addi(ar,pc, ?endif)
    Movez(pc,ar,inb)
    
    #>while1 ina >=inb: (if inb < 0 goto endwhile)
    Addi(ar,pc,?endwhile)
    Moven(pc,ar,ina)
        Addi(ans, ans,1)   #ans += 1
        Sub(ina,ina,inb)   #ina -= inb
        #jump back up to while
        Subi(pc,pc,?while1)
    #>endwhile

    Add(res,res,ina)    #res += ina
    Subi(ans,ans,1)     #ans -=1
    Add(res,res,inb)    #res += inb

    #>endif
    #return outy
"""
def divclass(ina:r1, inb:r2)->(ans, res):

    # where r1 and r2 are positive numbers
    ans = 0
    res= 0
    if inb!= 0:
        res = ina
        while res >= inb:
            res -= inb
            ans += 1
    return ans, res

divfclass= """
#> divclass(ina:r1, inb:r2)->(ans, res):
    #: ina = r1
    #: inb = r2
    #: intp = ans
    #: rem = res
    Set(intp,0)
    Set(rem,0)
    #if inb!= 0: (if inb == 0 goto endif)
    Addi(ar,pc,?endif)
    Movez(pc,ar,inb)
        #do div
        Move(rem,ina)
        #>while rem >= inb: (if rem < inb goto endwhile)
        Addi(ar,pc,?endwhile)
        Sub(cr,rem,inb)
        Moven(pc,ar,cr)
            Sub(rem ,rem, inb)
            Addi(intp,intp,1)
            #go back up to while
            Subi(pc,pc,?while)
    #>endwhile
    #>endif

"""


divfmastercode = f"""
Move(r3,r1)# due to r1 is used within div_
#: qu_= ans
#: re_ = res
#: nu_ = r3
#: de_ = r2

{div_qu_re_nu_de_} # function in bcpu line488
"""

if __name__ == "__main__":
    test1 = 2000
    test2= 1
    
    op= div(test1, test2)
    op2= divclass(test1, test2)
    setr(r1,test1)
    setr(r2,test2)
    startfast(divfmastercode)
    outa = getr(ans)
    outa2 = getr(res)

    print("py op: ",op,op2)
    print("asm: ",outa, outa2) 
