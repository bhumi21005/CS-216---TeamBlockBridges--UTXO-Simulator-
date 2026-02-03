import uuid
import random
class Transaction:
def __init__(self, tx_id, inputs, outputs):
self.tx_id = tx_id
self.inputs = inputs
self.outputs = outputs
self.fee = 0.0

def calculate_fee(self, utxo_manager):
input_total = sum(utxo_manager.utxo_set[(i["prev_tx"], i["index"])]["amount"] for i in self.inputs)
output_total = sum(o["amount"] for o in self.outputs)
self.fee = round(input_total - output_total, 8)
return self.fee

def to_dict(self):
return {"tx_id": self.tx_id, "inputs": self.inputs, "outputs": self.outputs, "fee": self.fee}
