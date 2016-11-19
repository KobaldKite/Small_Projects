import argparse
import os
from PIL import Image


def solve_proportion(orig_1, orig_2, new_1):
    """
    The equation is the following:
    orig_1 / orig_2 = new_1 / new_2
    """
    return new_1 / orig_1 * orig_2


def scale_size(orig, coefficient):
    return [dimension * coefficient for dimension in orig]


def check_proportion_consistency(orig_1, orig_2, new_1, new_2):
    """
    Checks whether image proportions are going to stay the same.
    """
    return abs(solve_proportion(orig_1, orig_2, new_1) / new_2 - 1) < 0.02


def calculate_new_size(orig_width, orig_height, new_width, new_height, scale):
    if scale is not None:
        new_size = scale_size((orig_width, orig_height), scale)
    elif new_width is not None and new_height is not None:
        new_size = (new_width, new_height)
    elif new_height is not None:
        new_size = (solve_proportion(orig_height, orig_width, new_height), new_height)
    elif new_width is not None:
        new_size = (new_width, solve_proportion(orig_width, orig_height, new_width))
    else:
        new_size = None
    if new_size is not None:
        new_size = [round(dimension) for dimension in new_size]
    return new_size


def resize_image(image, new_sizes):
    return image.resize(new_sizes)


def save_image(image, path_to_output):
    image.save(path_to_output)


def load_image(path_to_original):
    if os.path.exists(path_to_original):
        return Image.open(path_to_original)
    return None


def read_argument(argument, argument_type):
    """
    Checks if user input is correct (positive integers for sizes, positive float for scale).
    """
    if argument is None:
        return None
    return check_argument_sign(adjust_argument_type(argument, argument_type))


def adjust_argument_type(argument, argument_type):
    """
    Converts arguments to the right type.
    If it's impossible to convert argument to the required type,
    raises an error and sends it higher up for handling.
    """
    try:
        return argument_type(argument)
    except (ValueError, TypeError):
        raise


def check_argument_sign(argument):
    """
    Makes sure scale and sizes are positive.
    """
    if argument > 0:
        return argument
    raise ValueError


def generate_filename(path, width, height):
    name, extension = os.path.basename(path).split('.')
    return '{}__{}x{}.{}'.format(name, str(width), str(height), extension)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', action='store',
                        help='path to the original file')
    parser.add_argument('--output_path', action='store', dest='output_path',
                        help='path to the output file')
    parser.add_argument('--width', action='store', dest='width',
                        help='desired width of the result image')
    parser.add_argument('--height', action='store', dest='height',
                        help='desired height of the result image')
    parser.add_argument('--scale', action='store', dest='scale',
                        help='scale for image resizing keeping current proportions')
    return parser.parse_args()

if __name__ == '__main__':
    arguments = parse_arguments()

    # Load an image, get its size from it.
    path = arguments.path
    image = load_image(path)
    if image is None:
        print('There is no existing file with the path you provided.\n')
        raise SystemExit
    orig_width, orig_height = image.size

    # Read user input
    try:
        new_width = read_argument(arguments.width, int)
        new_height = read_argument(arguments.height, int)
        scale = read_argument(arguments.scale, float)
    except:
        print('Width and height must be positive integers. Scale must be a positive float.\n')
        raise SystemExit

    # Calculate sizes of the resulting image
    new_sizes = calculate_new_size(orig_width, orig_height, new_width, new_height, scale)
    width_index = 0
    height_index = 1
    if (arguments.scale is not None) and (new_width is not None or new_height is not None):
        print('Both scale and absolute sizes are given. Absolute sizes will be ignored.\n')
    elif not check_proportion_consistency(orig_width, orig_height,
                                          new_sizes[width_index], new_sizes[height_index]):
        print('Image proportions won\'t be preserved.\n')

    # Generate path to the resulting image (if necessary), write the image to file
    output_path = arguments.output_path
    if output_path is None:
        output_path = generate_filename(path, new_sizes[width_index], new_sizes[height_index])
    new_image = resize_image(image, new_sizes)
    save_image(new_image, output_path)
