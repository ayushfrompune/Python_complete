code1=open("txt1.txt","r")
code5=open("txt2.txt","r")
code3=open("txt3.txt","r")
code4=open("txt4.txt","r")
#info=int(input("Press 1 for Name\n"
#           "Press 2 for Age\n"
#           "Press 3 for Hobbies\n"
#           "Press 4 for Family Background\n"
#           "Press 5 for all information\n"
#           "Enter the data no. you want to know: "))

#if info==1:
#    print(code1.read())
#elif info==2:
#    print(code5.read())
#elif info==3:
#   print(code3.read())
#elif info==4:
#    print(code4.read())
#else:
#    print(code1.read())
#    print(code5.read())
#    print(code3.read())
#    print(code4.read())


inp1=code1.read()
inp2=code5.read()
inp3=code3.read()
inp4=code4.read()

lst1=[]
lst2=[]
lst3=[]
lst4=[]
lst1.append(inp1)
lst2.append(inp2)
print(lst2)
lst3.append(inp3)
lst4.append(inp4)
for i in range(len(lst1)):
    def Convert(lst1,lst2,lst3,lst4):
        dict1={(i+1):lst1[i],(i+2):lst2[i],(i+3):lst3[i],(i+4):lst4[i]}
        return dict1
print(Convert(lst1,lst2,lst3,lst4))
