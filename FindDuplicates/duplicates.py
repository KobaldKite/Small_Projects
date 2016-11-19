import argparse
import os


def compose_file_catalogue(path):
    """
    Scans a  given folder to create a dictionary of files,
    where keys are unique pairs of file attributes (name and size),
    while values are lists of paths to files with such name-size pairs.
    :returns dictionary of files
    """
    file_catalogue = {}
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_record = get_file_attributes(file_path, file_name)
            if file_record not in file_catalogue:
                file_catalogue[file_record] = [file_path, ]
            else:
                file_catalogue[file_record].append(file_path)
    return file_catalogue


def extract_duplicate_list(file_catalogue):
    """
    From file list only keeps records that have multiple file paths,
    and returns them as a list that is convenient to work with.
    :returns list of (name, size, paths[])
    """
    acceptable_amount = 1
    duplicate_records = list(filter(lambda record:
                                    len(file_catalogue[record]) > acceptable_amount,
                                    file_catalogue))
    for record in duplicate_records:
        file_name, file_size = record
        yield file_name, file_size, file_catalogue[record]


def get_file_attributes(file_path, file_name=None):
    """
    Gets name and size of a file, the two attributes that are used
    to tell unique files from duplicates.
    :returns name, size
    """
    if file_name is None:
        file_name = os.path.basename(file_path)
    if not os.path.exists(file_path):  # Protection against broken links
        return None
    file_size = os.path.getsize(file_path)
    return file_name, file_size


def print_duplicates(duplicate_list):
    for duplicate in duplicate_list:
        file_name, file_size, file_paths = duplicate
        first_string = 'File {} size of {} bytes encountered {} times:'\
            .format(file_name, file_size, len(file_paths))
        print(first_string)
        for duplicate_path in file_paths:
            print(duplicate_path)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', action='store',
                        help='path to the folder you want to scan for duplicates')
    return parser.parse_args()


if __name__ == '__main__':
    arguments = parse_arguments()
    files = compose_file_catalogue(arguments.path)
    duplicates = extract_duplicate_list(files)
    print_duplicates(duplicates)