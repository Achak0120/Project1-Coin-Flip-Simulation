#coin flip simulation
import random

coinFaces = ['Heads', 'Tails']

input('Type 1 to flip the coin: ')
if 1:
    result = random.choice(coinFaces)
    print(result)
else:
    print('PLEASE RESPOND WITH THE NUMBER 1 AND TRY AGAIN')
