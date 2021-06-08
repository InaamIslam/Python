#PRACTICING USING FUNCTIONS 

def basket(): 
    print("My Shopping is in this basket")

basket() #this calls the fucntion

####IF STATEMENTS WITHIN FUNCTIONS

def basket(items):
    if items == "Full":
        print("Trolley is full")
    else: 
        print("no itmems in this basket")

basket("Full") #This is my argument 'Full' 

#

def basket(items):
    if items == "Full":
        print("Trolley is full")
    else: 
        print("no itmems in this basket")

basket("empty") #This is my argument 'Full' 


#LEARING TO RETURN VALUES 

def basket(items):
    if items == "Vegatables":
        return "Broccoli, cabbage..."
    else:
        return "chicken, meat.."

items("Vegetables")

Order = f'(NO.1 + {basket})'

print(Order)


