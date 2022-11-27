import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.txt"


def csv_to_list_dict(file, delimiter=',') -> list[dict]:
    with open(file, encoding='utf-8') as f:
        headers = f.readline().replace('\n', "").split(delimiter)
        for line in f:
            line_new = line.replace('\n', "").split(delimiter)
            yield dict(zip(headers, line_new))


indent = "      "
new_line = "\n"
count_2 = 0
line_count = sum(1 for line in open(INPUT_FILE)) - 1

with open(OUTPUT_FILE, 'w') as dst:
    dst.write("[" + new_line)
    for record in csv_to_list_dict(INPUT_FILE):
        dst.write(indent + "{" + new_line)
        for count_1, (key, value) in enumerate(record.items()):
            dst.write(f'{indent}{indent}"{key}": {value}')
            if count_1 < len(record) - 1:
                dst.write(',')
                count_1 += 1
                else:
                count_1 = 0
            dst.write(new_line)
            dst.write(indent + "}")
            if count_2 < line_count - 1:
                dst.write(',')
                count_2 += 1
            dst.write(new_line)
        dst.write("]")

    with open(OUTPUT_FILE) as f:
        data = json.load(f)
        print(data)