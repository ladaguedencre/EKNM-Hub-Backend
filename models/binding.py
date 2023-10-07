from dataclasses import dataclass

@dataclass
class Binding:
    id: str
    title: str
    subtitle: str
    author: str
    date: str
    category: str

    def __init__(self, id: str, title: str, subtitle: str, author: str, date: str, category: str):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date = date
        self.category = category
