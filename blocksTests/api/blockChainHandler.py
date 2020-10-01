from blocksTests.api.redash.redashJsonPattern import RedashJsonPattern
import blocksTests.api.redash.redashHelper as redash_helper
from blocksTests.api.redash.redashQueryInfo import RedashQueryInfo
import blocksTests.api.polkadot_api as polkadot_rpc_api


class BlockChainHandler():

    # polkadot rpc

    def request_polkadot_rpc_latest_block(self):
        return polkadot_rpc_api.get_polkadot_rpc_latest_block()

    # polkadot

    def request_polkadot_top_block(self):
        json = redash_helper.get_fresh_query_result(RedashQueryInfo.polkadot_top_block.get_number)
        redash = RedashJsonPattern.from_json(json)
        return int(redash.get_top_block())

    def request_polkadot_missed_blocks(self):
        json = redash_helper.get_fresh_query_result(RedashQueryInfo.polkadot_missed_blocks.get_number)
        redash = RedashJsonPattern.from_json(json)
        return int(redash.get_missed_blocks_count())
