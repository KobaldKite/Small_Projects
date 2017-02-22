import argparse

TEST_CONTENT = '\
123 -> x\n\
456 -> y\n\
x AND y -> d\n\
x OR y -> e\n\
x LSHIFT 2 -> f\n\
y RSHIFT 2 -> g\n\
NOT x -> h\n\
NOT y -> i\n\
'


def write_test_file():
    with open('test_7', 'w') as test_file:
        test_file.write(TEST_CONTENT)


def parse_input_file():
    pass


class Instruction(object):
    def __init__(self, string):
        self.operator = 0
        self.sources = [0]    # List in case of binary operators
        self.destination = 0  #
        self.value = 0        # Numerical values for binary shifts and starting signals

    def check_not(self, words):
        if words[0] == 'NOT':
            self.operator = 'NOT'
            self.sources = [words[1], ]
            self.destination = words[3]
            return 0
        return 1

    def check_and_or(self, words):
        if words[1] in ['AND', 'OR']:
            self.operator = words[1]
            self.sources = [words[0], words[2]]
            self.destination = words[4]
            return 0
        return 1

    def check_shift(self, words):
        if words[1] in ['LSHIFT', 'RSHIFT']:
            self.operator = words[1]
            self.sources = [words[0], ]
            self.destination = words[4]
            self.value = words[2]
            return 0
        return 1

    def check_straight(self, words):
        if words[1] == '->':
            self.operator = 'STRAIGHT'
            self.sources = [words[0], ]
            self.destination = words[2]
            return 0
        return 1

    def parse_string(self, string):
        """
        Check the second word!!!
        :return:
        """
        words = string.split()
        if self.check_shift(words):
            if self.check_and_or(words):
                if self.check_not(words):
                    if self.check_straight(words):
                        print 'Wrong instruction format!'
                        return 1
        return 0


class Circuit(object):
    pass