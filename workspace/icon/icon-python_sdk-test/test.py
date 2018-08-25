from icx.wallet import Wallet
from icx import utils
import os

# Create a keystore file of a wallet

os.remove('./keystore.txt')
my_wallet_1, _ = Wallet.create_keystore_file_of_wallet(keystore_file_path="./keystore.txt", password="test1234*")

# Create a wallet by the private key.
#my_wallet_2, _ = Wallet.create_wallet_by_private_key(password="test1234*", hex_private_key="")

# Open the keystore file of the wallet.
#my_wallet_3, _ = Wallet.open_keystore_file_of_wallet(keystore_file_path="./keystore.txt", password="test1234*")

# Get balance.
#balance = my_wallet_1.get_balance(uri="https://testwallet.icon.foundation/api/")
balance = utils.get_balance('hx5bfdb090f43a808005ffc27c25b213145e80b7cd', "http://52.79.233.89:9000/api/")
print('balance = ' + str(balance))

# Get information of the wallet.
#wallet_info = my_wallet_1.get_wallet_info(uri="https://testwallet.icon.foundation/api/")

# Get an address.
#wallet_address = my_wallet_1.get_address()

# Get block information by hash.
#block1 = Wallet.get_block_by_hash('885b8021826f7e741be7f53bb95b48221e9ab263f377e997b2e47a7b8f4a2a8b')

# Get block information by height.
#block2 = Wallet.get_block_by_height(1)

# Get last block information.
#last_block = Wallet.get_last_block()
