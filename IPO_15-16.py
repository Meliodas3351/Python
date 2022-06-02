from abc import *


class ElectricCar(ABC):
    name = "Car"

    def __init__(self, charge, model, serviceability):
        self.charge = charge
        self.model = model
        self.serviceability = serviceability

    def get_rules(func):
        def use_funk(self):
            print("Decorator body")
            val = func(self)
            return val

        return use_funk

    @get_rules
    def get_rules_for_using(self):
        return "Rules for using - ..."

    @get_rules
    def get_rules_for_driving(self):
        return "Rules for driving - ..."

    @get_rules
    def get_rules_for_running(self):
        return "Rules for running - ..."

    @abstractmethod
    def print_info_about_company(self):
        pass

    @staticmethod
    @abstractmethod
    def get_car():
        pass

    def drive(self, distance):
        if self.charge >= distance and self.serviceability == True:
            for i in range(distance):
                print("Car traveled a kilometer.")
            self.charge -= distance
        elif self.charge <= 0:
            print("Not enough charge")
        else:
            print("Car is out of order")

    def drive_in_all_charge(self):
        x = 0
        while self.charge > 0:
            x += 1
            self.charge -= 1
        print("Car traveled " + x + " kilometres")

    def update_charge_dekorator(func):

        def inner_method(self, new_charge):
            print("Decorator body")
            return func(self, new_charge)
        return inner_method

    @update_charge_dekorator
    def update_charge(self, new_charge):
        self.charge = new_charge
        return "New Charge - " + str(self.charge)


    def repare_car(self):
        self.serviceability = True

    def break_car(self):
        self.serviceability = False

    def get_charge(self):
        return self.charge

    def get_serviceability(self):
        return self.serviceability

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def set_charge(self, charge):
        self.charge = charge

    def __str__(self):
        stre = str("Model - " + str(self.model) + "\nCharge - " + str(self.charge) + " \nServiceability " + str(
            self.serviceability))
        return stre


class Tesla(ElectricCar):
    def __init__(self, charge, model, serviceabnility):
        super().__init__(charge, model, serviceabnility)

    def print_info_about_company(self):
        print("Tesla is Elon Musk's company")

    @staticmethod
    def get_car():
        return Tesla(1200, "Tesla XXX", True)



tesla1 = Tesla(1111, " sfsdfd", True)

#print(tesla1.get_rules_for_driving())

print(tesla1.get_rules_for_using())

print(tesla1.update_charge(500))