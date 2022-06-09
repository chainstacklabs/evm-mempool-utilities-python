# import Web3 class from web3 module
from web3 import Web3
# import math module
import math

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


# Set the Value for the percentage multipliers
SPEEDUP_MULTIPLIER = 1.10  # 10 % increase
CANCEL_MULTIPLIER = 1.5  # 50 % increase
# you can obtain the values by running the gas estimation script
# you can choose your preferred priority [ low,medium,high]
# and copy the corresponding values
maxPriorityFee = 0
maxFeePerGas = 0.

# convert the estimated values to wei denomination
maxPriorityFeeWei = w3.toWei(maxPriorityFee, 'gwei')
maxFeePerGasWei = w3.toWei(maxFeePerGas, 'gwei')


# get the pending transaction details using the hash value
pendingTransactionDetail = w3.eth.get_transaction(
    '<Pending_Transaction_Hash_Hex>')

# generate the suggested MaxPriorityFee and MaxFeePerGas using the pendingtransationDetail
# and the multipliers. Here we are using the SPEEDUP_MULTIPLIER,
# you can use the CANCEL_MULTIPLIER if you wish to cancel the transaction

suggestedMaxPriorityFee = math.ceil(
    pendingTransactionDetail['maxPriorityFeePerGas'] * SPEEDUP_MULTIPLIER)

suggestedMaxFeePerGas = math.ceil(
    pendingTransactionDetail['maxFeePerGas'] * SPEEDUP_MULTIPLIER)
# compare the values and get the bigger one
maxFeePerGas = suggestedMaxFeePerGas if suggestedMaxFeePerGas > maxFeePerGasWei else maxFeePerGasWei
maxPriorityFee = suggestedMaxPriorityFee if suggestedMaxPriorityFee > maxPriorityFeeWei else maxPriorityFeeWei

transaction = {
    'nonce': pendingTransactionDetail['nonce'],
    'to': pendingTransactionDetail['to'],  # recever's address
    'chainId': pendingTransactionDetail['chainId'],
    # 0 if you are canceling the transaction
    'value': pendingTransactionDetail['value'],
    # maximum gas that can be used for the transaction execution
    'gas': pendingTransactionDetail['gas'],
    'maxFeePerGas': maxFeePerGas,
    'maxPriorityFeePerGas': maxPriorityFee,
}
signedTransaction = w3.eth.account.sign_transaction(
    transaction, SENDER_PRIVATEKEY)

transactionHash = w3.eth.send_raw_transaction(
    signedTransaction.rawTransaction)
transactionHashHex = w3.toHex(transactionHash)
transactionReceipt = w3.eth.wait_for_transaction_receipt(transactionHashHex)
print(transactionReceipt)
