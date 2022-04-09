MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
i= "" 
def coffee(req):
    if req == 'e':
        i = 'espresso'
    elif req == 'l':
        i="latte"
    else:
        i = 'cappuccino'
    return i

def resource_update(req):
    if req == 'e':
        i = 'espresso'
    elif req == 'l':
        i="latte"
    else:
        i = 'cappuccino'
    if req == 'e':
        MENU[i]['ingredients']['milk'] = 0
    resources['water'] =  int(resources['water']) - int(MENU[i]['ingredients']['water'])
    resources['milk'] = int(resources['milk']) - int(MENU[i]['ingredients']['milk']) 
    resources['coffee']= int(resources['coffee']) - int(MENU[i]['ingredients']['coffee'])

def cost(req):
    if req == 'e':
        i = 'espresso'
    elif req == 'l':
        i="latte"
    else:
        i = 'cappuccino'
    quarter = int(input("Please insert the coin for quarter"))
    nickle = int(input("Please insert the coin for nickle"))
    dime = int(input("Please insert the coin for dime"))
    pennies = int(input("Please insert the coin for pennies"))
    cost_entered = quarter + (dime * 2) + nickle + (pennies * 2)
    print(f"You entered ${cost_entered}")
    if float(cost_entered) == float(MENU[i]['cost']):
        print(f"Here's your {i}, Enjoy!")
        resource_update(req)
    elif float(cost_entered) <  float(MENU[i]['cost']):
        print("Sorry, thats not enough, Money refunded")
    elif float(cost_entered) >  float(MENU[i]['cost']):
        pending_amt = format(float(cost_entered) - float(MENU[i]['cost']), ".2f")
        print(f"Here's your ${pending_amt} change.")
        resource_update(req)
        


def check(req):
    if req == 'e':
        i = 'espresso'
    elif req == 'l':
        i="latte"
    else:
        i = 'cappuccino'
    print(i)
    # water_Q = int(MENU[i]["ingredients"]["water"])
    # milk_Q = int(MENU[i]['ingredients']['milk'])
    # coffee_Q = int(MENU[i]['ingredients']['coffee'])
    # cost_Q = int(MENU[i]['cost'])
    print(resources['water'])
    print(resources['milk'])
    print(resources['coffee'])
    
    if req not in 'e':
        if (int(resources['water']) < int(MENU[i]['ingredients']['water'])) or  int(resources['milk']) < int(MENU[i]['ingredients']['milk']) or int(resources['coffee']) < int(MENU[i]['ingredients']['coffee'])  :
            print("We are out of stock, sorry :(")
        req = "off"
        else: 
            cost(req)
    elif req == 'e':
        if (int(resources['water']) < int(MENU[i]['ingredients']['water'])) or int(resources['coffee']) < int(MENU[i]['ingredients']['coffee'])  :
            print("We are out of stock, sorry :(")
            req = "off" 
        else :
            cost(req)    
                                                                          
def request():
    system = False
    while not system:
        req = input("What would you like to have? espress/latte/cappuccino, e/l/c").lower()
        if req == 'off':
            system = True
        elif req == 'report':
            print(resources)
        elif req in ('e','l','c'):
            check(req)
                
request()

