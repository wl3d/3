import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

        def get_job(self):
            pass
        def get_home(self):
            pass
        def get_car(self):
            pass
        def eat(self):
            pass
        def work(self):
            pass
        def shopping(self, manage):
            pass
        def chill(self):
            pass
        def clean_home(self):
            pass
        def to_repair(self):
            pass
        def days_indexes(self, day):
            pass
        def is_alive(self):
            if (self.gladness < 0):
                print(f"{self.name} has depression...")
                return False
            if(self.satiety < 0):
                print(f"{self.name} is dead...")
                return False
            if (self.money < -500):
                print(f"{self.name} is bankrupt...")
                return False
            return True
        def live(self, day):
            pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strenght = brand_list[self.brand]['strenght']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strenght > 0 and self.fuel > 0 and self.consumption > 0:
             self.fuel -= self.consumption
             return True
        else:
            print("Car cant Move")
            return False

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['gladness']

job_list = {
    "Java_Developer" :
        {"salary": 50, "gladness": 10},
    "Python_Developer" :
        {"salary": 100, "gladness": 10},
    "C++_Developer" :
        {"salary": 100, "gladness": 5},
    "Java_Developer" :
        {"salary": 50, "gladness": 3},
}


brand_of_cars = {
    "BMW" : {"fuel": 100, "strenght" : 100, "consumption" : 6},
    "Volvo" : {"fuel": 200, "strenght" : 120, "consumption" : 20},
    "Ferrari" : {"fuel": 80, "strenght" : 120, "consumption" : 8},
}

first_car=Auto(brand_of_cars)