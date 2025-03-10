# from Car import Car
# 7 vs 3 4.6 km

#from race import chooseCarOne
#from race import chooseCarTwo
from Car import Car
import random
from race import sim

import matplotlib.pyplot as plt
#This function runs the race. It doesn't take any parameters and returns true when it reaches
# the end of the code after it shows the graphs for speed and position
def raceTimeOneKm():
    blind= input ('Shall your race be random?')
    #//////////////////////////////////////////////////////////////MAKES CAR 1
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
        line = input(choices + '/nChoose number 1-39:')
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
#////////////////////////////////////////////////////////////MAKES CAR 2
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




    dcar1=0
    dcar2=0
    timecar1=0
    timecar2=0
    t1=True
    t2=True
    distance=0
    if blind=='no':
        distance=int(input('How long should the race be in kilometers 0-25Km'))

    else:
        distance=random.randrange(0,50)

    distance = distance * 1000
    num_steps=50

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


    w=0
    if timecar1>timecar2:
        print('Player 2 with the ',car2.make,car2.model,'won with a time of: ',timecar2,'seconds, which was faster than',car1.make,car1.model,'by',timecar1-timecar2,'seconds over a distance of',distance,'meters')

    else:

        print('Player 1 with the ',car1.make,car1.model,'won with a time of: ',timecar1,'seconds, which was faster than',car2.make,car2.model,'by',timecar2-timecar1,'seconds over a distance of',distance,'meters')

    sim(car1, car2, distance, 0, 0)
    if timecar1 > timecar2:
        return True
    else:
        return True


    # Create a plot to visualize the race

    # plt.figure(figsize=(10, 6))
    # plt.plot(range(num_steps), dcar1, label=(car1.make,car1.model), color='blue', lw=2)
    # plt.plot(range(num_steps), dcar2, label=(car1.make,car1.model), color='red', lw=2)
    # plt.xlabel('Time Step')
    # plt.ylabel('Position')
    # plt.title('Race Simulation: Car 1 vs Car 2')
    # plt.legend()
    # plt.grid(True)
    # plt.show()


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
# #from race import chooseCarOne
# #from race import chooseCarTwo
# from Car import Car
# import random
#
# def raceTimeOneKm():
#     blind=input('shall your race be random?')
#     #/////////////////////////////////////////MAKES CAR 1
#     #car1 = Car("Tesla", "Model S", 2023, 10, 250)
#     #car2 = Car("Audi", "Model S", 2023, 8, 240)
#     #car1=chooseCarOne()
#     #car2=chooseCarTwo()
#     mak = ''
#     mode = ''
#     yea = ''
#     acce = ''
#     ts = ''
#     with open("text.txt", "r") as choice:
#         choices = choice.read()
#         line = input(choices + '/nChoose number 0-9:')
#     with open("text.txt", "r") as lst:
#         l = int(line)
#         g = 0
#         while g < l:
#             g += 1
#             r = lst.readline()
#         # f=lst.readlines()
#         car = r
#     cars = car.split()
#     print(cars)
#     for i in range(len(cars)):
#         if cars[i] == 'Make:':
#             mak = cars[i + 1]
#             print(mak + 'hi')
#         if cars[i] == 'Model:':
#             mode = cars[i + 1]
#
#         if cars[i] == 'Year:':
#             yea = cars[i + 1]
#         if cars[i] == 'Acceleration:':
#             acce = cars[i + 1]
#         if cars[i] == 'TopSpeed:':
#             ts = cars[i + 1]
#     car1 = Car(mak, mode, int(yea), float(acce), int(ts))
#
#     make = ''
#     model = 'k'
#     year = ''
#     acceleration = ''
#     topSpeed = ''
#     with open("text.txt", "r") as choice:
#         choices = choice.read()
#         line = input(choices + 'choose number 1-40')
#     with open("text.txt", "r") as lst:
#         l = int(line)
#         g = 0
#         while g < l:
#             g += 1
#             r = lst.readline()
#         # f=lst.readlines()
#         car = r
#     cars = car.split()
#     carDict = {}
#     for i in range(len(cars)):
#         if cars[i] == 'Make:':
#             carDict['Make'] = cars[i + 1]
#
#         if cars[i] == 'Model:':
#             carDict['Model'] = cars[i + 1]
#
#         if cars[i] == 'Year:':
#             carDict['Year'] = cars[i + 1]
#         if cars[i] == 'Acceleration:':
#             carDict['Acceleration'] = cars[i + 1]
#         if cars[i] == 'TopSpeed:':
#             carDict['topSpeed'] = cars[i + 1]
#     car2 = Car(carDict.get('Make'), carDict.get('Model'), int(carDict.get('Year')), float(carDict.get('Acceleration')),
#                  int(carDict.get('topSpeed')))
#
#
# #///////////////////////////////////////////////   MAKES CAR 2
#
#     dcar1=0
#     dcar2=0
#     timecar1=0
#     timecar2=0
#     t1=True
#     t2=True
#     distance=0
#     if blind=='no':
#         distance=int(input('how long should the race be in kilometers'))
#
#     else:
#         distance=random.randrange(0,50)
#
#     distance = distance * 1000
#     for i in range(10000):
#         if dcar1>distance and t1:
#             timecar1=i
#             t1=False
#         if dcar2>distance and t2:
#             timecar2=i
#             t2=False
#         if car1.speed+car1.acceleration<=car1.topSpeed:
#             car1.speed+=car1.acceleration
#         else:
#             car1.speed=car1.topSpeed
#
#         dcar1+=car1.speed
#         if car2.speed+car2.acceleration<=car2.topSpeed:
#             car2.speed+=car2.acceleration
#         else:
#             car2.speed=car2.topSpeed
#         dcar2 += car2.speed
#     if timecar1>timecar2:
#         print('player 2 with the ',car2.make,car2.model,'won with a time of: ',timecar2,'seconds, which was faster than',car1.make,car1.model,'by',timecar1-timecar2,'seconds over a distance of',distance,'meters')
#     else:
#         print('player 1 with the ',car1.make,car1.model,'won with a time of: ',timecar1,'seconds, which was faster than',car2.make,car2.model,'by',timecar2-timecar1,'seconds over a distance of',distance,'meters')
#
#
#
# raceTimeOneKm()
#
# # def chooseCarOne():
# #     mak=''
# #     mode=''
# #     yea=''
# #     acce=''
# #     ts=''
# #     with open("text.txt", "r") as choice:
# #         choices=choice.read()
# #         line=input(choices+'/nChoose number 0-9:')
# #     with open("text.txt","r") as lst:
# #         l=int(line)
# #         g=0
# #         while g<l:
# #             g+=1
# #             r=lst.readline()
# #         #f=lst.readlines()
# #         car=r
# #     cars = car.split()
# #     print(cars)
# #     for i in range(len(cars)):
# #         if cars[i]=='Make:':
# #             mak=cars[i+1]
# #             print(mak+'hi')
# #         if cars[i]=='Model:':
# #             mode=cars[i+1]
# #
# #         if cars[i]=='Year:':
# #             yea=cars[i+1]
# #         if cars[i]=='Acceleration:':
# #             acce=cars[i+1]
# #         if cars[i]=='TopSpeed:':
# #             ts=cars[i+1]
# #     newCar=Car(mak,mode,yea,acce,ts)
# #     #print(type(newCar))
# #     newCar.display_info()
# #     return newCar
# #
# #
# #
# # def chooseCarTwo():
# #     make=''
# #     model='k'
# #     year=''
# #     acceleration=''
# #     topSpeed=''
# #     with open("text.txt", "r") as choice:
# #         choices=choice.read()
# #         line=input(choices+'choose number 0-9')
# #     with open("text.txt","r") as lst:
# #         l=int(line)
# #         g=0
# #         while g<l:
# #             g+=1
# #             r=lst.readline()
# #         #f=lst.readlines()
# #         car=r
# #     cars = car.split()
# #     carDict={}
# #     for i in range(len(cars)):
# #         if cars[i]=='Make:':
# #             carDict['Make']=cars[i+1]
# #
# #         if cars[i]=='Model:':
# #             carDict['Model']=cars[i+1]
# #
# #         if cars[i]=='Year:':
# #             carDict['Year']=cars[i+1]
# #         if cars[i]=='Acceleration:':
# #             carDict['Acceleration']=cars[i+1]
# #         if cars[i]=='TopSpeed:':
# #             carDict['topSpeed']=cars[i+1]
# #     newCar=Car(carDict.get('Make'),carDict.get('Model'),carDict.get('Year'),carDict.get('Acceleration'),carDict.get('topSpeed'))
# #     #print(type(newCar))
# #     newCar.display_info()
# #     return newCar
# import random
#
# import matplotlib.pyplot as plt
# def sim(car1,car2,distance,dcar1,dcar2):
#     car1.speed=0
#     car2.speed=0
#     num_steps = 50
#     t1 = True
#     t2 = True
#     timecar1 = 0
#     timecar2 = 0
#     # Lists to track the positions of the cars over time
#     car1_positions = []
#     car2_positions = []
#     car1_speed = []
#     car2_speed = []
#     d1=0
#     d2=0
#     dcarone=0
#     dcartwo=0
#     # Simulate the race
#     #for step in range(num_steps):
#     for i in range(1000):
#         if not t1 and not t2:
#             break
#         p=i
#         d1=dcar1
#         d2=dcar2
#         if dcar1 > distance and t1:
#             timecar1 = i
#             t1 = False
#         if dcar2 > distance and t2:
#             timecar2 = i
#             t2 = False
#         if car1.speed + car1.acceleration <= car1.topSpeed:
#             car1.speed += car1.acceleration
#             dcar1 += car1.speed
#             dcarone = dcar1 - d1
#             car1_speed.append(dcar1)
#             car1_positions.append(dcar1 - d1)
#         else:
#             car1.speed = car1.topSpeed
#             dcar1 += car1.speed
#
#             car1_speed.append(dcar1)
#             car1_positions.append(dcar1 - d1)
#
#         if car2.speed + car2.acceleration <= car2.topSpeed:
#             car2.speed += car2.acceleration
#             dcar2 += car2.speed
#
#             dcartwo = dcar2 - d2
#             car2_speed.append(dcar2)
#             car2_positions.append(dcar2 - d2)
#         else:
#             car2.speed = car2.topSpeed
#             dcar2 += car2.speed
#
#             car2_speed.append(dcar2)
#             car2_positions.append(dcar2-d2)
#
#
#
#
#
#
#     if timecar1>timecar2:
#         p=timecar1+1
#     else:
#         p=timecar2+1
#     # Create a plot to visualize the race
#
#     d=input('speed graph or position graph? type p for position and s for speed')
#     if d=='p':
#         plt.figure(figsize=(10, 6))
#         plt.plot(range(p), car1_speed, label=(car1.make,car1.model,'speed'), color='blue', lw=2)
#         plt.plot(range(p), car2_speed, label=(car2.make,car2.model,'speed'), color='red', lw=2)
#
#         plt.xlabel('Time Step')
#         plt.ylabel('Position')
#         plt.title('Race Simulation: Car 1 vs Car 2')
#         plt.legend()
#         plt.grid(True)
#         plt.show()
#     elif d=='both':
#         plt.figure(figsize=(10, 6))
#         plt.plot(range(p), car1_speed, label=(car1.make, car1.model, 'speed'), color='blue', lw=2)
#         plt.plot(range(p), car2_speed, label=(car2.make, car2.model, 'speed'), color='red', lw=2)
#         plt.xlabel('Time Step')
#         plt.ylabel('Speed')
#         plt.title('Race Simulation: Car 1 vs Car 2')
#         plt.legend()
#         plt.grid(True)
#         plt.show()
#
#         plt.figure(figsize=(10, 6))
#         plt.plot(range(p), car1_positions, label=(car1.make, car1.model, 'position'), color='blue', lw=2)
#         plt.plot(range(p), car2_positions, label=(car2.make, car2.model, 'position'), color='red', lw=2)
#         plt.xlabel('Time Step')
#         plt.ylabel('Position')
#         plt.title('Race Simulation: Car 1 vs Car 2')
#         plt.legend()
#         plt.grid(True)
#         plt.show()
#     else:
#         plt.figure(figsize=(10, 6))
#         plt.plot(range(p), car1_positions, label=(car1.make, car1.model, 'position'), color='blue', lw=2)
#         plt.plot(range(p), car2_positions, label=(car2.make, car2.model, 'position'), color='red', lw=2)
#         plt.xlabel('Time Step')
#         plt.ylabel('Speed')
#         plt.title('Race Simulation: Car 1 vs Car 2')
#         plt.legend()
#         plt.grid(True)
#         plt.show()
# #
# #
# # def chooseCarOne():
# #     mak=''
# #     mode=''
# #     yea=''
# #     acce=''
# #     ts=''
# #     with open("text.txt", "r") as choice:
# #         choices=choice.read()
# #         line=input(choices+'/nChoose number 0-9:')
# #     with open("text.txt","r") as lst:
# #         l=int(line)
# #         g=0
# #         while g<l:
# #             g+=1
# #             r=lst.readline()
# #         #f=lst.readlines()
# #         car=r
# #     cars = car.split()
# #     print(cars)
# #     for i in range(len(cars)):
# #         if cars[i]=='Make:':
# #             mak=cars[i+1]
# #             print(mak+'hi')
# #         if cars[i]=='Model:':
# #             mode=cars[i+1]
# #
# #         if cars[i]=='Year:':
# #             yea=cars[i+1]
# #         if cars[i]=='Acceleration:':
# #             acce=cars[i+1]
# #         if cars[i]=='TopSpeed:':
# #             ts=cars[i+1]
# #     newCar=Car(mak,mode,yea,acce,ts)
# #     #print(type(newCar))
# #     newCar.display_info()
# #     return newCar
# #
# #
# #
# # def chooseCarTwo():
# #     make=''
# #     model='k'
# #     year=''
# #     acceleration=''
# #     topSpeed=''
# #     with open("text.txt", "r") as choice:
# #         choices=choice.read()
# #         line=input(choices+'choose number 0-9')
# #     with open("text.txt","r") as lst:
# #         l=int(line)
# #         g=0
# #         while g<l:
# #             g+=1
# #             r=lst.readline()
# #         #f=lst.readlines()
# #         car=r
# #     cars = car.split()
# #     carDict={}
# #     for i in range(len(cars)):
# #         if cars[i]=='Make:':
# #             carDict['Make']=cars[i+1]
# #
# #         if cars[i]=='Model:':
# #             carDict['Model']=cars[i+1]
# #
# #         if cars[i]=='Year:':
# #             carDict['Year']=cars[i+1]
# #         if cars[i]=='Acceleration:':
# #             carDict['Acceleration']=cars[i+1]
# #         if cars[i]=='TopSpeed:':
# #             carDict['topSpeed']=cars[i+1]
# #     newCar=Car(carDict.get('Make'),carDict.get('Model'),carDict.get('Year'),carDict.get('Acceleration'),carDict.get('topSpeed'))
# #     #print(type(newCar))
# #     newCar.display_info()
# #     return newCar
#
#
#
#
# # #from race import chooseCarOne
# # #from race import chooseCarTwo
# # from Car import Car
# # import random
# #
# # def raceTimeOneKm():
# #     blind= input ('shall your race be random?')
# #     #/////////////////////////////////////////MAKES CAR 1
# #     #car1 = Car("Tesla", "Model S", 2023, 10, 250)
# #     #car2 = Car("Audi", "Model S", 2023, 8, 240)
# #     #car1=chooseCarOne()
# #     #car2=chooseCarTwo()
# #     mak = ''
# #     mode = ''
# #     yea = ''
# #     acce = ''
# #     ts = ''
# #     with open("text.txt", "r") as choice:
# #         choices = choice.read()
# #         line = input(choices + '/nChoose number 1-40:')
# #     with open("text.txt", "r") as lst:
# #         l = int(line)
# #         g = 0
# #         while g < l:
# #             g += 1
# #             r = lst.readline()
# #         # f=lst.readlines()
# #         car = r
# #     cars = car.split()
# #     print(cars)
# #     for i in range(len(cars)):
# #         if cars[i] == 'Make:':
# #             mak = cars[i + 1]
# #             print(mak + 'hi')
# #         if cars[i] == 'Model:':
# #             mode = cars[i + 1]
# #
# #         if cars[i] == 'Year:':
# #             yea = cars[i + 1]
# #         if cars[i] == 'Acceleration:':
# #             acce = cars[i + 1]
# #         if cars[i] == 'TopSpeed:':
# #             ts = cars[i + 1]
# #     car1 = Car(mak, mode, int(yea), float(acce), int(ts))
# #
# #     make = ''
# #     model = 'k'
# #     year = ''
# #     acceleration = ''
# #     topSpeed = ''
# #     with open("text.txt", "r") as choice:
# #         choices = choice.read()
# #         line = input(choices + 'choose number 1-40')
# #     with open("text.txt", "r") as lst:
# #         l = int(line)
# #         g = 0
# #         while g < l:
# #             g += 1
# #             r = lst.readline()
# #         # f=lst.readlines()
# #         car = r
# #     cars = car.split()
# #     carDict = {}
# #     for i in range(len(cars)):
# #         if cars[i] == 'Make:':
# #             carDict['Make'] = cars[i + 1]
# #
# #         if cars[i] == 'Model:':
# #             carDict['Model'] = cars[i + 1]
# #         if cars[i] == 'Year:':
# #             carDict['Year'] = cars[i + 1]
# #         if cars[i] == 'Acceleration:':
# #             carDict['Acceleration'] = cars[i + 1]
# #         if cars[i] == 'TopSpeed:':
# #             carDict['topSpeed'] = cars[i + 1]
# #     car2 = Car(carDict.get('Make'), carDict.get('Model'), int(carDict.get('Year')), float(carDict.get('Acceleration')),
# #                  int(carDict.get('topSpeed')))
# #
# #
# # #///////////////////////////////////////////////   MAKES CAR 2
# #
# #     dcar1=0
# #     dcar2=0
# #     timecar1=0
# #     timecar2=0
# #     t1=True
# #     t2=True
# #     distance=0
# #     if blind=='no':
# #         distance=int(input('how long should the race be in kilometers'))
# #
# #     else:
# #         distance=random.randrange(0,50)
# #
# #     distance = distance * 1000
# #     for i in range(10000):
# #         if dcar1>distance and t1:
# #             timecar1=i
# #             t1=False
# #         if dcar2>distance and t2:
# #             timecar2=i
# #             t2=False
# #         if car1.speed+car1.acceleration<=car1.topSpeed:
# #             car1.speed+=car1.acceleration
# #         else:
# #             car1.speed=car1.topSpeed
# #
# #         dcar1+=car1.speed
# #         if car2.speed+car2.acceleration<=car2.topSpeed:
# #             car2.speed+=car2.acceleration
# #         else:
# #             car2.speed=car2.topSpeed
# #         dcar2 += car2.speed
# #     if timecar1>timecar2:
# #         print('player 2 with the ',car2.make,car2.model,'won with a time of: ',timecar2,'seconds, which was faster than',car1.make,car1.model,'by',timecar1-timecar2,'seconds over a distance of',distance,'meters')
# #     else:
# #         print('player 1 with the ',car1.make,car1.model,'won with a time of: ',timecar1,'seconds, which was faster than',car2.make,car2.model,'by',timecar2-timecar1,'seconds over a distance of',distance,'meters')
# #
# #
# #
# # raceTimeOneKm()
# #
# # # def chooseCarOne():
# # #     mak=''
# # #     mode=''
# # #     yea=''
# # #     acce=''
# # #     ts=''
# # #     with open("text.txt", "r") as choice:
# # #         choices=choice.read()
# # #         line=input(choices+'/nChoose number 0-9:')
# # #     with open("text.txt","r") as lst:
# # #         l=int(line)
# # #         g=0
# # #         while g<l:
# # #             g+=1
# # #             r=lst.readline()
# # #         #f=lst.readlines()
# # #         car=r
# # #     cars = car.split()
# # #     print(cars)
# # #     for i in range(len(cars)):
# # #         if cars[i]=='Make:':
# # #             mak=cars[i+1]
# # #             print(mak+'hi')
# # #         if cars[i]=='Model:':
# # #             mode=cars[i+1]
# # #
# # #         if cars[i]=='Year:':
# # #             yea=cars[i+1]
# # #         if cars[i]=='Acceleration:':
# # #             acce=cars[i+1]
# # #         if cars[i]=='TopSpeed:':
# # #             ts=cars[i+1]
# # #     newCar=Car(mak,mode,yea,acce,ts)
# # #     #print(type(newCar))
# # #     newCar.display_info()
# # #     return newCar
# # #
# # #
# # #
# # # def chooseCarTwo():
# # #     make=''
# # #     model='k'
# # #     year=''
# # #     acceleration=''
# # #     topSpeed=''
# # #     with open("text.txt", "r") as choice:
# # #         choices=choice.read()
# # #         line=input(choices+'choose number 0-9')
# # #     with open("text.txt","r") as lst:
# # #         l=int(line)
# # #         g=0
# # #         while g<l:
# # #             g+=1
# # #             r=lst.readline()
# # #         #f=lst.readlines()
# # #         car=r
# # #     cars = car.split()
# # #     carDict={}
# # #     for i in range(len(cars)):
# # #         if cars[i]=='Make:':
# # #             carDict['Make']=cars[i+1]
# # #
# # #         if cars[i]=='Model:':
# # #             carDict['Model']=cars[i+1]
# # #
# # #         if cars[i]=='Year:':
# # #             carDict['Year']=cars[i+1]
# # #         if cars[i]=='Acceleration:':
# # #             carDict['Acceleration']=cars[i+1]
# # #         if cars[i]=='TopSpeed:':
# # #             carDict['topSpeed']=cars[i+1]
# # #     newCar=Car(carDict.get('Make'),carDict.get('Model'),carDict.get('Year'),carDict.get('Acceleration'),carDict.get('topSpeed'))
# # #     #print(type(newCar))
# # #     newCar.display_info()
# # #     return newCar