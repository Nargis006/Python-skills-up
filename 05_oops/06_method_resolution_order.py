class A:
    label = "Called from class A"
class B(A):
    label = "Called from class B"
class C(A):
        label = "Called from class C"
class D(B, C):
    pass

obj = D()
print(obj.label)  # Output: Called from class B as B is first in MRO - Method Resolution Order
print(D.__mro__)  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]