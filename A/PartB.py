import unittest
from PartA import Car, Motorbike  # Import classes from PartA.py in the same folder

class TestInstances(unittest.TestCase):
    def test_instance_of_car(self):
        # B2. Test if an object is an instance of Car.
        car = Car("Toyota", 2015, 180, 12, "Red")
        try:
            self.assertIsInstance(car, Car, "Car instance creation failed: Object is not an instance of Car")
            print("test_instance_of_car: Success")
        except AssertionError as e:
            print("test_instance_of_car: Failure -", e)
            raise

    def test_instance_of_motorbike(self):
        # B2. Test if an object is an instance of Motorbike.
        bike = Motorbike("Harley Davidson", 2020, 220, 5000, "Black", 1200, "Cruiser")
        try:
            self.assertIsInstance(bike, Motorbike, "Motorbike instance creation failed: Object is not an instance of Motorbike")
            print("test_instance_of_motorbike: Success")
        except AssertionError as e:
            
            print("test_instance_of_motorbike: Failure -", e)
            raise

    def test_object_not_instance(self):
        # B3. Test if a Car object is NOT an instance of Motorbike.
        car = Car("Toyota", 2015, 180, 12, "Red")
        try:
            self.assertNotIsInstance(car, Motorbike, "Type check failed: Car object should not be an instance of Motorbike")
            print("test_object_not_instance: Success")
        except AssertionError as e:
            print("test_object_not_instance: Failure -", e)
            raise

    def test_objects_identical(self):
        # B4. Test if 2 variables reference the same object.
        car = Car("Toyota", 2015, 180, 12, "Red")
        same_car = car  # Both variables refer to the same object.
        try:
            self.assertIs(car, same_car, "Identity check failed: Both references should point to the same object")
            print("test_objects_identical: Success")
        except AssertionError as e:
            print("test_objects_identical: Failure -", e)
            raise

    def test_objects_not_identical(self):
        # Additional: Test that two separately created objects (even with identical attributes) are not identical.
        car1 = Car("Toyota", 2015, 180, 12, "Red")
        car2 = Car("Toyota", 2015, 180, 12, "Red")
        try:
            self.assertIsNot(car1, car2, "Identity check failed: Two different objects should not be identical")
            print("test_objects_not_identical: Success")
        except AssertionError as e:
            print("test_objects_not_identical: Failure -", e)
            raise

if __name__ == "__main__":
    # Run tests with increased verbosity to display detailed results.
    unittest.main(verbosity=2)
