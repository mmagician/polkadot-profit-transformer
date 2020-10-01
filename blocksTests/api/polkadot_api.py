from substrateinterface import SubstrateInterface


def get_polkadot_rpc_latest_block():
    substrate = SubstrateInterface(
        url="ws://127.0.0.1:9944",
        address_type=2,
        type_registry_preset='kusama'
    )
    return substrate.get_block_number(substrate.get_chain_head())
