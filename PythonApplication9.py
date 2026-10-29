class User():
    def __init__(self,name,surname,__number,__balance):

        self.name = name
        self.surname = surname
        self.__number = int(__number)
         

        self.__balance = int(__balance)
        
    @property
    def number(self) -> int:
        return self.__number
            
    @property
    def balance(self) -> int:
        return self.__balance

    def replenishment(self,x):
        if(x > 0):
            self.__balance += x

        else:
            print("Нельза положить отрицательное кол-во денег")
    def withdraw (self,x):
         if(x <= 0):
            print("Нельза снять отрицательное или нулевое кол-во денег")
         elif(x > self.__balance):
            print("У вас не достаточно средств ):")
         else:
            self.__balance -= x

    def showall(self):
        print(self.name, self.surname,self.__number,self.__balance)
user1 = User("Ivan","Ivanov","123","848")
user1.withdraw(0)
user1.showall()