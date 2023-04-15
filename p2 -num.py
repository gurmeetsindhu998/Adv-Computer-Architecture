from bcpu import *

#HW insert -12345 into r3
Set(r3, 12345%256)
Seth(r3,12345//256)
Not(r3,r3)  
Addi(r3,r3,1) 


printr(3) # for printing the value at r3
printrb(3) # to print value at r3 in binary


#class

#r2 = -12345 in binary

Set(r2,0b1100_0111)
Seth(r2, 0b1100_1111)
printrb()


#mask  to change a specfic bit
Set(r9,0)
Seth(r9, 0b0001_0000)
printrb()
And(r2,r2,r9)