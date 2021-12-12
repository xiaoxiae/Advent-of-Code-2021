import sys

sys.path.insert(0, "../")
from utilities import success, get_input

input = get_input()

gamma_rate = ""
epsilon_rate = ""

for i in range(len(input[0])):
    line = [input[j][i] for j in range(len(input))]
    ones = line.count("1")
    zeroes = line.count("0")

    gamma_rate += "0" if zeroes > ones else "1"
    epsilon_rate += "0" if zeroes < ones else "1"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
