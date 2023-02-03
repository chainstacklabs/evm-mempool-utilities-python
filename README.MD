<img width="1200" alt="Labs" src="https://user-images.githubusercontent.com/99700157/213291931-5a822628-5b8a-4768-980d-65f324985d32.png">

<p>
 <h3 align="center">Chainstack is the leading suite of services connecting developers with Web3 infrastructure</h3>
</p>

<p align="center">
  <a target="_blank" href="https://chainstack.com/build-better-with-ethereum/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/Ethereum.svg" /></a>&nbsp;  
  <a target="_blank" href="https://chainstack.com/build-better-with-bnb-smart-chain/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/BNB.svg" /></a>&nbsp;
  <a target="_blank" href="https://chainstack.com/build-better-with-polygon/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/Polygon.svg" /></a>&nbsp;
  <a target="_blank" href="https://chainstack.com/build-better-with-avalanche/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/Avalanche.svg" /></a>&nbsp;
  <a target="_blank" href="https://chainstack.com/build-better-with-solana/"><img src="https://github.com/soos3d/blockchain-badges/blob/main/protocols_badges/Solana.svg" /></a>&nbsp;
</p>

<p align="center">
  <a target="_blank" href="https://chainstack.com/protocols/">Supported protocols</a> •
  <a target="_blank" href="https://chainstack.com/blog/">Chainstack blog</a> •
  <a target="_blank" href="https://docs.chainstack.com">Chainstack docs</a> •
  <a target="_blank" href="https://docs.chainstack.com/api/">Blockchain API reference</a> •
  <a target="_blank" href="https://console.chainstack.com/user/account/create">Start for free</a>
</p>

# EVM mempool utilities using Python

This project uses the web3.py library to guide you through pending transactions, nonce gaps, transaction replacements, and gas fee estimation.

Read the full tutorial on the Chainstack blog:
* [Blockchain transactions in Ethereum mempool – Coding edition ](https://chainstack.com/a-developers-guide-to-the-transactions-in-mempool-code-edition/)

## Project details

This repository contains the scripts used in the [Blockchain transactions in Ethereum mempool – Coding edition ](https://chainstack.com/a-developers-guide-to-the-transactions-in-mempool-code-edition/) tutorial. The blog discusses some reasons for transaction confirmation delays in EVM-based networks. The scripts use Python and the `web3.py` library to:

* Conduct gas fee estimation
* Send transaction
* "Cancel" or "Speed Up" a transaction
* handle nonce gap

## Quick start

Before running the code, it is highly recommended that you go through the blog as it describes the whole logic of the code.

Clone this repository.

Install the Python dependencies:

```sh
cd web3.py
```

Then

```sh
pip install -r requirements.txt
```

Set up your credentials in each `.py` file:

```py
# Setting node endpoint value
CHAINSTACK_NODE_ENDPOINT = '<NODE_ENDPOINT>'

# Setting account addressess
# you can copy the account addresses from metamask]

FROM_ACCOUNT = "<FROM_ACCOUNT_ADDRESS>"
TO_ACCOUNT = "<TO_ACCOUNT_ADDRESS>"

# Setting the user private key
SENDER_PRIVATEKEY = "<SENDER_PRIVATE_KEY>"
```

Run the file that you want to use:

```sh
python gas_estimate.py
```

## Prerequisites

* Python ^3.6
* A node RPC endpoint.

Deploy a node with Chainstack:

1. [Sign up with Chainstack](https://console.chainstack.com/user/account/create).  
1. [Deploy a node](https://docs.chainstack.com/platform/join-a-public-network).  
1. [View node access and credentials](https://docs.chainstack.com/platform/view-node-access-and-credentials). 

## Dependencies

* web3.py ^5.29.2

## Install

Install Python on your system:

* [Install Python](https://realpython.com/installing-python/)

Clone this repository.

Install the Python dependencies:
  
```sh
pip install -r requirements.txt
```
