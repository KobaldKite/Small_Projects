import argparse


def validate(password):
    upper, lower, digit, symbol = False, False, False, False
    letter_count = 0
    for letter in password:
        if not upper:
            upper = letter.isupper()
        if not lower:
            lower = letter.islower()
        if not digit:
            digit = letter.isdigit()
        if not symbol:
            symbol = letter in ('@', '?', '#', '$', '%', '&', '*', '_', '-')
        if letter_count < 8:
            letter_count += 1
        if upper and lower and digit and symbol and (letter_count == 8):
            return True
    return False


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store', dest='password', default='')
    return parser.parse_args()


def main():
    arguments = parse_arguments()
    print validate(arguments.password)


if __name__ == '__main__':
    main()
