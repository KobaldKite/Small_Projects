import urllib
import json
import collections


def get_okrug_list():
    response = urllib.urlopen('http://python.aori.ru/data/technical_education_moscow.json')
    edu_data = json.load(response)
    return [element.get('Cells').get('okrug') for element in edu_data]


def select_most_common(okrug_list):
    """
    If several okrugs are tied for the 5th position,
    only one of them is shown.
    """
    okrug_count = collections.Counter(okrug_list)
    return [element[0] for element in okrug_count.most_common(5)]


def main():
    okrug_list = get_okrug_list()
    okrug_most_common = select_most_common(okrug_list)
    for element in okrug_most_common:
        print element


if __name__ == '__main__':
    main()