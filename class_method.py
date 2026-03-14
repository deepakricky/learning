class Broski:
    a=1

    @classmethod
    def show(cls):

        print(f"The value of class attribute is {cls.a}")

b=Broski()
b.a=77

b.show()
