from bcpu import *
#py program
inx = 0
outy= 0
if inx == 0:
    outy =1
print(outy)

if0then = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx == 0: (if inx!=0 goto endif)
Addi(ar,pc, ?endif) #put th address of endif int ar
Movex(pc, ar ,inx) # goto endif if inx!=0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""

inx = 0
outy= 0
if inx >= 0:
    outy =1
print(outy)

ifpositive = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx >= 0: (if inx < 0 goto endif)
Addi(ar,pc, ?endif) #put th address of endif int ar
Moven(pc, ar ,inx) # goto endif if inx<0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""

inx = 0
outy= 0
if inx != 0:
    outy =1
print(outy)

ifnot0then = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx != 0: (if inx==0 goto endif)
Addi(ar,pc, ?endif) #put th address of endif int ar
Movez(pc, ar ,inx) # goto endif if inx==0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""

inx = 0
outy= 0
if inx < 0:
    outy =1
print(outy)

ifnegative = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx < 0: (if inx >= 0 goto endif)
Addi(ar,pc, ?endif) #put th address of endif int ar
Movep(pc, ar ,inx) # goto endif if inx>=0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""

#testing

#load(if0then)
#printm()
print("Running...")
setr(r1,2) #dont provide -ve number
#start(if0then)
#start(ifnot0then)
#start(ifpositive)
start(ifnegative)
printr(2)