import sys
import argparse


TYPE = (
    'SILVER',
    'GOLD'
)


class Santa(object):
    def __init__(self, task_type=TYPE[0]):
        self.task_type = task_type
        self.directions_taken = 0
        self.location = 0

    def do_the_job(self, file_path):
        directions = parse_input_file(file_path)
        return self.follow_directions(directions)

    def follow_directions(self, directions):
        if self.task_type == TYPE[0]:
            return self.follow_directions_silver(directions)
        elif self.task_type == TYPE[1]:
            return self.follow_directions_gold(directions)
        else:
            sys.exit('Wrong task type. Please use "GOLD" or "SILVER".')

    def follow_directions_silver(self, directions):
        for direction in directions:
            self.follow_direction(direction)
        return self.location

    def follow_directions_gold(self, directions):
        for direction in directions:
            self.follow_direction(direction)
            if self.check_cellar():
                return self.directions_taken
        return -1

    def follow_direction(self, direction):
        self.directions_taken += 1
        if direction == '(':
            self.location += 1
        elif direction == ')':
            self.location -= 1
        else:
            print 'Some symbols are not parentheses, they will be ignored.'

    def check_cellar(self):
        if self.location < 0:
            return self.directions_taken


def parse_input_file(file_path):
    with open(file_path, 'r') as input_file:
        return input_file.read().strip("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_path', default='')
    parser.add_argument('-t', action='store', dest='task_type', default='SILVER')
    args = parser.parse_args()
    santa = Santa(args.task_type)
    print santa.do_the_job(args.file_path)


if __name__ == '__main__':
    main()

