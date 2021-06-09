#pythonif True: 
#this will always run because it is always true 
#if False 
#this will never run beacuse false is always false 

if 4 == 4: 
    age = 25 
    print (age)
name = "inaam"
print (name)

if 5 == 5:
    age = 55 
    print (age)
elif 3 == 6:
    hungry = True
    print (hungry) 

devs_money = 100
dev_can_play_smash = False

if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tornament!")
elif devs_money < 1 and dev_can_play_smash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")
