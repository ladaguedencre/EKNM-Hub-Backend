from dataclasses import dataclass
from typing import List
from common import common_db


@dataclass
class Binding:
    id: str
    title: str
    subtitle: str
    author: str
    date: str
    category: str

    def __init__(self, id: str, title: str, subtitle: str, author: str, date: str, category: str):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date = date
        self.category = category


def get_bindings() -> List[Binding]:
    collection = common_db.articles

    results = []

    for item in collection.find({}):
        if 'public' in item and item['public'] == False:
            continue
        results.append(
            Binding(
                item['id'],
                item['title'],
                item['subtitle'],
                item['author'],
                item['date'],
                item['category']
            )
        )
        results.sort(key=lambda item: item.date, reverse=True)

    return results    