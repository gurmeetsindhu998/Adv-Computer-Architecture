from bcpu import *

Set(r1,111)
ar #address register
cr # condition register

Set(ar,100)  # 100 is the address
Store(ar,r1) 
printd()
printd(100)

Load(r2,ar)
printr()

# total 256 bits to play
# first 100 for stack
# others for array 


#array
Set(r10,100)  #base for array 
Set(r11,0) #index of the array
Add(ar, r10,r11)
Load(r3,ar)
printr()
Set(r1,123)
Set(r11,1)
Add(ar,r10,r11)
Store(ar,r1)


#stack
st # stack top (r14 in bits ) #r14 tells number of elements in stack
#push 66 instack
Addi(st,st,1) #get new top space for push
Set(cr,66)
Store(st,cr)
printd()


Set(cr,77)
Addi(st,st,1)
Store(st,cr)
printd()

#pop 
Load(r3,st) #get top of stack and put in the r3
Subi(st,st,1)
printr()