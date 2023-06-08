from web3 import Web3
from web3.logs import WARN

from contract_compiler import abi, bytecode
import time

RPC_API_ENDPOINT = "http://192.168.109.131:8545"
CONTRACT_ADDRESS = '0x66752e648a8E96eD9cFE5CFB8BF4646Bb4E8317C'
web3 = Web3(Web3.HTTPProvider(RPC_API_ENDPOINT))
AlertProcessor = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi, bytecode=bytecode)


def handle_event(event):
    receipt = web3.eth.wait_for_transaction_receipt(event['transactionHash'])
    # data = bytes.fromhex(receipt.logs.data)
    # event NewAlert(string fqmn, uint256 timestamp, Suspect[] suspect, string description);
    # decodedABI = abi.decode(['string', 'ui', 'uint256'], data)
    result = AlertProcessor.events.NewAlert().process_receipt(receipt, errors=WARN)
    print(result)


def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)


def main():
    block_filter = web3.eth.filter({'fromBlock':'latest', 'address':CONTRACT_ADDRESS})
    log_loop(block_filter, 2)


if __name__ == '__main__':
    main()
