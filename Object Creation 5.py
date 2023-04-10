from datetime import datetime

#define car class
class Car:
    def __init__(self, make, model, year, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

#define rental class
class Rental:
    def __init__(self, car, start_date, end_date, customer_name):
        self.car = car
        self.start_date = start_date
        self.end_date = end_date
        self.customer_name = customer_name

    #define rental period method
    def get_rental_period(self):

        #convert string to date object
        start = datetime.strptime(self.start_date, '%Y-%m-%d').date()
        end = datetime.strptime(self.end_date, '%Y-%m-%d').date()

        #calculate rental duration
        duration = (end - start).days
        return duration
    
    #define rental cost method
    def get_rental_cost(self):
        daily_rate = self.car.daily_rate
        duration = self.get_rental_period()
        cost = duration * daily_rate
        return cost


Car_1 = Car("Nissan", "Kumquat", 2020, 90)
Car_2 = Car("Toyota", "Corolla", 2021, 59)
selected_car = Car_1
Rental_1 = Rental(selected_car, "2023-04-21", "2023-04-29", "Jenkins")

#display rental period and cost for the period
rental = Rental_1
print(f"Rental period: {rental.get_rental_period()} days")
print(f" Rental cost: ${rental.get_rental_cost()} ")       
