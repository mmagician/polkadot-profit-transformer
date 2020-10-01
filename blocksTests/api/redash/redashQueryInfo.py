from enum import Enum
from collections import namedtuple

query = namedtuple('query', ['number', 'api_key'])


class RedashQueryInfo(Enum):
    # polkadot
    polkadot_top_block = query(73, 'o1GvCRbDbZcYGffmQN9OI9ezmWjtVVi8eQxotLfs')
    polkadot_missed_blocks = query(72, 'V0Hz083FZ2LhQCLPABX7cT50LBO5iN3YwGRTczwW')

    @property
    def get_url(self):
        return self.value.url

    @property
    def get_number(self):
        return self.value.number

    @property
    def get_api_key(self):
        return self.value.api_key
