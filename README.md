# Coinbase Home Task - Wallet Script

## Overview

This Python script allows you to create and manage a persistent wallet on the Base testnet, fund it using the Base testnet faucet, and display wallet information, including the balance in ETH.

The wallet is persistent across script executions, and the script handles wallet creation, funding from a faucet, and balance checking.

## Requirements

- Python 3.7 or later
- Install required Python packages:
  - web3: Used for interacting with Ethereum-based networks.
  - requests: Used for making HTTP requests to the faucet.

### Install dependencies:
```bash
pip install web3 requests