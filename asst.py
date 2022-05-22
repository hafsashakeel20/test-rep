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

#1
def numb():
    print("")
    print("Numbers divided by 7 but not multiples of 5:")
    for x in range(2000,3201):
        if x%7==0 and x%5!=0:
            print(x)
numb()

#2
def occr():
    print("")
    sent = "The quick brown fox jumps over the lazy dog on a cool evening"
    sent_list= list(sent)
    print(sent_list)
    #VOWELS
    item_a=sent_list.count('a')
    item_e=sent_list.count('e')
    item_i=sent_list.count('i')
    item_o=sent_list.count('o')
    item_u=sent_list.count('u')
    #CONSONANTS
    item_b=sent_list.count('b')
    item_c=sent_list.count('c')
    item_d=sent_list.count('d')
    item_f=sent_list.count('f')
    item_g=sent_list.count('g')
    item_h=sent_list.count('h')
    item_j=sent_list.count('j')
    item_k=sent_list.count('k')
    item_l=sent_list.count('l')
    item_m=sent_list.count('m')
    item_n=sent_list.count('n')
    item_p=sent_list.count('p')
    item_q=sent_list.count('q')
    item_r=sent_list.count('r')
    item_s=sent_list.count('s')
    item_t=sent_list.count('t')
    item_v=sent_list.count('v')
    item_w=sent_list.count('w')
    item_x=sent_list.count('x')
    item_y=sent_list.count('y')
    item_z=sent_list.count('z')
    
    print("VOWELS:")
    print(f"[a:{item_a} e:{item_e} i:{item_i} o:{item_o} u:{item_u}]")
    print("CONSONANTS:")
    print(f"[b:{item_b} c:{item_c} d:{item_d} f:{item_f} g:{item_g} h:{item_h} j:{item_j} k{item_k} l:{item_l} m:{item_m} n:{item_n} p:{item_p} q:{item_q} r:{item_r} s:{item_s} t:{item_t} v:{item_v} w:{item_w} x:{item_x} y:{item_y} z:{item_z}]")
occr()

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

#6
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

#5
def comm_list():
    print("")
    participants_list = [
        ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
        ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
        ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
        ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
        ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
        ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
        ]
    #daily_participants= list(reduce(lambda i,j:i&j, (set(n) for n in participants_list)))
    #print("Daily participants: " ,daily_participants)

    all_participants=participants_list[0]+participants_list[1]+participants_list[2]+participants_list[3]+participants_list[4]+participants_list[5]
    
    daily_participants = [i for i in all_participants if all_participants.count(i)==len(participants_list)]
    print("Daily participants: " ,list(set(daily_participants)))

    one_time_participants = [i for i in all_participants if all_participants.count(i)<2]
    print("One time participants: " ,one_time_participants)

    first_day_participants = [i for i in all_participants if all_participants.count(i)<2 and i in participants_list[0]]
    print("first day participants: " ,first_day_participants)
comm_list()


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

#10
class Bank:
	def __init__(self,p,t,r):
		self.p = p
		self.t = t
		self.r = r

	def simple_interest(self):
		si = (self.p * self.t * self.r)/100
		print('The Simple Interest is', si)
		return si
	def compound_interest(self):
		ci = self.p * ( (1+self.r/100)**self.t - 1)
		print('The compound Interest is',ci)
		return ci
pnb = Bank(2,3,4)
icici = Bank(3,5,3)
hdfc = Bank(3,6,7)

pnb.simple_interest()
pnb.compound_interest()

icici.simple_interest()
icici.compound_interest()

hdfc.simple_interest()
hdfc.compound_interest()

#9

class A:
    def __init__(self):
        self.x= 100
    def display(self):
        print("")
        print("X(from base) = ", self.x)
    #def display(self, z):
    #    print("X(from base) = ", self.x)
    #    print("Z value overloaded = ", z)

class B(A):
    def __init__(self):
        self.y=50
        A.__init__(self)
    def display(self):
        print("X(from derived) = ", self.x)
        print("Y(from derived) = ",self.y)
        print("Overiding achieved!")
    def dets(self):
        print("X and Y values are printed!")

objt3=A()
objt2=B()
print(objt2.x)
print(objt2.y)
#print(objt3.display(20))
print(objt3.display())
print(objt2.display())
print(objt2.dets())

#8  
import json
def json_prog():
   sampleJson ="""{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
            }
         }
      }
   }"""

   data=json.loads(sampleJson)

   print(data["company"]["employee"]["payble"]["salary"])
json_prog()
