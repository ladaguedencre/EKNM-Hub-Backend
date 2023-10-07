from typing import List
from models.brew import Brew

class BrewService:

    def __init__(self, database) -> None:
        self.database = database

    def get_brews(self) -> List[Brew]:
        collection = self.database.brews

        results = []

        for item in collection.find({}):
            results.append(
                Brew(
                    item['id'],
                    item['description'],
                    item['image_url'],
                    item['name']
                )
            )

        return results
