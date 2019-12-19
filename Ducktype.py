
class Pycharm:
    def execute(self):
        print("Compliling")
        print("Running")

class Editor:
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compliling")
        print("Running")
class Laptop:
    def code(self,ide):
        ide.execute()

ide= Editor()


lap= Laptop()
lap.code(ide)