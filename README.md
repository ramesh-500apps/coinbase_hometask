# Coinbase Wallet Creation, Funding, and Info Display Script

## Overview

This script allows you to:
1. Create a persistent wallet on the Base testnet.
2. Fund the wallet using the Base testnet faucet.
3. Display the wallet's address and balance in ETH.

It uses the **Coinbase Developer Kit (CDP SDK)** to interact with the Coinbase network.

## Prerequisites

1. **Python 3.11+** (ensure you are using the appropriate version).
2. Install required dependencies:
   ```bash
   pip install cdp-sdk
