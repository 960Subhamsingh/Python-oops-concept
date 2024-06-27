import random

class ran:
    def __init__(self, item) -> None:
        self._items = list(._items) 
        random.shuffle(self._items)
    def main(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from emptyran')
    def _call__(self):
        return self.pick()
    