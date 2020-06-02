import json
import collections
from collections import Counter

def get_info(file_path) -> list:

    with open('newsafr.json', encoding='utf8') as read_file:
        data = json.load(read_file)

    news_lists = []

    for item in data.values():
        if item['channel']:
            for key, value in item['channel'].items():
                if key == 'items':
                    for info_dict in value:
                        for key, value in info_dict.items():
                            if key == 'description':
                                news_lists.append(value.split())

    return news_lists

def top_word_counter(top_figure: int) -> str:

    news_lists = get_info('newsafr.json')

    c = collections.Counter()
    d = collections.Counter()

    for list_of_item in news_lists:
        for word in list_of_item:
            if len(word) > 6:
                if word.islower():
                    c[word] += 1
                elif word.istitle():
                    d[word] += 1

    top_list_lower = Counter(c).most_common(top_figure)
    top_list_title = Counter(d).most_common(top_figure)

    print(f'Список {top_figure} наиболее часто употребляемых слов с маленькой буквы:')

    for word_count_item in top_list_lower:
        print(f'{top_list_lower.index(word_count_item) + 1} место у слова "{word_count_item[0]}" количество повторений равняется {word_count_item[-1]}')

    print(f'\nСписок {top_figure} наиболее часто употребляемых слов с большой буквы:')

    for word_count_item in top_list_title:
        print(f'{top_list_title.index(word_count_item) + 1} место у слова "{word_count_item[0]}" количество повторений равняется {word_count_item[-1]}')

if __name__ == '__main__':
    top_word_counter(10)

# import xml.etree.ElementTree as ET, collections
# from Homework_task_1 import top_word_counter

# def get_info(file_path) -> list:
#     parser = ET.XMLParser(encoding="utf-8")
#     tree = ET.parse("newsafr.xml", parser)
#     root = tree.getroot()
#     xml_items = root.findall("channel/item")

#     news_lists = []

#     for item in xml_items:
#         news_lists.append(item.find('description').text.split())

#     return news_lists

# if __name__ == '__main__':
#     top_word_counter(10)