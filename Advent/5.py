import argparse


def main(args):
    with open(args.file_name, 'r') as input_file:
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_name')
    arguments = parser.parse_args()
    main(arguments)