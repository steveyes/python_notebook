from dataclasses import dataclass, field, InitVar
from typing import List


@dataclass
class Book:
    '''Object for tracking physical books in a collection.'''
    name: str
    condition: InitVar[str] = None
    weight: float = field(default=0.0, repr=False)
    shelf_id: int = field(init=False)
    chapters: List[str] = field(default_factory=list)

    def __post_init__(self, condition):
        if condition == "Discarded":
            self.shelf_id = None
        else:
            self.shelf_id = 0


book1 = Book('the book of chagnes', 'Disc')
print(book1)

