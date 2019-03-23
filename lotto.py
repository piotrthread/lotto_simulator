from random import randint

def input_six_numbers():
    picked_numbers = []
    while not len(picked_numbers) == 6:
        try:
            number = input("Podaj liczbę: ")
            number = int(number)
            if number not in range(1,50):
                print("Liczba z poza zakresu!")
            elif number in picked_numbers:
                print("Ta liczba juz jest!")
            else:
                picked_numbers.append(number)
            
        except ValueError:
            print("To nie jest liczba!")
            continue
    return sorted(picked_numbers)

def check_coupon(your_list, lotto_list):
    guessed_numbers_amount = 0
    for number in your_list:
        if number in lotto_list:
            guessed_numbers_amount += 1
    return guessed_numbers_amount

lotto_numbers = sorted([randint(1,49) for i in range(6)])
your_numbers = input_six_numbers()
print(f"Wylosowane liczby: {lotto_numbers}.")
print(f"Twoje liczby: {your_numbers}.")
print(f"Trafiłeś {check_coupon(your_numbers, lotto_numbers)} !")
