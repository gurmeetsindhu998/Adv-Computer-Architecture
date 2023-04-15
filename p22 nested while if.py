from bcpu import *
# using while

mctest = f"""
#: rd_ = r1
#: pv_ = 8
{set_rd_pv_} #+ve num to r1

#: rd_ = r2
#: pv_ = 10
{set_rd_pv_} #+ve num to r2
Set(ans,0)

    #: ina = r1
    #: inb = r2
    #: outy = ans
    Set(outy,0)  #outy: ans = 0
    Set(r3,0)
    Set(r4,1)

    #>while ina>=4
    Set(r9,4)
    #: a_ = ina   #r1=10
    #: b_ = r9
    #: end_ = endwhile
    {a_ge_b_}  #a>=b
        #if ina==inb:  #10==10
            #: a_ = ina
            #: b_ = inb
            #: end_ = endif
            {a_eq_b_}  #a==b
                Set(outy,1)
                Set(ina,3)
                #break
                #: to_ = endwhile
                {go_to_}
            #>endif
        #else:
            #: end_ = endel
            Set(ina,2)
            #>endel
        
            
    #: up_ = while
    {go_up_}
#>endwhile


"""



if __name__=="__main__":
    start(mctest)
    printr(1)
    printr(2)
    printr(ans)
    a= 10
    b= 10
    while a >=4:
        if a==b:
            print("if")
            a= 0
        else:
            print("else")
            a = 2
