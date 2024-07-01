# Not following ISP
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Human(Worker):
    def work(self):
        # code to work

    def eat(self):
        # code to eat

class Robot(Worker):
    def work(self):
        # code to work

    def eat(self):
        pass  # Robots don't eat, but they have to implement the method

# Following ISP
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        # code to work

    def eat(self):
        # code to eat

class Robot(Workable):
    def work(self):
        # code to work
