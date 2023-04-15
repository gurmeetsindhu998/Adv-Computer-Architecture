from bcpu import*
##HW
"""
def mul(ina:r1, inb:r2)->ans:
"""

mulfmastercode = f"""
#: rd_= ans
#: ra_ = r1
#: rb_ = r2

{mul_rd_ra_rb_ }    # function in bcpu line488
"""
if __name__=="__main__":
    a = 2000
    b = 4
    setr(r1, a)
    setr(r2, b)
    startfast(mulfmastercode)
    print(getr(ans))
    print(getr(r2))
    print(getr(r1))