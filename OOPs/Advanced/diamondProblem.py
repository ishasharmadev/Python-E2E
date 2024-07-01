class A:
    def method(self):
        print("Method of A")

class B(A):
    pass

class C(A):
    def method(self):
        print("Method of C")

class D(B, C):
    pass

# Usage
obj = D()
obj.method()  # Output: Method of C
