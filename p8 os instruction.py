from bcpu import *
clearbit = """
#inr  = input register
#: inr = r1 # declare var inr = r1
#: mask  = r9 #using r9 as mask
#: bitlow = 0
#: bithigh = ob1111_1010
# r1 = 0b1100_1111_1100_0111

Set(inr, 0b1100_0111)

Seth(inr, 0b1100_1111)

# put your code here 

# clear r1 bit 8 and bit 10 to 0

# os instruction
Set(mask,bitlow) 
Seth(mask,bithigh) 

And(inr,inr,mask)"""


# os instruction
# r1 = 0b1100_1111_1100_0111
setr(r1, 0b1100_1111_1100_0111)

start(clearbit)
printrb(1)
