from dataclasses import dataclass

@dataclass
class Brew:
    id: str
    description: any
    image_url: str
    name: any

    def __init__(self, id: str, description: any, image_url: str, name: any):
        self.id = id
        self.description = description
        self.image_url = image_url
        self.name = name
