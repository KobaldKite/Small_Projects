import subprocess
import argparse

SORT_METHODS = [
    'honest',
    'cheat'
]


class Sorter(object):
    def __init__(self, directory, method):
        self.directory = directory
        self.method = method

    def filter_files(self):
        raw_ls_data = self.get_files()
        ls_data_list = raw_ls_data.splitlines()
        file_data_list = []
        for item in ls_data_list[1:]:
            if item[0] != 'd':
                item = item.split()
                file_data_list.append(item)
        return file_data_list

    def get_files(self):
        arguments = '-la' if (self.method == SORT_METHODS[0]) else '-laS'
        return subprocess.check_output(['ls', arguments, self.directory])

    def sort_files(self):
        sorted_ls_files = []
        ls_files = self.filter_files()
        if self.method == SORT_METHODS[0]:
            ls_files.sort(key=lambda elem: int(elem[4]), reverse=True)
            for item in ls_files:
                sorted_ls_files.append(' '.join(item))
            return sorted_ls_files
        elif self.method == SORT_METHODS[1]:
                return ls_files
        else:
            print "Wrong argument. Please use 'honest' or 'cheat'."
            return -1


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store', dest='directory', default='/')
    parser.add_argument('-m', action='store', dest='method', default='honest')
    return parser.parse_args()


def main():
    arguments = parse_arguments()
    sorter = Sorter(arguments.directory, arguments.method)
    print sorter.sort_files()


if __name__ == '__main__':
    main()