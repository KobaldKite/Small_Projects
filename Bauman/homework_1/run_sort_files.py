import subprocess
import argparse
import os

SORT_METHODS = [
    'honest',
    'cheat'
]

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_files(directory, method):
    arguments = '-la' if (method == SORT_METHODS[0]) else '-laS'
    return subprocess.check_output(['ls', arguments, directory])


def filter_files(directory, method):
    """
    First, the directories got by '-ls' are ignored;
    then, the result strings are divided into lists
    :return: list (elements are files) of lists (elements are file properties, e.g. size, name, etc.)
    """
    raw_ls_data = get_files(directory, method)
    ls_data_list = raw_ls_data.splitlines()
    file_data_list = []
    for item in ls_data_list[1:]:
        if item[0] != 'd':
            item = item.split()
            file_data_list.append(item)
    return file_data_list


def sort_files(directory=CURRENT_DIR, method=SORT_METHODS[0]):
    """
    :param directory: path to the directory, files in which need to be shown in size order
    :param method: either 'honest' or 'cheat'; 'honest' uses program sort, 'cheat' uses system sort
    :return: if 'honest': a list of strings, where each string contains full info on each file
             if 'cheat': a list of lists, where each inner list
                         contains full set of file parameters as strings
    """
    sorted_ls_files = []
    ls_files = filter_files(directory, method)
    if method == SORT_METHODS[0]:
        ls_files.sort(key=lambda elem: int(elem[4]), reverse=True)
        for item in ls_files:
            sorted_ls_files.append(' '.join(item))
        return sorted_ls_files
    elif method == SORT_METHODS[1]:
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
    print sort_files(arguments.directory, arguments.method)


if __name__ == '__main__':
    main()