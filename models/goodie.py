from dataclasses import dataclass

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
