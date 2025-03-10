class Car:
    #This class makes the car
    def __init__(self, make:str, model:str, year:int, acceleration:float, topSpeed:int):
        # Initialize the car's attributes
        self.make = make
        self.model = model
        self.year = year
        self.acceleration = acceleration
        self.topSpeed = topSpeed
        self.speed = 0  # Starting speed is 0

    # Getter and setter for make
    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    # Getter and setter for model
    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    # Getter and setter for year
    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    # Getter and setter for acceleration
    def get_acceleration(self):
        return self.acceleration

    def set_acceleration(self, acceleration):
        self.acceleration = acceleration

    # Getter and setter for topSpeed
    def get_topSpeed(self):
        return self.topSpeed

    def set_topSpeed(self, topSpeed):
        self.topSpeed = topSpeed

    # Getter and setter for speed
    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        if speed < 0:
            print("Speed cannot be negative.")
        elif speed > self.topSpeed:
            print(f"Speed cannot exceed top speed of {self.topSpeed} km/h.")
        else:
            self.speed = speed

    def accelerate(self):
        """Increase the car's speed based on acceleration."""
        if self.speed + self.acceleration <= self.topSpeed:
            self.speed += self.acceleration
        else:
            self.speed = self.topSpeed  # Ensure the speed doesn't exceed the top speed
        print(f"The car is now going {self.speed} km/h.")

    def brake(self):
        """Decrease the car's speed."""
        if self.speed > 0:
            self.speed -= 10  # Decelerate by 10 km/h
        else:
            self.speed = 0  # Speed can't be negative
        print(f"The car is now going {self.speed} km/h.")

    def display_info(self):
        """Display information about the car."""
        e='Car Info: {} {} {}'.format(self.year,self.make,self.model)
        t='Top Speed: {} km/h, Current Speed: {} km/h, Acceleration: {} m/s^2'.format(self.topSpeed,self.speed,self.acceleration)
        print(e)
        print(t)

# Example usage:
my_car = Car("Tesla", "Model S", 2023, 10, 250)

# Display the car's information
my_car.display_info()
#wecnm
