
class CarManager:
    all_cars = [] #will store all car instances created
    total_cars = 0

    def __init__(self, make, model, year, mileage, services=[]):
        #create total_cars and create id for this car
        self._id = CarManager.total_cars + 1
        CarManager.total_cars += 1

        CarManager.all_cars.append(self) #update all_cars
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services


    def __str__(self):
        return f"ID: {self._id} | make: {self._make} | model: {self._model} | year: {self._year} | mileage: {self._mileage} | services done to car: {self._services}"
   
    def __repr__(self):
        f"ID: {self._id} | make: {self._make} | model: {self._model} | year: {self._year} | mileage: {self._mileage} | services done to car: {self._services}"

    def details(self):
        print(f"ID: {self._id} | make: {self._make} | model: {self._model} | year: {self._year} | mileage: {self._mileage} | services done to car: {self._services}")
    
    def update_mileage(self, updated_mileage):
        self._mileage = updated_mileage
        print(f'Updated Mileage: {self._mileage}')

    @property
    def get_id(self):
        return self._id
    @property
    def get_make(self):
        return self._make
    @property
    def get_model(self):
        return self._model
    @property
    def get_year(self):
        return self._year
    @property
    def get_mileage(self):
        return self._mileage
    @property
    def get_services(self):
        return self._services
    @property
    def get_all_cars(self):
        return self.all_cars
    



##welcome message
def menu_face():
    print('------ WELCOME ------')
    print("1. Add a car")
    print("2. View all cars")
    print("3. View total number of cars")
    print("4. See a car's details")
    print("5. Service a car")
    print("6. Update mileage")
    print("7. Quit")


##functions for choices---------

##choice 1  
def add_car():
    new_make = input('tell me the make of the car: ')
    new_model = input('tell me the model of the car: ')
    new_year = int(input('tell me the year of the car: '))
    new_mileage = int(input('tell me the mileage of the car: '))
    new_services = [input('tell me the services the car has had: ')]
    new_id = CarManager.total_cars + 1
    car_name = f'car{new_id}'
    car_name = CarManager(new_make, new_model, new_year, new_mileage, new_services)
    print(f'you have added a new car, this is your ID: {car_name.get_id}')

##choice 2
def view_all_cars():
    for car in CarManager.all_cars:
                print(str(car))

##choice 4 
def car_details():
    which_car = int(input("which car's details? please provide the ID "))
    for car in CarManager.all_cars:
        if car._id == which_car:
            car.details()

##choice 5  
def service_a_car():
    which_car = int(input("which car needs servicing? please provide the ID "))
    for car in CarManager.all_cars:
        if car._id == which_car:
            new_services = []
            add_these_services = input('what services do you need? ')
            new_services.append(add_these_services)
            car._services.append(new_services)

##choice 6  
def replace_mileage():
    which_car = int(input("which car needs their mileage updated? please provide the ID "))
    for car in CarManager.all_cars:
        if car._id == which_car:
            new_mileage = int(input("what's the new mileage?  "))
            car.update_mileage(new_mileage)

##returning to menu face function-----------
            
def return_to_menu_face():
    #return to main menu
    user_input = (int(input('Press 0 if you want to return to main menu, press any other number to exit menu')))
    return user_input
    # if user_input == 0:
    #     return
    # elif user_input == 7:
    #     print('goodbye!')
    #     return False

    # '''main function'''
def main():
    user_input = 0
    while user_input == 0:
        
        menu_face()
        choice = int(input("Enter your choice number "))

        # "1. Add a car"
        if choice == 1:
            add_car()
            #return to main menu
            user_input = return_to_menu_face()
            
        # "2. View all cars
        elif choice == 2:
            view_all_cars()
            #return to main menu
            user_input = return_to_menu_face()


        # 3. View total number of cars
        elif choice == 3:
            print(f'Total Number of Cars: {CarManager.total_cars}')
             #return to main menu
            user_input = return_to_menu_face()

        
        #4. See a car's details"
        elif choice == 4:
            car_details()
             #return to main menu
            user_input = return_to_menu_face()
                
        # "5. Service a car"
        elif choice == 5:
            service_a_car()
             #return to main menu
            user_input = return_to_menu_face()
                

        # "6. Update mileage"
        elif choice == 6:
            replace_mileage()
             #return to main menu
            user_input = return_to_menu_face()
                 
        # quit
        elif choice == 7:
            break
        
        else:
            raise ValueError('enter a number 1-7')
    


# car1.terminal_menu()


# print(f"total cars: {CarManager.total_cars} before new car is added")
car1 = CarManager("jeep", 'wrangler', 2010, 99999, ['upgraded seats', 'added rims'])
# print(f" car is now added, this id is {car1._id}")

car2 = CarManager('ford','fusion', 2016, 11111, ['car freshner'])
# print(car2)

main()



# # print(f"total cars: {CarManager.total_cars}  before new car is added")
# # car2 = CarManager('ford','fusion', 2016, 11111, ['car freshner'])
# # print(f"car is now added, this id is {car2._id}")
# # print(CarManager.all_cars)

# # print(f"total cars: {CarManager.total_cars} before new car is added")
# # car3 = CarManager('toyota', 'camry', 1999, 200000)
# # print(f"car is now added, this id is {car3._id}")
# # print(CarManager.all_cars)
