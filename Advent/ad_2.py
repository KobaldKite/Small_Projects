import argparse


TYPE = (
    'SILVER',
    'GOLD'
)


def wrap_boxes(args):  # TODO: wouldn't it be better to read everything and work with it later?
    wrap_function = wrap_manager(args.task_type)
    with open(args.file_path, 'r') as input_file:
        material = 0
        for line in input_file:
            sizes = [int(size) for size in line.split('x')]
            material += wrap_function(sizes)
    print material


def wrap_manager(task_type):
    if task_type == TYPE[0]:
        return wrap_paper
    elif task_type == TYPE[1]:
        return wrap_ribbon
    else:
        print 'Wrong task type. Please use "GOLD" or "SILVER".'
        # Throw some error!
        return sum  # A bad stub


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
    wrap_boxes(args)


if __name__ == '__main__':  # TESTED AND WORKS
    main()
