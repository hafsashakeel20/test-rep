#7
def list_dict():
    print("")
    mylist= [1234,"abcd","lmno",5678,"wxyz",9090]
    print("MAin list: ", mylist)
    mydict ={"key1":1234, "k2":"abcd", "k3": 9090, "k4": "wxyz"}
    val_list=list(mydict.values())
    print("List of dictionary values: " ,val_list)

    for i in mylist[:]:
        if i not in val_list:
            mylist.remove(i)
        else:
            continue
    print("Result list: " ,mylist)
    print("")
list_dict()