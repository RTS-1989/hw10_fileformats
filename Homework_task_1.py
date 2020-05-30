import json, collections
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

def top_word_counter() -> str:

    news_lists = get_info('newsafr.json')

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
