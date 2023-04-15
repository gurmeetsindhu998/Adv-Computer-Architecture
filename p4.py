from bcpu import *
#check change in bits or number
Set(r1,0b1100_0111)
Seth(r1, 0b1100_1111)
printrb(1)

Set(r9, 0b0100_0000)
print("and")
And(r10,r1,r9)
Set(r9,0b0010_0000)
And(r10,r1,r9)

printrb()