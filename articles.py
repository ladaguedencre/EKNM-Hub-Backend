from dataclasses import dataclass, asdict
from typing import List
from common import common_db

@dataclass
class Article:
    id: str
    author: str
    background: str
    category: str
    content: any
    date: str
    name: any
    section: str

    def __init__(
        self, 
        id: str,
        author: str,
        background: str,
        category: str,
        content: any,
        date: str,
        name: any,
        section: str
    ):
        self.id = id
        self.author = author
        self.background = background
        self.category = category
        self.content = content
        self.date = date
        self.name = name
        self.section = section


def get_article(id: str) -> List[Article]:
    collection = common_db.articles

    item = collection.find_one({'id': id})
    if item:
        return asdict(Article(
            item['id'],
            item.get('author', None),
            item.get('background', None),
            item.get('category', None),
            item['content'],
            item.get('date', None),
            item['name'],
            item.get('section', None)
        ))

    return None    