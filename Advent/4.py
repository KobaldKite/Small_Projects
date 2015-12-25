import hashlib
import argparse


class SecretKey:
    def __init__(self, key):
        self.key = key

    def get_hash(self, number):
        string_in_question = ''.join([self.key, str(number)])
        h = hashlib.md5()
        h.update(string_in_question)
        return h.hexdigest()

    def find_number(self):
        number = 1
        while number:
            md5_hash = self.get_hash(number)
            print md5_hash
            if md5_hash < 0x00000fffffffffffffffffffffffffff:
                print md5_hash
                print number
                break
            number += 1


def main(args):
    k = SecretKey(args.input_key)
    k.find_number()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', action='store', dest='input_key')
    arguments = parser.parse_args()
    main(arguments)
