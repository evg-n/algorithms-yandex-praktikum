"""
-- ПРИНЦИП РАБОТЫ --

    1. Создание поискового индекса на основе считанных документов.
    Поисковый индекс в нашей задаче - это просто вложенная хеш-таблица, в
    которой хранятся записи о том, в каких документах и сколько раз встречалось
    каждое уникальное слово, которое мы встретили при обработке документов.

    Используем встроенную структуру данных Counter из стандартной библиотеки
    для повышения наглядности и удобства, можно было бы обойтись обычной
    хеш-таблицей для подсчета статистики вхождений различных слов в запросе.

    Обходим в циклах каждое слово каждого документа, сохраняем в index нужную
    информацию о статистике. Наш индекс имеет следующий вид:

    {
        word_1: {
            document_1: 3,
            document_3: 6,
            document_2: 1,
        },
        word_2: {
            document_5: 30,
            document_4: 16,
        },
        ...
    }

    2. Обработка запросов.
    Для каждого уникального слова из запроса, мы собираем все данные о том, в
    каких документах и сполько раз встречалось встречалось слово в одну общую
    хеш-таблицу результатов для запроса. Такая хеш-таблица будет иметь вид:

    {
        document_1: 3,
        document_3: 61,
        document_5: 40,
        document_2: 26,
        document_4: 4
    }

    Затем, мы выполняем сортировку этой хеш-таблицы сперва по убыванию значения,
    затем по возрастанию индекса документа, если значения совпадают.
    Из результатов сортировки выбираются 5 первых элементов - это и есть ответ.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    Создание индекса:
    O(n), обходим каждое слово в каждом документе O(n), ведя учет вхождений и
    записывая результаты в структуру данных index O(1).

    Обработка запроса:
    O(m * n * s), где
        m - число запросов,
        n - число документов. Мы должны посмотреть, сколько раз каждое слово
        из запроса встречается в каждом документе.
        Второй проход по числу документов нужен для отбора 5 самых 
        релевантных документов с помощью heapq.nlargest()

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Поисковой индекс - это словарь словарей, где ключи - все слова во всех
    документах (W), а значения - словари из n ключей (количество данного слова в каждом из n документов). 
    Получается  O(W*n).

    Обработка запросов:
    O(m), здесь дополнительная память используется для:
    - Хранения уже встреченных слов текущего запроса (по задаче есть требование
    уникальности),
    - Хранение хеш-таблицы со статистикой вхождений в документы по каждому
    запросу. Затраты на этот шаг зависят от того, сколько документов содержат
    данное слово запроса.
"""
from collections import defaultdict, Counter
from heapq import nlargest
from typing import List


def build_index(docs: List[str]):
    index = defaultdict(dict)
    for doc_id, doc in enumerate(docs, start=1):  # document id starts from 1
        for word, occ_count in Counter(doc.split()).items():
            index[word][doc_id] = occ_count
    return index


def process_queries(query: str, index, limit: int = 5):
    seen_words = {}
    query_words_stat = defaultdict(int)

    for word in query.split():
        if word not in seen_words:
            if word in index:
                # for every unique query word we save every document id and
                # number of word's occurences in that document in the hashmap
                for doc_id, count in index[word].items():
                    query_words_stat[doc_id] += count
            seen_words[word] = True

    # traverse through the hashmap and pick 5 largest results based on:
    # 1) number of occurences
    # 2) negative doc_id (in case occurences are the same)
    most_common = nlargest(
        5,
        query_words_stat.items(),
        key=lambda item: (item[1], -item[0]),
    )
    # pick only document ids
    return map(lambda item: item[0], most_common)


def main():
    n = int(input())
    documents = []
    for _ in range(n):
        documents.append(input())
    index = build_index(documents)

    m = int(input())
    for _ in range(m):
        query = input()
        result_relevancy = process_queries(query, index)
        print(" ".join(map(str, result_relevancy)))


if __name__ == "__main__":
    main()
