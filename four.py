#4
def rev_list():
    print("")
    mylist=['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ]
    print("Reverse list using negative index:", end="")
    print(mylist[::-1])
rev_list()

def rev_for_list():
    mylist=['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ]
    my_l=len(mylist)
    revlist=[]
    for i in range(my_l-1,-1,-1):
        revlist.append(mylist[i])
    print("Reverse list using for loop: ", end="")
    print(revlist)
rev_for_list()