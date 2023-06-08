from web3 import Web3
from contract_compiler import abi, bytecode

RPC_API_ENDPOINT = "http://192.168.109.131:8545"
CONTRACT_ADDRESS = '0x66752e648a8E96eD9cFE5CFB8BF4646Bb4E8317C'

web3 = Web3(Web3.HTTPProvider(RPC_API_ENDPOINT))
AlertProcessor = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi, bytecode=bytecode)



account_from = {
    'private_key': 'd5ade9e961f2873084f8ee7eaaf91f729b15abcd7249041ed964a279f4c3b405',
    'address': Web3.to_checksum_address('5886ccdeba01f62d9fc9009c981ff65e256bfdf0'),
}

fqmn = "twerwerest"
callstack = "0x0000000000000000000000000000000000000000000000000000000000000023"
parameterIndexes = [123, 456]
features = [1234, 5678]
paths = ["wowie", "eiwow"]
chars = ["b", "c"]
timestamp = 21312312
description = "this is a tets to sljflsaef"

params = [fqmn, callstack, parameterIndexes, features, paths, chars, timestamp, description]
thing = AlertProcessor.encodeABI(fn_name="processAlert", args=params)
tx_create = web3.eth.account.sign_transaction(dict(
    nonce=web3.eth.get_transaction_count(account_from["address"]),
    gasPrice=200002300000,
    gas=1000000,
    to=CONTRACT_ADDRESS,
    data=thing,
  ),
  account_from["private_key"],
)
# processAlert_tx = AlertProcessor.functions.processAlert(params).build_transaction(
#     {
#         "gasPrice": web3.eth.gas_price,
#         'from': account_from['address'],
#         'nonce': web3.eth.get_transaction_count(account_from['address']),
#     }
# )

# tx_create = web3.eth.account.sign_transaction(processAlert_tx, account_from['private_key'])

tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Tx successful with hash: {tx_receipt.transactionHash.hex()}')