import urllib
import json
import io
import collections


def data_from_source(method, address):
    if method == 'url':
        return urllib.urlopen(address)
    elif method == 'path':
        return io.open(address)
    else:
        raise ValueError('Wrong source fetch method!')


def get_district_list(method='url', address='http://python.aori.ru/data/technical_education_moscow.json'):
    response = data_from_source(method, address)
    edu_data = json.load(response)
    return [element.get('Cells').get('okrug') for element in edu_data]


def select_most_common(district_list, most_common_count=5):
    """
    If several districts are tied for the 5th position,
    only one of them is shown.
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