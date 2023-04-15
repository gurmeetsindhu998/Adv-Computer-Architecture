from bcpu import *
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
printd()