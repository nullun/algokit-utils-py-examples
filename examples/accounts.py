#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

#from algokit_utils import *
#from algosdk import kmd, mnemonic
import algokit_utils
import algosdk

# Setup clients
algod_config = algokit_utils.get_default_localnet_config("algod")
algod_client = algokit_utils.get_algod_client(algod_config)
kmd_config = algokit_utils.get_default_localnet_config("kmd")
kmd_client = algokit_utils.get_kmd_client_from_algod_client(algod_client)

# Create a new wallet and generate an account
wallet_name = "Test Wallet"
#new_acc = create_kmd_wallet_account(kmd_client, wallet_name)
account = algokit_utils.get_or_create_kmd_wallet_account(algod_client, wallet_name, 10, kmd_client)
print(f"Wallet Name: {wallet_name}")
print(f"New Address: {account.address}")
print(f"Private Key: {account.private_key}")

## Save wallet ID and master derivation key
#wallet_id = [wallet for wallet in kmd_client.list_wallets() if wallet['name'] == wallet_name][0]['id']
#hndl = kmd_client.init_wallet_handle(wallet_id, "")
#mdk = kmd_client.export_master_derivation_key(hndl, "")
#kmd_client.release_wallet_handle(hndl)
#
## Recover wallet and regenerate account
#create_kmd_wallet_account(kmd_client, "Restored " + wallet_name, mdk)

# Export an account
accout = algokit_utils.get_kmd_wallet_account(algod_client, kmd_client, wallet_name)
mn = algosdk.mnemonic.from_private_key(accout.private_key)
print(f"Account mnemonic: {mn}")

