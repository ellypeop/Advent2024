import re

f = open("input_files/d3.txt")
file_contents = f.read()

pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
matches = pattern.finditer(file_contents)

multipliers = []

for match in matches:
    multipliers.append(match[0])

numbers = [list(map(int, re.findall(r'\d+', string))) for string in multipliers]

multiply = [[a * b for a, b in numbers]]

flat_list = [i for i in multiply for i in i]

print(sum(flat_list))