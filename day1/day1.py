# Advent of Code Day 1: https://adventofcode.com/2021/day/1
# off by 1 need to figure out why
with open('input.txt', 'r') as file:
    data = file.readlines()

input = [line.strip() for line in data]

greaterCount = 0

for i in range(1, len(input)):
    if input[i] > input[i-1]:
        greaterCount+=1

print(greaterCount)