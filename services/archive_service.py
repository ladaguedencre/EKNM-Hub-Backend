from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from models.article import Article
from models.binding import Binding

class ArchiveService:

    def __init__(self, database) -> None:
        self.database = database

    def get_article(self, id: str) -> Optional[Dict]:
        collection = self.database.articles
        item = collection.find_one({'id': id})
        if item:
            return asdict(Article(
                item['id'],
                item['title'],
                item['subtitle'],
                item['background'],
                item['content'],
            ))
        return None   

    def get_bindings(self) -> List[Binding]:
        collection = self.database.articles

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
