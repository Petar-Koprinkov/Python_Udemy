import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_set = []
computer_set = []
user_score = 0
computer_score = 0


def draw_card(card_set):
    card_set.append(random.choice(cards))


for _ in range(2):
    draw_card(user_set)
    draw_card(computer_set)

if 11 in user_set and len(user_set) == 2 and user_score > 21:
    user_set.remove(11)
    user_set.append(1)

print(f'Your cards are {user_set[0]} and {user_set[1]}')
print(f'Computer card is {computer_set[0]}\n')

while len(user_set) < 3 and input("Do you want to draw cards. Type 'y' or 'n': ").lower() == 'y':
    draw_card(user_set)

while sum(computer_set) < 17:
    draw_card(computer_set)


def sum_score(u_set, c_set):
    user = sum(u_set)
    pc = sum(c_set)
    return user, pc


user_score, computer_score = sum_score(user_set, computer_set)

c_numbers = []
u_numbers = []

for number in user_set:
    u_numbers.append(str(number))

print(f'\nYour cards are: ' + ', '.join(u_numbers))

for number in computer_set:
    c_numbers.append(str(number))

print(f'Computer cards are: ' + ', '.join(c_numbers))


def print_statement():
    print(f'\nYour score is {user_score}')
    print(f'Your opponent score is {computer_score}\n')


def final_result():
    print_statement()
    if user_score == computer_score:
        return 'Draw!'
    elif user_score > 21:
        return 'You lose!'
    elif computer_score > 21:
        return 'You win!'
    elif user_score == 21:
        return 'You win! You have Blackjack'
    elif computer_score == 21:
        return 'You lose! Your opponent have Blackjack'
    elif user_score > computer_score:
        return 'You win! You have better cards'
    else:
        return 'You lose! Your opponent have better cards'


print(final_result())
