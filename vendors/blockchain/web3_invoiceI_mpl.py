import sys
import time
import pprint
from web3 import HTTPProvider
from web3.contract import ConciseContract
from web3.providers.eth_tester import EthereumTesterProvider
from web3 import Web3
from solc import compile_source
from InvoiceOnchain.settings import LOCAL_NETWORK_ADDR,CONTRACT_ADDRESS
import json

def compile_source_file(file_path):
   with open(file_path, 'r') as f:
      source = f.read()
   return compile_source(source)


def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).deploy()

    address = w3.eth.getTransactionReceipt(tx_hash)['contractAddress']
    return address


def wait_for_receipt(w3, tx_hash, poll_interval):
   while True:
       tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       if tx_receipt:
         return tx_receipt
       time.sleep(poll_interval)

def compile_deploy_contract(path):  # w3  Web3(HTTPProvider(LOCAL_NETWORK_ADDR))
        myfile = open('/Users/sierra/Projects/Aurora/InvoiceChainService/InvoiceOnChain/vendors/blockchain/VendorInvoice.json','r').read()
        w3 = Web3(HTTPProvider('http://127.0.0.1:7545'))
        contract = w3.eth.contract(abi=json.loads(myfile),address='0x16cD64626C42014cEc20de4802ea247F94F2C1Eb')
        transaction = contract.transact({"from": w3.eth.accounts[0]})
        contract.functions.addInvoice('0x6e9E9B26819a66c82337df78bdA2E80e6822F2E5','init invoice','blah0-234',200000000000,'0x4974Bf8c8163A61FE81114EA4747f6349318110E',2313231231).estimateGas()
        c2 = ConciseContract
        # Get transaction hash from deployed contract
        # Get tx receipt to get contract address
        #tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
        #contract_address = tx_receipt['contractAddress']
        # Contract instance in concise mode
        # Getters + Setters for web3.eth.contract object


