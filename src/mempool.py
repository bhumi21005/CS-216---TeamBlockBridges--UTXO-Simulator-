#MEMPOOL CLASS
class Mempool:
def __init__(self, max_size=50):
self.transactions = []
self.spent_utxos = set()
self.max_size = max_size

def add_transaction(self, tx_obj, utxo_manager):
if len(self.transactions) >= self.max_size:
return False, "REJECT: Mempool is full"

# USE SEPARATE VALIDATION CLASS
is_valid, message = Validation.validate_transaction(tx_obj, utxo_manager, self.spent_utxos)

if not is_valid:
return False, message

tx_obj.calculate_fee(utxo_manager)
self.transactions.append(tx_obj)
for inp in tx_obj.inputs:
self.spent_utxos.add((inp["prev_tx"], inp["index"]))
return True, tx_obj.to_dict()

def get_top_transactions(self, n):
return sorted(self.transactions, key=lambda x: x.fee, reverse=True)[:n]
