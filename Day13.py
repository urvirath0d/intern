class CoffeeMaker:
    water=300
    milk=400
    coffee=150
    money=0
    def __init__(self,value):
        self.value=value
    def report(self,value):
        print("Water:",self.water,"ml\nMilk:",self.milk,"ml\nCoffee:",self.coffee,"g\nMoney:$",self.money)
    def makecoffee(self,value):
        if(value=="latte"):
            self.water=self.water-50
            self.milk=self.milk-70
            self.coffee=self.coffee-50
            self.money=self.money+2.50
            print("Here is your latte. Enjoy!")
        elif(value=="espresso"):
            self.water=self.water-100
            self.milk=self.milk-10
            self.coffee=self.coffee-100
            self.money=self.money+3.50
            print("Here is your espresso. Enjoy!")
        else:
            self.water=self.water-70
            self.milk=self.milk-50
            self.coffee=self.coffee-70
            self.money=self.money+4.50
            print("Here is your cappucino. Enjoy!")
    def transac(self,value,amount):
        if(value=="latte"):
            if(amount<2.50):
                print("Sorry that's not enough money. Money refunded.")
            elif(amount>2.50):
                print("Here is $",round(amount-2.50,2),"dollars in change.")
                self.makecoffee(value)
            else:
                self.makecoffee(value)
        elif(value=="espresso"):
            if(amount<3.50):
                print("Sorry that's not enough money. Money refunded.")
            elif(amount>3.50):
                print("Here is $",round(amount-3.50,2),"dollars in change.")
                self.makecoffee(value)
            else:
               self.makecoffee(value)
        else:
            if(amount<4.50):
                print("Sorry that's not enough money. Money refunded.")
            elif(amount>4.50):
                print("Here is $",round(amount-4.50,2),"dollars in change.")
                self.makecoffee(value)
            else:
                self.makecoffee(value)
    def coins(self,value):
        quarters=0.25
        dimes=0.10
        nickles=0.05
        pennies=0.01
        print("Insert coins!")
        q=int(input("Enter number of quarters:"))
        d=int(input("Enter number of dimes:"))
        n=int(input("Enter number of nickles:"))
        p=int(input("Enter number of pennies:"))
        amount=(q*quarters)+(d*dimes)+(n*nickles)+(p*pennies)
        self.transac(value,amount)
    def resources(self,value):
        if(value=="latte"):
            if(self.water<50):
                print("Sorry there is not enough water!")
            elif(self.milk<70):
                print("Sorry there is not enough milk!")
            elif(self.coffee<50):
                print("Sorry there is not enough coffee!")
            else:
                self.coins(value)
        elif(value=="espresso"):
            if(self.water<100):
                print("Sorry there is not enough water!")
            elif(self.milk<10):
                print("Sorry there is not enough milk!")
            elif(self.coffee<100):
                print("Sorry there is not enough coffee!")
            else:
                self.coins(value)
        else:
            if(self.water<70):
                print("Sorry there is not enough water!")
            elif(self.milk<50):
                print("Sorry there is not enough milk!")
            elif(self.coffee<70):
                print("Sorry there is not enough coffee!")
            else:
                self.coins(value)
       
    
    
   
                
        
x="on"
s=CoffeeMaker(x)
while(True):
    print("\n\nLatte:$2.50\nEspresso:$3.50\nCappucino:$4.50")
    x=input("What would you like?(espresso/latte/cappucino):")
    if(x=="off"):
        break
    if(x=="report"):
        s.report(x)
        continue
    s.resources(x)
    
