class RedashJsonPattern():

    def __init__(self, data, **kw):
        self.data = data

    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)

    def get_data(self):
        return self.data

    def get_top_block(self):
        return self.get_data()['rows'][0]['max']

    def get_missed_blocks_count(self):
        return self.get_data()['rows'][0]['?column?']
