#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

#from algokit_utils import *
#from algosdk import kmd, mnemonic
import algokit_utils
import algosdk

# example: KMD_CREATE_CLIENT

algod_config = algokit_utils.get_default_localnet_config("algod")
algod_client = algokit_utils.get_algod_client(algod_config)
kmd_config = algokit_utils.get_default_localnet_config("kmd")
kmd_client = algokit_utils.get_kmd_client_from_algod_client(algod_client)

# example: KMD_CREATE_CLIENT

# example: KMD_CREATE_WALLET

wallet_name = "Test Wallet"
account = algokit_utils.get_or_create_kmd_wallet_account(algod_client, wallet_name, 10, kmd_client)
print(f"Wallet Name: {wallet_name}")
print(f"New Address: {account.address}")
print(f"Private Key: {account.private_key}")

# example: KMD_CREATE_WALLET

# example: KMD_CREATE_ACCOUNT

accout = algokit_utils.get_kmd_wallet_account(algod_client, kmd_client, wallet_name)
mn = algosdk.mnemonic.from_private_key(accout.private_key)
print(f"Account mnemonic: {mn}")

# example: KMD_CREATE_ACCOUNT

