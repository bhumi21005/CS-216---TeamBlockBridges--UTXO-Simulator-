class Validation:
    @staticmethod
    def validate_transaction(tx, utxo_manager, mempool_spent_utxos):
        # 1. Check for Same-TX double spend
        seen_in_tx = set()
        for inp in tx.inputs:
            u_key = (inp["prev_tx"], inp["index"])
            if u_key in seen_in_tx:
                return False, "REJECT: Same-TX double spend"
            seen_in_tx.add(u_key)

            # 2. Check for Mempool double spend
            if u_key in mempool_spent_utxos:
                return False, "REJECT: Double-spend (Mempool)"
            
            # 3. Check if UTXO exists in Global Set
            if not utxo_manager.exists(*u_key):
                return False, "REJECT: Input UTXO does not exist (Unconfirmed)"

        # 4. Check for Negative Amounts
        if any(o["amount"] < 0 for o in tx.outputs):
            return False, "REJECT: Negative amount"

        # 5. Check for Insufficient Funds
        input_total = sum(utxo_manager.utxo_set[(i["prev_tx"], i["index"])]["amount"] for i in tx.inputs)
        output_total = sum(o["amount"] for o in tx.outputs)
        
        if round(input_total, 8) < round(output_total, 8):
            return False, "REJECT: Insufficient funds"

        return True, "VALID"
