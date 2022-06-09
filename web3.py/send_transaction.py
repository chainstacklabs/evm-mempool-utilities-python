# import Web3 class from web3 module
from web3 import Web3
# Setting node endpoint value
CHAINSTACK_NODE_ENDPOINT = '<NODE_ENDPOINT>'

# Setting account addressess
# you can copy the account addresses from metamask]

FROM_ACCOUNT = "<FROM_ACCOUNT_ADDRESS>"
TO_ACCOUNT = "<TO_ACCOUNT_ADDRESS>"

# Setting the user private key
SENDER_PRIVATEKEY = "<SENDER_PRIVATE_KEY>"

# Connect to the node
w3 = Web3(Web3.HTTPProvider(CHAINSTACK_NODE_ENDPOINT))


# Setting the transaction variables

# get the MAX_PRIORITY_FEE and MAX_FEE_PER_GAS values
# by running the gas estimation script.
# you can choose your preferred priority [ low,medium,high]
# and copy the corresponding values
MAX_PRIORITY_FEE = 0
MAX_FEE_PER_GAS = 0

# Setting the value that you wish to send
ETH_VALUE = 0.05

# Getting the account-nonce value
ACCOUNT_NONCE = w3.eth.getTransactionCount(FROM_ACCOUNT)
# Setting the value for chainID
CHAIN_ID = w3.eth.chain_id


# While sending the transaction,
# we must represent all the fee related values and
# the ethereum value in wei denomination.
transaction = {
    'nonce': ACCOUNT_NONCE,
    'to': TO_ACCOUNT,  # recever's address
    'value': w3.toWei(ETH_VALUE, "ether"),
    # maximum gas that can be used for the transaction execution
    'gas': 2100000,
    'maxFeePerGas': w3.toWei(MAX_FEE_PER_GAS, 'gwei'),
    'maxPriorityFeePerGas': w3.toWei(MAX_PRIORITY_FEE, 'gwei'),
    'chainId': CHAIN_ID
}
# signing the transaction using the sender's private key
signedTransaction = w3.eth.account.sign_transaction(
    transaction, SENDER_PRIVATEKEY)
# sending the signed transaction,
# this will return the transaction hash in byte encoded format
transactionHash = w3.eth.send_raw_transaction(
    signedTransaction.rawTransaction)
# converting the byte-encoded transaction hash to hex string
transactionHashHex = w3.toHex(transactionHash)
print(transactionHashHex)
