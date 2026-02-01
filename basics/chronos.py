#creating the class
class millenia:
    def __init__(self,name,gender,color,haircolor,age):
        self.name=name
        self.gender=gender
        self.color=color
        self.haircolor=haircolor
        self.age=age
        print("person is created")
    def display(self):
        print("name:",self.name,"gender:",self.gender,"color:",self.color,"haircolor:",self.haircolor,"age",self.age)
    def update(self):
        choice=input("would you like to change your age good sir...")
        if choice == "yes":
            aje=int(input("what is your updated age;good sir"))
            self.age=aje
        else:
            print("very well good sir,have a delightful day")
#object creation
person1=millenia("Stuti,","female,","brown,","black,",25)
person2=millenia("Karl","Male","beige","Brown",13)
person1.display()
person2.display()
person1.update()
person1.display()