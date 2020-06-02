import xml.etree.ElementTree as ET, collections
from Homework_task_1 import top_word_counter

def get_info(file_path) -> list:
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    xml_items = root.findall("channel/item")

    news_lists = []

    for item in xml_items:
        news_lists.append(item.find('description').text.split())

    return news_lists

if __name__ == '__main__':
    top_word_counter(10)
