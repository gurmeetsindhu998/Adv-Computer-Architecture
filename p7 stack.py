from bcpu import *
#HW
"""
Stack
Push 11
push 22
push 33
push 44
pop into r1
pop into r2
"""
#push
Addi(st,st,1) 
Set(cr,11)
Store(st,cr)

Addi(st,st,1) 
Set(cr,22)
Store(st,cr)

Addi(st,st,1) 
Set(cr,33)
Store(st,cr)

Addi(st,st,1) 
Set(cr,44)
Store(st,cr)
printd()


#pop 
Load(r1,st) #get top of stack and put in the r1
Subi(st,st,1)

Load(r2,st) #get top of stack and put in the r2
Subi(st,st,1)
printr()