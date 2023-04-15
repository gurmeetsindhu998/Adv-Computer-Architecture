from bcpu import *
#set value
mctest = f"""
#: rd_ = r1
#: pv_ = 200
{set_rd_pv_} #+ve num to r1

#: rd_ = r2
#: pv_ = 200
{set_rd_pv_} #+ve num to r2

#: rd_ = r2
#: pv_ = 2345
{setn_rd_pv_}  #-ve num to r2

#: rd_ = r2
#: pv_ = 200
{set_rd_pv_} #+ve num to r2"""


eq=f"""
Set(ans, 0)
#if  r1 == r2:
#: a_ =r1
#: b_ = r2
#: end_ = endif
{a_eq_b_}  #a==b
    Set(ans,1)
#>endif


"""

if __name__=="__main__":
    start(eq)
    Set(r1,2)
    Set(r2,2)
    printr(ans) # for a==b

    