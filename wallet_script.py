from cdp import Cdp, Wallet  
import os
import json

api_key_name = "organizations/77b84c86-7548-48cd-8598-0825aebefceb/apiKeys/c93805f1-ad0e-4fef-b466-ca8a977b6c39"
api_key_private_key = '''-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIPcz+JJTCAASHCLGc2si9yFaNDyDC7xR/ichbcZbX+nOoAoGCCqGSM49
AwEHoUQDQgAEAq7dXZPbqqYazjGwwLpR3RxwCkYV3UAuvomlL9vqL9iW1+v4Wtti
z0iDh23C5GYepBVuXGzUTL2IEhfKkdWLJA==
-----END EC PRIVATE KEY-----'''

# Configure the CDP SDK with your API credentials
Cdp.configure(api_key_name=api_key_name, api_key_private_key=api_key_private_key)

# File to store the wallet seed (or private key)
wallet_seed_file = "wallet_seed.json"

def create_wallet():
    # Check if a wallet seed already exists to maintain wallet persistence
    if os.path.exists(wallet_seed_file):
        with open(wallet_seed_file, "r") as file:
            wallet_data = json.load(file)
        print(f"Wallet already exists. Using existing wallet with address: {wallet_data['address']}")
        return wallet_data
    else:
        # Create a new wallet
        wallet = Wallet.create()

        # Save the wallet's seed and public address for persistence
        wallet_data = {
            "seed": wallet.seed,
            "address": wallet.address
        }

        with open(wallet_seed_file, "w") as file:
            json.dump(wallet_data, file)

        print(f"New wallet created with address: {wallet.address}")
        return wallet_data

def fund_wallet(wallet_address):
    # Interact with the faucet API to fund the wallet
    try:
        faucet_url = "https://faucet.base.org"  # Assuming the faucet URL for the Base testnet
        response = Cdp.fund_wallet(wallet_address, faucet_url)

        if response.status_code == 200:
            print(f"Wallet {wallet_address} successfully funded.")
        else:
            print(f"Failed to fund the wallet: {response.text}")
    except Exception as e:
        print(f"Error funding wallet: {str(e)}")

def display_wallet_info(wallet_address):
    try:
        # Retrieve wallet balance
        balance = Cdp.get_balance(wallet_address)
        
        # Assuming the balance is returned in Wei, convert to ETH
        balance_eth = balance / 1e18

        print(f"Wallet Address: {wallet_address}")
        print(f"Balance: {balance_eth:.4f} ETH")
    except Exception as e:
        print(f"Error fetching wallet info: {str(e)}")

# Create or load the wallet
wallet_info = create_wallet()

# Fund the wallet
fund_wallet(wallet_info["address"])

# Display wallet information
display_wallet_info(wallet_info["address"])
