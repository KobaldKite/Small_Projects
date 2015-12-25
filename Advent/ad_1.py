import argparse


TYPE = [
    'SILVER',
    'GOLD'
]


class Santa(object):
    def __init__(self, args):
        self.task_type = args.task_type
        self.file_path = args.file_path  # Move it out of here?
        self.directions_taken = 0
        self.location = 0
        self.directions = self.get_directions_from_file()

    def get_directions_from_file(self):
        with open(self.file_path, 'r') as input_file:
            return input_file.read().strip("\n")

    def follow_directions(self):
        if self.task_type == 'SILVER':
            self.follow_directions_silver()
        elif self.task_type == 'GOLD':
            self.follow_directions_gold()
        else:
            print "Wrong task type! Please use either 'SILVER' or 'GOLD'!"

    def follow_directions_silver(self):
        for direction in self.directions:
            self.follow_direction(direction)

    def follow_directions_gold(self):
        for direction in self.directions:
            self.follow_direction(direction)
            if self.check_cellar():
                break

    def follow_direction(self, direction):
        self.directions_taken += 1
        if direction == '(':
            self.location += 1
        elif direction == ')':
            self.location -= 1
        else:
            print 'Some symbols are not parentheses!'

    def check_cellar(self):
        if self.location < 0:
            print self.directions_taken
            return self.directions_taken


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_path', default='')
    parser.add_argument('-t', action='store', dest='task_type', default='SILVER')
    args = parser.parse_args()
    santa = Santa(args)
    santa.follow_directions()


if __name__ == '__main__':  # TESTED AND WORKS
    main()

