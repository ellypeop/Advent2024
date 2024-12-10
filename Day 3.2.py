import re

f = open("input_files/d3.txt")
file_contents = f.read()

pattern_1 = re.compile(r'\bdon\'t\b.+?\bdo\b|\Z')

def clean_text(parser, text):
    new_text = text
    new_text = re.sub(pattern_1, '', new_text)
    return new_text

cleaned_text = clean_text(pattern_1, file_contents)
result = cleaned_text[0:12980]

pattern_2 = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
matches = pattern_2.finditer(result)

multipliers = []

for match in matches:
    multipliers.append(match[0])

numbers = [list(map(int, re.findall(r'\d+', string))) for string in multipliers]

multiply = [[a * b for a, b in numbers]]

flat_list = [i for i in multiply for i in i]

print(sum(flat_list))