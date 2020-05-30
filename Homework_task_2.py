import xml.etree.ElementTree as ET, collections
from collections import Counter

def get_info(file_path) -> list:
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    xml_items = root.findall("channel/item")

    news_lists = []

    for item in xml_items:
        news_lists.append(item.find('description').text.split())

    return news_lists

def top_word_counter() -> str:

    news_lists = get_info("newsafr.xml")

    c = collections.Counter()

    for list_of_item in news_lists:
        for word in list_of_item:
            if len(word) > 6:
                c[word] += 1

    a = Counter(c).most_common(10)

    print('Список 10 наиболее часто употребляемых слов:')

    for word_count_item in a:
        print(f'{a.index(word_count_item) + 1} место у слова "{word_count_item[0]}" количество повторений равняется {word_count_item[-1]}')

if __name__ == '__main__':
    top_word_counter()
