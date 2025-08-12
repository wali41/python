class Car:
    def __init__(self, brand, color):
        self.brand = brand        # attribute
        self.color = color        # attribute

    def drive(self):              # behavior
        print(f"The {self.color} {self.brand} is driving.")

class Phone:
    def __init__(self, model, battery_life):
        self.model = model
        self.battery_life = battery_life  # in hours

    def call(self, contact):
        print(f"Calling {contact} from {self.model}...")

class Event:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def start(self):
        print(f"The event '{self.name}' is starting at {self.time}.")

# Create separate objects
car1 = Car("Toyota", "red")
phone1 = Phone("iPhone 15", 20)
event1 = Event("Meeting", "10:00 AM")

# Each object works independently
car1.drive()
phone1.call("Ali")
event1.start()