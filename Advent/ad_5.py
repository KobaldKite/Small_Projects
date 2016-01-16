import argparse


BAD_SUBSTRINGS = ('ab', 'cd', 'pq', 'xy')
VOWELS = ('a', 'e', 'i', 'o', 'u')
STRING_SHIFT = 1

TASK_TYPE = (
    'SILVER',
    'GOLD'
)


def file_analyze(filename, task_type):
    with open(filename, 'r') as input_file:  # TODO: Wouldn't it be better to read files separately?
        nice_count = 0
        if task_type == TASK_TYPE[0]:
            for line in input_file:
                nice_count += full_check_silver(line)
        elif task_type == TASK_TYPE[1]:
            for line in input_file:
                nice_count += full_check_gold(line)
        else:
            print "Wrong task type! Please use either 'SILVER' or 'GOLD'!"
        print 'There is %d nice strings.' % nice_count


def full_check_silver(string):
    if (check_enough_vowels(string) or
       check_bad_substrings(string) or
       check_double_letters(string)):
        return 0
    return 1  # Nice


def full_check_gold(string):
    if (check_duplicates(string) or
       check_enclosing(string)):
        return 0
    return 1  # Nice


def check_enough_vowels(string, vowel_count=3):
    count = 0
    for vowel in VOWELS:
        count += string.count(vowel)
    if count < vowel_count:
        return 1  # Naughty
    return 0


def check_bad_substrings(string):
    for substring in BAD_SUBSTRINGS:
        if string.find(substring) != -1:
            return 1  # Naughty
    return 0


def check_double_letters(string):
    string_length = len(string)
    for count in xrange(1, string_length):
        if string[count - 1] == string[count]:
            return 0
    return 1  # Naughty


def check_duplicates(string, duplicate_length=2):
    for i in xrange(len(string) - duplicate_length + STRING_SHIFT):
        sample = string[i:i + duplicate_length]
        rest = string[i + duplicate_length:]
        if rest.find(sample) != -1:
            return 0
    return 1  # Naughty


def check_enclosing(string, enclosure_length=1):
    for i in xrange(len(string) - enclosure_length - STRING_SHIFT):
        if string[i] == string[i + enclosure_length + STRING_SHIFT]:
            return 0
    return 1  # Naughty


def main():
    # Change the string to a lower case just in case.
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_name')
    parser.add_argument('-t', action='store', dest='task_type', default='SILVER')
    args = parser.parse_args()
    file_analyze(args.file_name, args.task_type)


if __name__ == '__main__':  # TESTED AND WORKS
    main()
