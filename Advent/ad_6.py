import argparse


ONE_WORD = 1
TWO_WORDS = 2
COMMAND_SHIFT_1 = -1
COMMAND_SHIFT_2 = 2


class LightGrid(object):
    def __init__(self, sizes=(1000, 1000)):
        self.sizes = sizes
        self.grid = [False] * sizes[0] * sizes[1]  # Everything is turned off

    def edit_square(self, coordinates, operation):
        # Coordinates have ((x, y), (x, y)) format
        point_1, point_2 = coordinates  # TODO: Letters instead of "words" here! D:
        for y in xrange(point_1[1], point_2[1]):
            for element in xrange(y * self.sizes[0] + point_1[0],
                                  y * self.sizes[0] + point_2[0]):
                self.grid[element] = operation(self.grid[element])

    def parse_instruction_file(self, file_name):
        with open(file_name) as input_file:
            instructions = input_file.read().splitlines()
            self.follow_instructions(instructions)

    def follow_instructions(self, instructions):  # I don't like that it copied the whole "instructions"
        for instruction in instructions:
            self.follow_instruction(instruction)

    def follow_instruction(self, instruction):
        parsed_instruction = parse_instruction(instruction)
        operation = choose_command(parsed_instruction[0])
        coordinates = (parsed_instruction[1], parsed_instruction[2])
        self.edit_square(coordinates, operation)

    def count_lit(self):
        lit_count = 0
        for element in self.grid:
            lit_count += element
        print lit_count


def parse_instruction(string):  # TODO: add some more format checks (?)
    #  turn off 660,55 through 986,197
    #  toggle 537,781 through 687,941
    #  turn on 226,196 through 599,390 TODO: use "try - except" here
    instruction = string.split(" ")
    if instruction[0] == 'toggle':
        return pack_instruction(instruction, ONE_WORD)  # Command is one word long
    elif instruction[0] == 'turn':
        return pack_instruction(instruction, TWO_WORDS)  # Command is two words long
    else:
        print 'Wrong file format.'


def pack_instruction(instruction, command_word_count):
    command = instruction[command_word_count + COMMAND_SHIFT_1]
    point_1 = [int(number) for number
               in instruction[command_word_count].split(',')]
    point_2 = [int(number) for number
               in instruction[command_word_count + COMMAND_SHIFT_2].split(',')]
    return command, point_1, point_2


def choose_command(command):
    if command == 'on':
        return true_stub
    elif command == 'off':
        return false_stub
    else:
        return toggle


def toggle(bool_element):
    return not bool_element


def false_stub(some_element):
    return False


def true_stub(some_element):
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_name')
    args = parser.parse_args()
    grid = LightGrid()
    grid.parse_instruction_file(args.file_name)
    grid.count_lit()


if __name__ == '__main__':
    main()