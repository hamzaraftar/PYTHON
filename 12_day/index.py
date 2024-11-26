# Global Constant
enemies = 1

def increase_enemies():
    global enemies 
    enemies =+ 1
    print(f'enemies inside function {enemies}')

increase_enemies()
print(f'enemies inside funcion is {enemies}')