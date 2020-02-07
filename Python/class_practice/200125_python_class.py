# class CountFromBy:
#     pass
#
# a = CountFromBy()
# b = CountFromBy
#
# def apple():
#     return 'Hi'
#
# i = apple()
# j = apple

# print("소괄호가 있는 class : ",a)
# print("소괄호가 없는 class : ",b)
# print("소괄호가 있는 함수   : ",i)
# print("소괄호가 없는 함수   : ",j)

class Person():
    def __init__(self, name):
        self.name = name

someone = Person('Elmer Fudd')

# print(someone)
# print(someone.name)

#class 상속, 오버라이드
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")

# car = Car()
# car.exclaim()

#car객체의 Car클래스를 찾는다.
#car객체를 Car클래스의 exclaim()메서드의 self 매개변수에 전달한다.


# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
#
# give_me_a_car.exclaim()
# give_me_a_yugo.exclaim()
# give_me_a_yugo.need_a_push()
#
# class MDPerson(Person):
#     def __init__(self, name):
#         self.name = "Doctor " + name
#
# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name + ", Esquire"
#
# person = Person('Fudd')
# doctor = MDPerson('Fudd')
# lawyer = JDPerson('Fudd')
# print(person.name)
# print(doctor.name)
# print(lawyer.name)
#
# class EmailPerson(Person):
#     def __init__(self, name, email):
#         super().__init__(name)
#         self.email = email
#
# bob = EmailPerson('Bob Frapples', "bob@frapples.com")
# print(bob.name)
# print(bob.email)


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print("inside the getter")
        return self.hidden_name
    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
fowl.name
fowl.get_name()
fowl.set_name('Howard')



