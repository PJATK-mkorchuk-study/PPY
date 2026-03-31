dict = {}
prev_var = 0
while True:
    user_input = int(input('Enter a number(Enter 0 if you want to leave): '))
    
    if user_input == 0:
        break

    if user_input == prev_var or dict.get(str(user_input)) != None:
        dict.update({str(user_input): dict.get(str(user_input)) + 1})
    else:
        dict.update({str(user_input): 1})

    prev_var = user_input
    

print(dict)