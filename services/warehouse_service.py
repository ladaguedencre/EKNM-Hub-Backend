from typing import List
from models.goodie import Goodie

class WarehouseService:

    def __init__(self, database) -> None:
        self.database = database

    def get_goods(self) -> List[Goodie]:
        collection = self.database.goods
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
