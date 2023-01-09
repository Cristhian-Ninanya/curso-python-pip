import random

def choose_options():
    options = ('piedra', 'papel','tijera')
    user_option = input('Elegir piedra, papel o tijera: ')
    user_option = user_option.lower()

    if not user_option in options:
        print('Opcion no valida')
        #continue
        return None, None

    computer_option = random.choice(options)
    print('User option:',user_option)
    print('Computer option:',computer_option)
    return user_option , computer_option

def check_rules(user_option,computer_option, computer_wins, user_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('User gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Computer gano!!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('User gano!')
            user_wins += 1
        else:
            print('Tijera gana a Papel')
            print('Computer gano!!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('User gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Computer gano!!')
            computer_wins += 1
    return user_wins , computer_wins

#Definicion del juego
def run_game():
    computer_wins = 0
    user_wins =0
    rounds = 1

    while True:
        print()
        print('*' * 10)
        print('ROUND:',rounds)
        print('*' * 10)

        print('User Wins = ',user_wins)
        print('Computer Wins = ',computer_wins)
        rounds += 1

        #Funcion para escoger opciones
        user_option, computer_option = choose_options()
        #Funcion para validar el ganador
        user_wins , computer_wins = check_rules(user_option,computer_option, computer_wins, user_wins)
        
        if computer_wins == 2:
            print('Gana la computadora!!!')
            break
        if user_wins == 2:
            print('Usuario gano!!!')
            break

#Ejecutar funcion principal
run_game()
