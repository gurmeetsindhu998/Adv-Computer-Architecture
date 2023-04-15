from bcpu import *

#mask  to change a specfic bit
Set(r1,0b1100_0111)
Seth(r1, 0b1100_1111)
printrb(1)
Set(r9,0b0001_0000)  #for changing 4th bit from the right

printrb()
Or(r1,r1,r9)  # or operation to add 0 instaed of 1
printrb(1)

"""
for changing 1 to 0 we use And operation: "use brain to change numbers" 

"""

Set(r8,0b0000_0010) #for changing 2nd bit from 1 to zero
Not(r8,r8)
And(r1,r1,r8)
printrb(1)