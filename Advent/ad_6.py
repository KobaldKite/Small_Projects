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
        point_1, point_2 = coordinates
        for y in xrange(point_1[1], point_2[1]):
            for element in xrange(y * self.sizes[0] + point_1[0],
                                  y * self.sizes[0] + point_2[0]):
                self.grid[element] = operation(self.grid[element])

    def follow_instructions(self, instructions):
        pass

    def follow_instruction(self, instruction):
        operation = choose_command(instruction[0])
        coordinates = (instruction[1], instruction[2])
        self.edit_square(coordinates, operation)


def parse_instruction(string):  # TODO: add some more format checks (?)
    #  turn off 660,55 through 986,197
    #  toggle 537,781 through 687,941
    #  turn on 226,196 through 599,390
    instruction = string.split()
    if instruction[0] == 'toggle':
        pack_instruction(instruction, ONE_WORD)  # Command is one word long
    elif instruction[0] == 'turn':
        pack_instruction(instruction, TWO_WORDS)  # Command is two words long
    else:
        print 'Wrong file format.'


def pack_instruction(instruction, command_word_count):  # TODO: dispose of these magic numbers!
    command = instruction[command_word_count + COMMAND_SHIFT_1]
    point_1 = [int(number) for number in instruction[command_word_count]]
    point_2 = [int(number) for number in instruction[command_word_count + COMMAND_SHIFT_2]]
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


def read_file(file_path):
    with open(file_path) as input_file:
        pass  # Read all the lines into a tuple


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_name')
    args = parser.parse_args()


if __name__ == '__main__':
    main()