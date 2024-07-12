from unittest.mock import patch
from doors_game import play
import random

doors = [1, 2, 3]
switch = ['', 'yes']
results = []

for i in range(1000):
    simulate_values = [random.choice(doors), 'yes']

    with patch("builtins.input", side_effect=simulate_values):
        result = play()
        results.append(result)

print(len([result for result in results if result[2] == 'car']))
