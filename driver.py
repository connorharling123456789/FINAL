#from race import chooseCarOne
#from race import chooseCarTwo
from Car import Car
import random

def raceTimeOneKm():
    blind=input('shall your race be random?')
    #/////////////////////////////////////////MAKES CAR 1
    #car1 = Car("Tesla", "Model S", 2023, 10, 250)
    #car2 = Car("Audi", "Model S", 2023, 8, 240)
    #car1=chooseCarOne()
    #car2=chooseCarTwo()
    mak = ''
    mode = ''
    yea = ''
    acce = ''
    ts = ''
    with open("text.txt", "r") as choice:
        choices = choice.read()
        line = input(choices + '/nChoose number 0-9:')
    with open("text.txt", "r") as lst:
        l = int(line)
        g = 0
        while g < l:
            g += 1
            r = lst.readline()
        # f=lst.readlines()
        car = r
    cars = car.split()
    print(cars)
    for i in range(len(cars)):
        if cars[i] == 'Make:':
            mak = cars[i + 1]
            print(mak + 'hi')
        if cars[i] == 'Model:':
            mode = cars[i + 1]

        if cars[i] == 'Year:':
            yea = cars[i + 1]
        if cars[i] == 'Acceleration:':
            acce = cars[i + 1]
        if cars[i] == 'TopSpeed:':
            ts = cars[i + 1]
    car1 = Car(mak, mode, int(yea), float(acce), int(ts))

    make = ''
    model = 'k'
    year = ''
    acceleration = ''
    topSpeed = ''
    with open("text.txt", "r") as choice:
        choices = choice.read()
        line = input(choices + 'choose number 1-40')
    with open("text.txt", "r") as lst:
        l = int(line)
        g = 0
        while g < l:
            g += 1
            r = lst.readline()
        # f=lst.readlines()
        car = r
    cars = car.split()
    carDict = {}
    for i in range(len(cars)):
        if cars[i] == 'Make:':
            carDict['Make'] = cars[i + 1]

        if cars[i] == 'Model:':
            carDict['Model'] = cars[i + 1]

        if cars[i] == 'Year:':
            carDict['Year'] = cars[i + 1]
        if cars[i] == 'Acceleration:':
            carDict['Acceleration'] = cars[i + 1]
        if cars[i] == 'TopSpeed:':
            carDict['topSpeed'] = cars[i + 1]
    car2 = Car(carDict.get('Make'), carDict.get('Model'), int(carDict.get('Year')), float(carDict.get('Acceleration')),
                 int(carDict.get('topSpeed')))


#///////////////////////////////////////////////   MAKES CAR 2

    dcar1=0
    dcar2=0
    timecar1=0
    timecar2=0
    t1=True
    t2=True
    distance=0
    if blind=='no':
        distance=int(input('how long should the race be in kilometers'))

    else:
        distance=random.randrange(0,50)

    distance = distance * 1000
    for i in range(10000):
        if dcar1>distance and t1:
            timecar1=i
            t1=False
        if dcar2>distance and t2:
            timecar2=i
            t2=False
        if car1.speed+car1.acceleration<=car1.topSpeed:
            car1.speed+=car1.acceleration
        else:
            car1.speed=car1.topSpeed

        dcar1+=car1.speed
        if car2.speed+car2.acceleration<=car2.topSpeed:
            car2.speed+=car2.acceleration
        else:
            car2.speed=car2.topSpeed
        dcar2 += car2.speed
    if timecar1>timecar2:
        print('player 2 with the ',car2.make,car2.model,'won with a time of: ',timecar2,'seconds, which was faster than',car1.make,car1.model,'by',timecar1-timecar2,'seconds over a distance of',distance,'meters')
    else:
        print('player 1 with the ',car1.make,car1.model,'won with a time of: ',timecar1,'seconds, which was faster than',car2.make,car2.model,'by',timecar2-timecar1,'seconds over a distance of',distance,'meters')



raceTimeOneKm()

# def chooseCarOne():
#     mak=''
#     mode=''
#     yea=''
#     acce=''
#     ts=''
#     with open("text.txt", "r") as choice:
#         choices=choice.read()
#         line=input(choices+'/nChoose number 0-9:')
#     with open("text.txt","r") as lst:
#         l=int(line)
#         g=0
#         while g<l:
#             g+=1
#             r=lst.readline()
#         #f=lst.readlines()
#         car=r
#     cars = car.split()
#     print(cars)
#     for i in range(len(cars)):
#         if cars[i]=='Make:':
#             mak=cars[i+1]
#             print(mak+'hi')
#         if cars[i]=='Model:':
#             mode=cars[i+1]
#
#         if cars[i]=='Year:':
#             yea=cars[i+1]
#         if cars[i]=='Acceleration:':
#             acce=cars[i+1]
#         if cars[i]=='TopSpeed:':
#             ts=cars[i+1]
#     newCar=Car(mak,mode,yea,acce,ts)
#     #print(type(newCar))
#     newCar.display_info()
#     return newCar
#
#
#
# def chooseCarTwo():
#     make=''
#     model='k'
#     year=''
#     acceleration=''
#     topSpeed=''
#     with open("text.txt", "r") as choice:
#         choices=choice.read()
#         line=input(choices+'choose number 0-9')
#     with open("text.txt","r") as lst:
#         l=int(line)
#         g=0
#         while g<l:
#             g+=1
#             r=lst.readline()
#         #f=lst.readlines()
#         car=r
#     cars = car.split()
#     carDict={}
#     for i in range(len(cars)):
#         if cars[i]=='Make:':
#             carDict['Make']=cars[i+1]
#
#         if cars[i]=='Model:':
#             carDict['Model']=cars[i+1]
#
#         if cars[i]=='Year:':
#             carDict['Year']=cars[i+1]
#         if cars[i]=='Acceleration:':
#             carDict['Acceleration']=cars[i+1]
#         if cars[i]=='TopSpeed:':
#             carDict['topSpeed']=cars[i+1]
#     newCar=Car(carDict.get('Make'),carDict.get('Model'),carDict.get('Year'),carDict.get('Acceleration'),carDict.get('topSpeed'))
#     #print(type(newCar))
#     newCar.display_info()
#     return newCar