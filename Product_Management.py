import os

r = open("Product.txt", "r")
a = r.read()
lst = a.split(",")
c=""

def printProductMenu():
    # Clearing the Screen
    os.system('cls')
    print("==================================\n")
    print("Product Data Management\n")
    print("==================================\n")
    print("1. Add Product\n")
    print("2. Update Quantity\n")
    print("3. Update Price\n")
    print("4. List All Products\n")
    print("5. Exit\n")
    print("==================================\n")

def getNewProductNumber():
    newProductnumber = 0
    productFile = open("Product.txt", "r")
    for productLine in productFile.readlines():
        if (productLine.strip() != "") :
            productLineSplitted = productLine.split(",")
            currentProductNumber = int(productLineSplitted[0])
            if (newProductnumber < currentProductNumber) :
                newProductnumber = currentProductNumber
    return (newProductnumber + 1)

def DisplayProducts():
    productFile = open("Product.txt", "r")
    for productLine in productFile.readlines():
        if (productLine.strip() != "") :
            pls = productLine.split(",")
            print("%-5s %-25s %-7s %-10s" %(pls[0],pls[1],pls[2],pls[3]))

def addProduct():
    print("==================================\n")
    print("Add Product\n")
    print("==================================\n")
    productName = str(input("Enter the name of product : "))
    productPrc =str(input("Enter the price of product : "))
    productQty =str(input("Enter the quantity of product : "))
    productNumber = getNewProductNumber()
    info=str(productNumber) + "," + productName + "," + productPrc + "," + productQty+"\n"
    append=open("Product.txt","a")
    app=append.write(info)
    append.close()
    print("New Product Number will be : " + str(productNumber))
    input("Press Enter")

while True:
    printProductMenu()
    otn=int(input("Select Option : "))
    if otn==5:
        break
    if otn==1:
        addProduct()
    if otn==4:
        print("%-5s %-50s %-7s %-10s" %("ID","Name","Price","Quantity"))
        DisplayProducts()
        end=input("press enter")
#     if otn==1:
#         num=int(lst[-4])
#         num+=1
#         num1="\n"+str(num)
#         inp1=input("Enter he name of item")
#         inp2=input("Enter the price of item")
#         inp3=input("Enter the quantity")
#         lst.append(num1)
#         lst.append(inp1)
#         lst.append(inp2)
#         lst.append(inp3)
#     elif otn==2:
#         inp1=input("Enter Biscuit Name: ")
#         inp2=int(input("Enter Quantity to be added: "))
#         for i in range(len(lst)):
#          if lst[i] == inp1:
#             qty=int(lst[i+2])
#             qty+=inp2
#             lst[i+2]=str(qty)
#     elif otn==3:
#         inp1=input("Enter Biscuit Name: ")
#         inp2=int(input("Enter new price: "))
#         for i in range(len(lst)):
#             if lst[i] == inp1:
#                 qty=int(lst[i+1])
#                 qty=inp2
#                 lst[i+1]=str(qty)
#     elif otn==5:
#         break

#     for i in range(len(lst)):
#         if i==len(lst)-1:
#             c+=str(lst[i])
#         else:
#             c+=str(lst[i]+",")

# w=open("Product.txt","w")
# b=w.write(c)
# w.close()
# r.close()
