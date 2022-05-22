#1
def numb():
    print("")
    print("Numbers divided by 7 but not multiples of 5:")
    for x in range(2000,3201):
        if x%7==0 and x%5!=0:
            print(x)
numb()