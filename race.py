from Car import Car

def chooseCarOne():
    mak=''
    mode=''
    yea=''
    acce=''
    ts=''
    with open("text.txt", "r") as choice:
        choices=choice.read()
        line=input(choices)
    with open("text.txt","r") as lst:
        l=int(line)
        g=0
        while g<l:
            g+=1
            r=lst.readline()
        #f=lst.readlines()
        car=r
    cars = car.split()
    print(cars)
    for i in range(len(cars)):
        if cars[i]=='Make:':
            mak=cars[i+1]
            print(mak+'hi')
        if cars[i]=='Model:':
            mode=cars[i+1]

        if cars[i]=='Year:':
            yea=cars[i+1]
        if cars[i]=='Acceleration:':
            acce=cars[i+1]
        if cars[i]=='TopSpeed:':
            ts=cars[i+1]
    newCar=Car(mak,mode,yea,acce,ts)
    #print(type(newCar))
    newCar.display_info()
    return newCar

chooseCarOne()
