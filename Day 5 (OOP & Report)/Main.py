class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        if velocity > 200:
            velocity = 200
        self.velocity = velocity
        fuel_needed = distance // 10 * 10
        self.fuelRate -= fuel_needed
        if self.fuelRate <= 0:
            self.fuelRate = 0
            self.stop(distance)
        else:
            self.stop(0)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance == 0:
            print("You arrived")
        else:
            print(f"{remain_distance}")


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount
        if self.car.fuelRate > 100:
            self.car.fuelRate = 100

    def send_mail(self, to, subject, body, receiver_name):
        print(f"mail to {receiver_name} <{to}>  {subject} {body}")
class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        employee = self.get_employee(empId)
        if employee:
            self.employees.remove(employee)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        employee = self.get_employee(empId)
        if employee:
            employee.salary -= deduction

    def reward(self, empId, reward):
        employee = self.get_employee(empId)
        if employee:
            employee.salary += reward

    def check_lateness(self, empId, moveHour):
        employee = self.get_employee(empId)
        if employee:
            is_late = Office.calculate_lateness(9, moveHour, employee.distanceToWork, employee.car.velocity)
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)



    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True
        travel_time = distance / velocity
        arrival_time = moveHour + travel_time
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num








samy_car = Car("Fiat128", 100, 60)
samy = Employee("Samy", 1000, "happy", 100, 1, samy_car, "samy@iti.com", 5000, 20)
iti_office = Office("ITI Smart Village")
iti_office.hire(samy)
print(iti_office.get_all_employees())
samy.drive(20)
iti_office.check_lateness(1, 7)






