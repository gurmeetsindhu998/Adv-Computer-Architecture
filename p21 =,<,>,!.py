from bcpu import *
#all operators
"""
a_eq_b_
a_ne_b_ 
a_lt_b_ 
a_gt_b_
a_le_b_ 
a_ge_b_

"""
Set(r1,5)
Set(r2,6)
aeqb=f"""

Set(ans, 0)
#if  r1 == r2:
#: a_ =r1
#: b_ = r2
#: end_ = endif
{a_eq_b_}  #a==b
    Set(ans,1)
#>endif
"""
start(aeqb)
print("a==b")
printr(ans)

aneb= f"""
Set(ans, 0)
#if  r1 == r2:
#: a_ =r1
#: b_ = r2
#: end_ = endif
{a_ne_b_}  #a==b
    Set(ans,1)
#>endif
"""
start(aneb)
print("a!=b")
printr(ans)

aneb= f"""
Set(ans, 0)
#if  r1 == r2:
#: a_ =r1
#: b_ = r2
#: end_ = endif
{a_ne_b_}  #a==b
    Set(ans,1)
#>endif
"""
start(aneb)
print("a!=b")
printr(ans)


