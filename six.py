#6
def even_odd():
    odd=['a','b','c','d','e']
    even=['v','w','x','y','z']
    res_list1=[]
    res_list2=[]
    main_list=[]
    print("")
    for i in range(len(odd)):
        if (i%2!=0):
            res_list1.append(odd[i])
    print("list with odd values: ", res_list1)
    res_list2=[even[j] for j in range(len(even)) if j%2==0]
    print("list with even values:", res_list2)
    main_list= res_list1 + res_list2
    print("Concatenated list:" , main_list)
even_odd()