import unittest

from blocksTests.tests.api.polkadotDevTest.polkadotProdCompareHeadRpcTest import PolkadotProdRpcIndexTest
from blocksTests.tests.api.polkadotDevTest.polkadotProdMissedBlocksTest import PolkadotProdMissedBlocksTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(PolkadotProdRpcIndexTest('test_polkadot_prod_rpc_index'))
    suite.addTest(PolkadotProdMissedBlocksTest('test_polkadot_prod_missed_blocks'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
