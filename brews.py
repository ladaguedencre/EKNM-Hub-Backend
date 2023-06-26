from dataclasses import dataclass
from typing import List
from common import common_db

@dataclass
class Brew:
    id: str
    count: int
    description: any
    image_url: str
    name: any

    def __init__(self, id: str, count: int, description: any, image_url: str, name: any):
        self.id = id
        self.count = count
        self.description = description
        self.image_url = image_url
        self.name = name


def get_brews() -> List[Brew]:
    collection = common_db.brews

    results = []

    for item in collection.find({}):
        results.append(
            Brew(
                item['id'],
                item['count'],
                item['description'],
                item['image_url'],
                item['name']
            )
        )

    return results    