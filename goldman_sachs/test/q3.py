class Test:
    
    def add(self, *args) -> float:
        # print("inside grandmother")
        total = 0
        print(args)
        for arg in args:
            print(arg)
            total += arg
        
        return total
    
class ChildTest(Test):
    def add(self, *args):
        # print("inside daughter")
        return super().add(*args)
    
class grandChildTest(ChildTest):
    def add(self, *args):
        # print("inside grandchild")
        return super().add(*args)
    

t = Test()
t2 = ChildTest()

print(t.add(1, 2, 3))

print(t.add(1, 2))

print(t2.add(1, 2, 4, 5, 6))

t3 = grandChildTest()


print(t3.add(1, 2, 4))



"""
Q4. B

Q5. C

Q6. Polymorphism - the word means one name, multiple forms

Q7. abstract (i need help with implementation of the same)

Q8. 
Inheritance: reusable code - share properties
abstraction: hide unnecessary complexity
Polymorhphism: one name multiple forms: method overloading and overriding
encapsulation: capsule everything for reusability


Q9. 
abstract class just gives definition
interface may give some basic code? 

Q10. 
using classes? why it is important - not sharing one data with the other. each object of each class has its unique data so yeah
"""



