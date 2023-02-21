n=int(input('enter the no. f cars: '))
truck=10
w4=10
w2=10
for i in range(n):
    car=input("enter car type")
    try:
        if car =="Truck":
            if truck!=0:
                truck-=1
                print('park in truck section.')
            else:
                print('No parking available.')
        elif car == "4 wheeler":
            if w4 != 0:
                w4 -= 1
                print('park in 4 wheeler section.')
            elif truck!=0:
                truck-=1
                print('park in truck section.')
            else:
                print('No parking available.')
        elif car == "2 wheeler":
            if w2 != 0:
                w2 -= 1
                print('park in 2 wheeler section.')
            elif w4!=0:
                w4-=1
                print('park in 4 wheeler section.')
            elif truck != 0:
                truck -= 1
                print('park in truck section.')
            else:
                print('No parking available.')
        else:
            print('No parking available.')
    except:
        print("server crashed")

print("Thank You")