#3
def binar(x):
    if x>1:
        binar(x//2)
    print(x%2, end='')
print("The binary value of 12 is :")    
binar(12)

def deci():
    bval="1100"
    num_bin=list(bval)
    dec_val=0

    for i in range(len(num_bin)):
        sel_val=num_bin.pop()
        if sel_val=='1':
            dec_val+=pow(2,i)
    print("")
    print(f"decimal value of {bval} is :", dec_val)
deci()