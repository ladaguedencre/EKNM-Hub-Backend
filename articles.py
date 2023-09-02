from dataclasses import dataclass, asdict
from typing import List
from common import common_db

@dataclass
class Article:
    id: str
    title: str
    subtitle: str
    content: str

    def __init__(
        self, 
        id: str,
        title: str,
        subtitle: str,
        content: str
    ):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.content = content


def get_article(id: str) -> List[Article]:
    collection = common_db.articles

    item = collection.find_one({'id': id})
    if item:
        return asdict(Article(
            item['id'],
            item['title'],
            item['subtitle'],
            item['content'],
        ))

    return None    