import json, xml.etree.ElementTree as ET, collections
from collections import Counter

def get_info_json(file_path) -> list:

    with open(file_path, encoding='utf8') as read_file:
        data = json.load(read_file)

    news_lists = []

    for value_list in data['rss']['channel']['items']:
        news_lists.append(value_list['description'].split())

    return news_lists

def get_info_xml(file_path) -> list:
    
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    xml_items = root.findall("channel/item")

    news_lists = []

    for item in xml_items:
        news_lists.append(item.find('description').text.split())

    return news_lists


def top_word_counter(function, file_path, top_figure: int) -> str:

    news_lists = function(file_path)
    news_lists_word_lower = []
    
    c = collections.Counter()

    for list_of_item in news_lists:
        for word in list_of_item:
            if word.istitle():
                lower_word = word.lower()
                news_lists_word_lower.append(lower_word)
            else:
                news_lists_word_lower.append(word)

    for word in news_lists_word_lower:
        if len(word) > 6:
            c[word] += 1

    top_list_lower = Counter(c).most_common(top_figure)

    print(f'\nСписок {top_figure} наиболее часто употребляемых слов:')

    for word_count_item in top_list_lower:
        print(f'{top_list_lower.index(word_count_item) + 1} место у слова "{word_count_item[0]}" количество повторений равняется {word_count_item[-1]}')


if __name__ == '__main__':
    top_word_counter(get_info_xml, 'newsafr.xml', 10)
    top_word_counter(get_info_json, 'newsafr.json', 10)