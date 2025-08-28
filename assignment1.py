# assignment1.py

# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Inheriting from Device
        self.storage = storage
        self.battery = battery

    def call(self, number):
        return f"Calling {number} 📞 from {self.model}..."

    def charge(self):
        return f"{self.model} is charging 🔋..."

    def info(self):
        # Polymorphism: overriding parent method
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}mAh"


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S24", 256, 5000)
    phone2 = Smartphone("Apple", "iPhone 15", 128, 4300)

    print(phone1.info())
    print(phone1.call("+2348123456789"))
    print(phone2.charge())
