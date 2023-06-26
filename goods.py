from dataclasses import dataclass
from typing import List
from common import common_db

@dataclass
class Goodie:
    id: str
    count: int
    name: any
    image_url: str
    type: int

    def __init__(self, id: str, count: int, name: any, image_url: str, type: int):
        self.id = id
        self.count = count
        self.name = name
        self.image_url = image_url
        self.type = type


def get_goods() -> List[Goodie]:
    collection = common_db.goods
    results = []

    for item in collection.find({}):
        results.append(
            Goodie(
                item['id'],
                item['count'],
                item['name'],
                item['image_url'],
                item['type']
            )
        )

    return results    