import unittest
from blocksTests.api.blockChainHandler import BlockChainHandler
import blocksTests.tests.testsThreshold as limits


class PolkadotProdMissedBlocksTest(unittest.TestCase):

    def test_polkadot_prod_missed_blocks(self):
        block_chain_handler = BlockChainHandler()
        missed_blocks_count = block_chain_handler.request_polkadot_missed_blocks()
        self.assertTrue(missed_blocks_count <= limits.MISSED_BLOCKS_THRESHOLD,
                        'Polkadot have missed blocksTests : {} '.format(missed_blocks_count))
