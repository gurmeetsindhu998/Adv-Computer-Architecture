from bcpu import *
# using while
mctest = f"""
#: rd_ = r1
#: pv_ = 0
{set_rd_pv_} #+ve num to r1

#: rd_ = r2
#: pv_ = 10
{set_rd_pv_} #+ve num to r2
Set(ans,0)

#>while r1<r2:
#: a_ = r1
#: b_ = r2
#: end_ = endwhile
{a_lt_b_}  #a<b
    Add(ans,ans,r1)    # 0+1+2+...+9
    Addi(r1,r1,1)
    #: up_ = while
    {go_up_}
#>endwhile

"""



if __name__=="__main__":
    start(mctest)
    printr(1)
    printr(2)
    printr(ans) 
