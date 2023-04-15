from bcpu import *
#HW

#less, large: Moven
#lessequal, largeequal: Movep
"""
r1 == 11

r1 != 11

r1 > 11

r1 < 11

r1 >= 11

r1 <= 11
"""
inx = 0
outy= 0
if inx == 11:
    outy =1
print(outy)

ifequal11then = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx == 11: (if inx!=0 goto endif)
Subi(inx,inx,11)
Addi(ar,pc, ?endif) #put th address of endif int ar
Movex(pc, ar ,inx) # goto endif if inx!=0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""

inx = 0
outy= 0
if inx != 11:
    outy =1
print(outy)

ifnotequal11then = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx != 11: (if inx=11 goto endif)
Subi(inx,inx,11)
Addi(ar,pc, ?endif) #put th address of endif int ar
Movez(pc, ar ,inx) # goto endif if inx=0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""
inx = 0
outy= 0
if inx > 11:
    outy =1
print(outy)

ifless11 = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx >11: (if inx >= 11 goto endif)
Subi(cr,inx,11)
Addi(ar,pc, ?endif) #put th address of endif int ar
Movep(pc, ar ,cr) # goto endif if inx<0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""
inx = 0
outy= 0
if inx >= 11:
    outy =1
print(outy)

iflessequal11 = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx <=11: (if inx > 11 goto endif)
Set(cr,11)
Sub(cr,cr,inx)
Addi(ar,pc, ?endif) #put th address of endif int ar
Moven(pc, ar ,cr) # goto endif if inx<0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""
inx = 0
outy= 0
if inx < 11:
    outy =1
print(outy)

ifgreat11 = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx >11: (if inx < 0 goto endif)
Subi(inx,inx,12)
Addi(ar,pc, ?endif) #put th address of endif int ar
Moven(pc, ar ,inx) # goto endif if inx>0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""

inx = 0
outy= 0
if inx >= 11:
    outy =1
print(outy)

ifgreatequal11 = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx >=11: (if inx < 11 goto endif)
Subi(cr,inx,11)
Addi(ar,pc, ?endif) #put th address of endif int ar
Moven(pc, ar ,cr) 
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""

Choigreat11 = """
#: inx = r1
#: outy = r2

Set(outy, 0) #outy= 0
#if inx >11: (if inx < 11 goto endif)
Set(cr,11)
Sub(cr,cr,inx)
Addi(ar,pc, ?endif) #put th address of endif int ar
Movep(pc, ar ,cr) # goto endif if inx>0
    Set(outy,1) #outy =1
#> endif # defining a label      # ">" = arrow(go to)
Move(outy,outy) #print(outy)

"""

#testing

#load(if0then)
#printm()
print("Running...")
setr(r1,12) #dont provide -ve number
#start(ifequal11then)
#start(ifnotequal11then)
#start(ifless11)
start(iflessequal11)
#start(ifgreat11)
#start(ifgreatequal11)
#start(Choigreat11)
printr(2)

