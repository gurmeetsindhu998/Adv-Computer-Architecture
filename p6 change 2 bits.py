from bcpu import *
#HW

# r1 = 0b1100_1111_1100_0111

Set(r1, 0b1100_0111)

Seth(r1, 0b1100_1111)

# put your code here 

# clear r1 bit 8 and bit 10 to 0

# os instruction
Set(r8,0) 
Seth(r8,0b0000_0101) 
Not(r8,r8)
And(r1,r1,r8)
printrb()
printrb(1)

