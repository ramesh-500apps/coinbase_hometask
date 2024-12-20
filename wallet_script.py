import os
import json
import logging
from eth_account import Account
import requests
from web3 import Web3
import time

WALLET_FILE = "wallet.json"  # File to store wallet details
FAUCET_URL = "http://faucet.base.org"  # URL for the faucet to fund the wallet
RPC_URL = "https://rpc.base.org/testnet"  # RPC URL for interacting with the Ethereum testnet

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def load_wallet():
    """
    Load wallet data from a file. If the wallet does not exist, create a new wallet and save it to a file.
    """
    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE, 'r') as file:
            wallet_data = json.load(file)
            logging.info("Wallet loaded successfully.")
            return wallet_data
    else:
        wallet = Account.create()  # Create a new Ethereum wallet
        wallet_data = {
            "address": wallet.address,  # Wallet address
            "private_key": wallet._private_key.hex()  # Private key in hex format
        }
        with open(WALLET_FILE, 'w') as file:
            json.dump(wallet_data, file)
            logging.info(f"New wallet created and saved with address {wallet.address}.")
            return wallet_data

def fund_wallet(wallet_address):
    """
    Request funds for the wallet from the faucet.
    """
    try:
        response = requests.post(FAUCET_URL, json={'address': wallet_address})
        if response.status_code == 200:
            logging.info("Faucet request sent successfully.")
            return True
        else:
            logging.error(f"Failed to fund wallet. Status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred while requesting faucet funds: {e}")
        return False

def check_balance(wallet_address, web3):
    """
    Check the balance of the wallet.
    """
    try:
        balance = web3.eth.get_balance(wallet_address)  # Get wallet balance in Wei
        eth_balance = web3.fromWei(balance, 'ether')  # Convert balance to ETH
        logging.info(f"Wallet balance: {eth_balance} ETH")
        return eth_balance
    except Exception as e:
        logging.error(f"Error checking balance: {e}")
        return None

def main():
    """
    Main function to load the wallet, request funds, and check the balance.
    """
    # Connect to the Ethereum testnet
    web3 = Web3(Web3.HTTPProvider(RPC_URL))

    # Load or create wallet data
    wallet_data = load_wallet()

    logging.info(f"Wallet address: {wallet_data['address']}")

    # Request funds and check balance
    if fund_wallet(wallet_data['address']):
        time.sleep(10)  # Wait for the faucet transaction to complete
        check_balance(wallet_data['address'], web3)
    else:
        logging.error("Failed to fund the wallet.")

if __name__ == "__main__":
    main()
