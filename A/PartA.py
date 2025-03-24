class Car:
    def __init__(self, name, year, max_speed, mileage, colour):
        #initialize the car object with the provided attributes.
        self.name = name
        self.year = year
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour  

    def display_car(self):
        #display the car's attributes.
        print("Name:", self.name)
        print("Year:", self.year)
        print("Max Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Colour:", self.colour)

    def update_name(self, new_name):
        #update the cars name after checking if the input is a string.
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self.name = new_name
        print("Name updated to:", self.name)

    def update_year(self, new_year):
        # update the cars year
        if not isinstance(new_year, int):
            raise TypeError("Year must be an integer")
        self.year = new_year
        print("Year updated to:", self.year)

    def update_max_speed(self, new_max_speed):
        #update cars maximum speed ensuring value is an integer.
        if not isinstance(new_max_speed, int):
            raise TypeError("Max speed must be an integer")
        self.max_speed = new_max_speed
        print("Max Speed updated to:", self.max_speed)

    def update_mileage(self, new_mileage):
        #update the mileage
        if not isinstance(new_mileage, int):
            raise TypeError("Mileage must be an integer")
        self.mileage = new_mileage
        print("Mileage updated to:", self.mileage)

    def update_colour(self, new_colour):
        #update the cars colour.
        if not isinstance(new_colour, str):
            raise TypeError("Colour must be a string")
        self.colour = new_colour
        print("Colour updated to:", self.colour)

# Child class Motorbike inheriting from Car
class Motorbike(Car):
    def __init__(self, name, year, max_speed, mileage, colour, engine_capacity, type):
        #initialize the motorbike object with the provided attributes, inheriting from Car.
        super().__init__(name, year, max_speed, mileage, colour)
        
        # check that engine_capacity variable is an integer.
        if not isinstance(engine_capacity, int):
            raise TypeError("Engine capacity must be an integer")
        self.engine_capacity = engine_capacity

        # check that type variable is a string.
        if not isinstance(type, str):
            raise TypeError("Type must be a string")
        self.type = type

    def display_motorbike(self):
        #display the motorbike's attributes.
            #attributes inherited from Car.
        print("Name:", self.name)
        print("Year:", self.year)
        print("Max Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Colour:", self.colour)
        #print("Type:", self.type)

        #additional attribute specific to Motorbike.
        print("Engine Capacity:", self.engine_capacity)
        print("Type:", self.type)

    def update_engine_capacity(self, new_engine_capacity):
        #update the engine capacity also checking if the input is an integer.
        if not isinstance(new_engine_capacity, int):
            raise TypeError("Engine capacity must be an integer")
        self.engine_capacity = new_engine_capacity
        print("engine Capacity updated to:", self.engine_capacity)
    def update_type(self, new_type):
        #update the type of motorbike (Offroad, Racer, Grand Tour or Cruiser).
        if not isinstance(new_type, str):
            raise TypeError("Type must be a string")
        self.type = new_type
        print("Type updated to:", self.type)

def main():
    # Manual entry for testing car funcions as I create them
    mode = input("Do you want manual input? (y/n): ").strip().lower()
   
    #if yes then manual input for car attributes.
    if mode == 'y':
        # manual input for the car attributes.
        name = input("Enter the car name: ")
        year_input = input("Enter the car year (integer): ")
        try:
            year = int(year_input)
        except ValueError:
            print("Invalid input for year. Using default value 2000.")
            year = 2000

        max_speed_input = input("Enter the car's maximum speed (integer): ")
        try:
            max_speed = int(max_speed_input)
        except ValueError:
            print("Invalid input for max speed. Using default value 100.")
            max_speed = 100

        mileage_input = input("Enter the car's mileage (integer): ")
        try:
            mileage = int(mileage_input)
        except ValueError:
            print("Invalid input for mileage. Using default value 0.")
            mileage = 0

        colour = input("Enter the car colour: ")

        # create a Car object using the manual inputs.
        car1 = Car(name, year, max_speed, mileage, colour)
    # if no then auto-populate the car attributes.
    else:
        # auto-population of the car attributes.
        print("Auto populating the car attributes with default values.")
        name = "Toyota"
        year = 2015
        max_speed = 180
        mileage = 12
        colour = "Red"
        # create a Car object using auto-populated values.
        car1 = Car(name, year, max_speed, mileage, colour)

    # display the car's details.
    print("===================< Car Details >===================")
    car1.display_car()
    print("===================< Car Details >===================")

    # Create an instance of the Motorbike class with correct initialization.
        # becaus its not part of the test that i need to create manual input for motorbike or car
        # i will just auto populate the motorbike attributes

    print("\n  Creating a Motorbike instance with default values.")
    motorbike1 = Motorbike("Harley Davidson", 2020, 220, 5000, "Black", 1200, "Cruiser")
    print("===================<  Details >===================")
    motorbike1.display_motorbike()
    print("===================<  Details >===================")

    # update the car's attributes.
    car1.update_name("Honda")
    car1.update_year(2018)
    car1.update_max_speed(200)
    car1.update_mileage(25000)
    car1.update_colour("Blue")
    print("===================< updated Details >===================")
    car1.display_car()
    print("===================< update Details >===================")

    # update the motorbike's attributes.
    motorbike1.update_name("Ducati")
    motorbike1.update_year(2019)
    motorbike1.update_max_speed(250)
    motorbike1.update_mileage(3000)
    motorbike1.update_colour("Red")
    motorbike1.update_engine_capacity(1500)
    motorbike1.update_type("Racer")
    print("===================< mBIKE Updated Details >===================")
    motorbike1.display_motorbike()
    print("===================< mBike Updated Details >===================")


if __name__ == "__main__":
    main()