from dataclasses import dataclass

@dataclass
class Article:
    id: str
    title: str
    subtitle: str
    background: str
    content: str

    def __init__(
        self, 
        id: str,
        title: str,
        subtitle: str,
        background: str,
        content: str
    ):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.background = background
        self.content = content
