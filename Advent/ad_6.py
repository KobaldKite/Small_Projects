import sys
import argparse


ONE_WORD = 1
TWO_WORDS = 2
COMMAND_SHIFT_1 = -1
COMMAND_SHIFT_2 = 2
GRID_SHIFT = 1
GRID_HEIGHT = 1000
GRID_WIDTH = 1000

TASK_TYPE = (
    'SILVER',
    'GOLD'
)

COMMAND = (
    'on',
    'off',
    'toggle'
)


class LightGrid(object):
    def __init__(self, task_type=TASK_TYPE[0], sizes=(GRID_HEIGHT, GRID_WIDTH)):
        self.sizes = sizes
        self.grid = [False] * sizes[0] * sizes[1]  # Everything is turned off
        if task_type == TASK_TYPE[0]:
            self.choose_command = choose_command_silver
        elif task_type == TASK_TYPE[1]:
            self.choose_command = choose_command_gold
        else:
            sys.exit('Wrong task type. Please use "GOLD" or "SILVER".')

    def edit_square(self, coordinates, operation):
        # Coordinates have ((x, y), (x, y)) format
        point_1, point_2 = coordinates
        for y in xrange(point_1[1], point_2[1] + GRID_SHIFT):
            for element in xrange(y * self.sizes[0] + point_1[0],
                                  y * self.sizes[0] + point_2[0] + GRID_SHIFT):
                self.grid[element] = operation(self.grid[element])

    def parse_input_file(self, file_name):
        with open(file_name) as input_file:
            instructions = input_file.read().splitlines()
            self.follow_instructions(instructions)

    def follow_instructions(self, instructions):  # I don't like that it copied the whole "instructions"
        for instruction in instructions:
            self.follow_instruction(instruction)

    def follow_instruction(self, instruction):
        parsed_instruction = parse_instruction(instruction)
        operation = self.choose_command(parsed_instruction[0])
        coordinates = (parsed_instruction[1], parsed_instruction[2])
        self.edit_square(coordinates, operation)

    def count_lit(self):
        lit_count = 0
        for element in self.grid:
            lit_count += element
        return lit_count


def parse_instruction(string):  # TODO: use "try - except" here
    instruction = string.split(" ")
    if instruction[0] == 'toggle':
        return pack_instruction(instruction, ONE_WORD)  # Command is one word long
    elif instruction[0] == 'turn':
        return pack_instruction(instruction, TWO_WORDS)  # Command is two words long
    else:
        sys.exit('Wrong file format.')


def pack_instruction(instruction, command_word_count):
    command = instruction[command_word_count + COMMAND_SHIFT_1]
    point_1 = [int(number) for number
               in instruction[command_word_count].split(',')]
    point_2 = [int(number) for number
               in instruction[command_word_count + COMMAND_SHIFT_2].split(',')]
    return command, point_1, point_2


def choose_command_silver(command):
    if command == 'on':
        return on_silver
    elif command == 'off':
        return off_silver
    elif command == 'toggle':
        return toggle_silver
    else:
        sys.exit('Wrong file format.')


def choose_command_gold(command):  # TODO: repetition! Such repetition!
    if command == 'on':
        return on_gold
    elif command == 'off':
        return off_gold
    elif command == 'toggle':
        return toggle_gold
    else:
        sys.exit('Wrong file format.')


def toggle_silver(bool_element):
    return not bool_element


def off_silver(stub):
    return False


def on_silver(stub):
    return True


def toggle_gold(brightness):
    return brightness + 2


def off_gold(brightness):
    return 0 if brightness < 2 else brightness - 1


def on_gold(brightness):
    return brightness + 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_name')
    parser.add_argument('-t', action='store', dest='task_type')
    args = parser.parse_args()
    grid = LightGrid(args.task_type)
    grid.parse_instruction_file(args.file_name)
    print grid.count_lit()


if __name__ == '__main__':
    main()