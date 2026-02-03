import uuid
import random
def smart_create_tx(sender, receiver, amount, fee=0.001):
    utxos = um.get_utxos_for_owner(sender)
    selected_inputs, accumulated = [], 0
    for key in utxos:
        accumulated += um.utxo_set[key]["amount"]
        selected_inputs.append({"prev_tx": key[0], "index": key[1]})
        if accumulated >= (amount + fee): break
    if accumulated < (amount + fee): return False, "Insufficient balance"
    
    change = round(accumulated - amount - fee, 8)
    outputs = [{"amount": amount, "address": receiver}]
    if change > 0: outputs.append({"amount": change, "address": sender})
    
    new_tx = Transaction(f"TX-{uuid.uuid4().hex[:8].upper()}", selected_inputs, outputs)
    return mp.add_transaction(new_tx, um)

um = UTXOManager(); mp = Mempool()

def initialize_genesis_data():
    genesis_data = [("Alice", 50.0, 0), ("Bob", 30.0, 1), ("Charlie", 20.0, 2), ("David", 10.0, 3), ("Eve", 5.0, 4)]
    for owner, amt, idx in genesis_data: um.add_utxo("genesis", idx, amt, owner)

def main():
    initialize_genesis_data()
    while True:
        print("\n" + "═"*35 + "\n     BITCOIN UTXO SIMULATOR\n" + "═"*35)
        print("1. Create TX\n2. View UTXO Set\n3. View Mempool\n4. Mine Block\n5. Run Mandatory Tests\n6. Add User\n7. Exit")
        c = input("\nChoice: ")
        if c == "1":
            try:
                sender = input("Sender: "); sender_utxos = um.get_utxos_for_owner(sender)
                print("-" * 35 + f"\n      {sender.upper()}'S AVAILABLE UTXOs\n" + "-" * 35)
                if not sender_utxos: print("No available coins found.")
                else:
                    for key in sender_utxos: print(f"Ref: {key[0]}:{key[1]:<5} | Amount: {um.utxo_set[key]['amount']:>6} BTC")
                print("-" * 35)
                recipient = input("Recipient: "); amount = float(input("Amount: "))
                f_in = input("Fee (Enter for 0.001): "); fee = float(f_in) if f_in.strip() else 0.001
                success, result = smart_create_tx(sender, recipient, amount, fee)
                if success:
                    print("-" * 35 + f"\n      TRANSACTION RECEIPT\nID     : {result['tx_id']}\nStatus : SUCCESS\nFee    : {result['fee']} BTC\nMempool: {len(mp.transactions)} pending\n" + "-" * 35)
                else: print(f"\n[!] FAILED: {result}")
            except Exception as e: print(f"\n[!] Error: {e}")
        elif c == "2":
            print("\n" + "-" * 35 + f"\n      GLOBAL UTXO SET\n" + "-" * 35)
            for k, v in sorted(um.utxo_set.items(), key=lambda x: x[1]['owner']): print(f"Owner: {v['owner']:<8} | Amt: {v['amount']:>6} BTC | {k[0]}:{k[1]}")
            print("-" * 35)
        elif c == "3":
            print("\n" + "-" * 35 + f"\n      MEMPOOL STATUS\n" + "-" * 35)
            for tx in mp.transactions: print(f"• {tx.tx_id} | Fee: {tx.fee}")
            print("-" * 35)
        elif c == "4":
            res = mine_block('Miner1', mp, um)
            if res: print("-" * 35 + f"\n      BLOCK MINED\nMiner  : {res['miner']}\nTXs    : {res['tx_count']}\nRewards: {res['fees']} BTC\n" + "-" * 35)
            else: print("\n[!] Mining failed: Mempool empty.")
        elif c == "5": run_mandatory_tests()
        elif c == "6":
            try:
                u, amt = input("Username: "), float(input("Amount: "))
                um.add_utxo(f"airdrop_{uuid.uuid4().hex[:4]}", 0, amt, u)
                print("-" * 35 + f"\n      USER ADDED\nUser: {u} | Bal: {amt}\n" + "-" * 35)
            except: print("\n[!] Error: Invalid Input")
        elif c == "7": break

if __name__ == "__main__":
    main()
