class Person:
    def __init__(self, param_name):
        print("I am created!", self)
        self.name = param_name
    def talk(self):
        print("안녕하세요, 제 이름은", self.name,"입니다.")

person_1 = Person("박상재")
print(person_1.name)
print(person_1)
person_1.talk()
person_2 = Person("김종욱")
print(person_2.name)
print(person_2)
person_2.talk()
