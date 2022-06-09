## Introduction

This repository contains the scripts used in the "Developer guide to the transactions in mempool - code edition " blog. The blog discusses some of the reasons for transaction confirmation delays in EVM-based networks. The scripts use python and web3.py library in order to,

* Conduct gas fee estimation
* Send transaction
* "Cancel" or "Speed Up" a transaction
* handle nonce gap

## Prerequisites

Before running the scripts, make sure you have the following requirements

* python v3.6 (or above)
* web3.py library

you can use the following code to install the desired web3.py version

```
cd web3.py
pip install -r requirements.txt
```

In addition to these requirements, you would also need access to a blockchain node, in order to run these scripts. To deploy your own ethereum node for free, visit [chainstack](https://chainstack.com/)

## Getting Started

The full breakdown of the code is available in the above mentioned blog. You may refer the blog before running the scripts