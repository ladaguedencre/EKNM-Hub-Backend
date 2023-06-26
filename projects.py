from dataclasses import dataclass
from typing import List
from common import common_db

@dataclass
class Project:
    id: str
    description: any
    link: str
    logo_url: str
    name: any
    state: int
    type: int

    def __init__(self, id: str, description: any, link: str, logo_url: str, name: any, state: int, type: int):
        self.id = id
        self.description = description
        self.link = link
        self.logo_url = logo_url
        self.name = name
        self.state = state
        self.type = type


def get_projects() -> List[Project]:
    collection = common_db.projects

    results = []

    for item in collection.find({}):
        results.append(
            Project(
                item['id'],
                item['description'],
                item.get('link', None),
                item['logo_url'],
                item['name'],
                item['state'],
                item['type']
            )
        )

    return results    