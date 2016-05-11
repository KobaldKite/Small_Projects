import urllib
import json
import io
import collections

ACCESS_METHODS = [
    'url',
    'path'
]


def data_from_source(method, address):
    if method == ACCESS_METHODS[0]:
        return urllib.urlopen(address)
    elif method == ACCESS_METHODS[1]:
        return io.open(address)
    else:
        raise ValueError('Wrong source fetch method!')


def get_district_list(method='url', address='http://python.aori.ru/data/technical_education_moscow.json'):
    """
    :param method: either 'url' or 'path'; defines how the data is accessed
    :param address: either url or path to a file with data
    :return: list of districts read from the aforementioned source
    """
    response = data_from_source(method, address)
    edu_data = json.load(response)
    return [element.get('Cells').get('okrug') for element in edu_data]


def select_most_common(district_list, most_common_count=5):
    """
    If several districts are tied for several positions, some districts are not shown.
    (If there are three districts of the same rarity,
    competing for two last positions, for example.)
    The shown elements are chosen based on alphabetical order,
    e.g. 'Alaska' is chosen before 'Texas'.
    """
    district_count = collections.Counter(district_list)
    return [element[0] for element in district_count.most_common(most_common_count)]


def main():
    district_list = get_district_list()
    district_most_common = select_most_common(district_list)
    for element in district_most_common:
        print element


if __name__ == '__main__':
    main()