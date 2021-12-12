# Advent of Code Day 2: https://adventofcode.com/2021/day/2

with open('input.txt', 'r') as file:
    data = file.readlines()

input = [line.strip() for line in data]

horizontal, depth = 0,0

for movement in input:
    direction = movement.split()[0]
    amount = int(movement.split()[1])
    
    if direction == "forward":
        horizontal += amount
    elif direction == "down":
        depth += amount
    else:  # direction is up
        depth -= amount

print(depth*horizontal)