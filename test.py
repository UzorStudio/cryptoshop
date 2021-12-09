from tronpy import Tron
from tronpy.providers import HTTPProvider

client = Tron(HTTPProvider(api_key="3fdadf50-c0e0-4223-ae9c-00fc44ff6358"),network="shasta")
acc = client.generate_address()
print(acc)

print(client.get_account_balance(acc["base58check_address"]))