import sys
import argparse


TYPE = (
    'SILVER',
    'GOLD'
)


def parse_size_file(file_path):
    with open(file_path, 'r') as input_file:
        string_list = input_file.read().strip('\n').split('\n')
        try:
            sizes_list = [[int(size) for size in line.split('x')] for line in string_list]
        except ValueError:
            print 'Not possible to convert data to integer!'
            return -1
        else:
            return sizes_list


def wrap_boxes(size_list, task_type=TYPE[0]):
    """
    The only function user really needs to use.
    Calculates the required material depending on the list os sizes and type of wrapping.
    :param size_list: three-dimensional vector
    :param task_type: SILVER for paper, GOLD for ribbon and bow
    :return: the amount of material needed
    """
    material = 0
    try:
        for sizes in size_list:
            material += wrap_function(sizes, task_type)
    except TypeError:
        print 'Not possible to process data!'
        return -1
    return material


def wrap_function(sizes, task_type=TYPE[0]):
    if check_negative(sizes) == -1:
        return 0
    if task_type == TYPE[0]:
        return wrap_paper(sizes)
    elif task_type == TYPE[1]:
        return wrap_ribbon(sizes)
    else:
        sys.exit('Wrong task type. Please use "GOLD" or "SILVER".')


def check_negative(sizes):
    for size in sizes:
        if size <= 0:
            print 'Some dimensions are not natural numbers. Such boxes will be ignored.'
            return -1
    return 0


def wrap_paper(sizes):
    sides = [sizes[0] * sizes[1],
             sizes[0] * sizes[2],
             sizes[1] * sizes[2]]
    result = sum([2 * side for side in sides]) + min(sides)
    return result


def wrap_ribbon(sizes):
    wrap = 2 * (sum(sizes) - max(sizes))
    bow = 1
    for size in sizes:
        bow *= size
    result = wrap + bow
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='file_path')
    parser.add_argument('-t', action='store', dest='task_type', default='SILVER')
    args = parser.parse_args()
    sizes_list = parse_size_file(args.file_path)
    print wrap_boxes(sizes_list, args.task_type)


if __name__ == '__main__':
    main()
