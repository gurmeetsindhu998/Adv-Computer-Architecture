from bcpu import *
Set(r1,11)   # r1=11 where r1 is the address(label) and 11 is the value
print(r1)
Move(r3,r1)   # r3= r1 copy
print(r3,r1)
Add(r4,r1,r1)  #r4 = r1+r1   all variables
Addi(r5,r1,5)  #r5 = r1+5   one val in instructiions
#Addi(r5,r1,66) error   
"""
because we have 16 bits in size and addi is 4 bit , r5 and r1 is another 8 bit so we are 
left with 4 bit which means(0-15) numbers and 15 is used for pc(program counter) 
"""
Set(r6,234)  #addi is 4 bit , r6 is 4 bit and remaning 8 bit (0-255)

#set r7= 777
Set(r7, 777%256)
Seth(r7,777//256)
# 777//256 = 3 and 777%256 = 9    3*256+9 = 777


#set r8 = -888
Set(r8, 888%256)
Seth(r8,888//256)
Not(r8,r8)  #-889 888 
Addi(r8,r8,1) #-888 -889 1

printr() # to print all 16 bit
printrb() # to print all 16 bit in binary