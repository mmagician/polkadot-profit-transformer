import unittest
from blocksTests.api.blockChainHandler import BlockChainHandler
import blocksTests.tests.testsThreshold as limits


class PolkadotProdRpcIndexTest(unittest.TestCase):

    # Request_polkadot_rpc_latest_block require a tunnel using data/id_rsa ssh private key.
    # Private key is approved remotely.
    # To run this test locally replace /root/.ssh/id_rsa by /p2p-autotests/data/id_rsa

    def test_polkadot_prod_rpc_index(self):
        block_chain_handler = BlockChainHandler()
        difference = block_chain_handler.request_polkadot_rpc_latest_block() - block_chain_handler.request_polkadot_top_block()
        self.assertTrue(difference <= limits.RPC_HEAD_THRESHOLD,
                        'Polkadot top blockw is less than rpc latest block for : {} '.format(difference))
