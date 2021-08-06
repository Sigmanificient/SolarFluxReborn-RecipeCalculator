class Counter(dict):

    def __getitem__(self, key):
        if key not in self:
            self[key] = 0

        return super(Counter, self).__getitem__(key)
