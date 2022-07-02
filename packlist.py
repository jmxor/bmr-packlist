import os
import re


def process_delivery_note(filename: str):
    note_pattern = re.compile(r'Ind. (\w*)')
    order_pattern = re.compile(r'\d\(([A-Z]{1,3}\d{5}[A-Z]?)')
    replacement_pattern_1 = re.compile(r'(\w{5}[-BCT]\w{5}([-JN][\dA-Z]{3})? replaces :)')
    replacement_pattern_2 = re.compile(r'(\w{5}[-BCT]\w{5}([-JN][\dA-Z]{3})? is replaced by :)')
    part_pattern = re.compile(r'(\w\d{4}[-BCT]\w{5}([-JN][\dA-Z]{3})?).*\s(\d{1,3})\n')
    parts = []

    # read the contents of the file
    with open(filename) as file:
        lines = file.readlines()

    # loop over the contents of the file
    for line in lines:
        if match := note_pattern.findall(line):
            note_number = match[0]
        elif match := replacement_pattern_1.findall(line):
            parts.append(f',,{match[0][0]}\n')
        elif match := replacement_pattern_2.findall(line):
            parts.append(f',,{match[0][0]}\n')
        elif match := order_pattern.findall(line):
            order_number = match[0]
        elif match := part_pattern.findall(line):
            part_number, _, quantity = match[0]
            parts.append(f'{note_number}, {order_number}, {part_number}, {quantity}\n')

    return parts


def main():
    pass


if __name__ == '__main__':
    main()