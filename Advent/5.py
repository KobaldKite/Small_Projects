import argparse


BAD_SUBSTRINGS = ('ab', 'cd', 'pq', 'xy')
VOWELS = ('a', 'e', 'i', 'o', 'u')


def file_analyze(filename):
    with open(filename, 'r') as input_file:
        nice_count = 0
        for line in input_file:
            nice_count += full_check_silver(line)
            print '----'
        print 'There is %d nice strings.' % nice_count


def full_check_silver(string):
    if (check_enough_vowels(string) or
       check_bad_substrings(string) or
       check_double_letters(string)):
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


def main():
    # Change the string to a lower case just in case.
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_name')
    args = parser.parse_args()
    file_analyze(args.file_name)


if __name__ == '__main__':
    main()