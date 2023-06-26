from dataclasses import dataclass
from typing import List
from common import common_db

@dataclass
class Binding:
    id: str
    first_line: str
    second_line: str
    image_url: str
    link: str

    def __init__(self, id: str, first_line: str, second_line: str, image_url: str, link: str):
        self.id = id
        self.first_line = first_line
        self.second_line = second_line
        self.image_url = image_url
        self.link = link


mock_binding: List[Binding] = [
    Binding(
        'test1',
        'Luntik test 1',
        'Super test 228',
        '../../assets/mock/icon1.png',
        '/test1',
    )
]

def get_bindings() -> List[Binding]:
    collection = common_db.bindings

    results = []

    for item in collection.find({}):
        results.append(
            Binding(
                item['id'],
                item['first_line'],
                item['second_line'],
                item['image_url'],
                item['link']
            )
        )

    return results    