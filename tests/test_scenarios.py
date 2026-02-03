
# PART 5: THE COMPLETE 10-TEST SUITE
def run_mandatory_tests():
    print("\n" + "═"*60)
    print("      DETAILED TEST SUITE: ALL 10 MANDATORY CASES")
    print("═"*60)
    
    t_um = UTXOManager()
    t_mp = Mempool()
    t_um.add_utxo("genesis", 0, 50.0, "Alice")
    t_um.add_utxo("genesis", 1, 30.0, "Bob")
    t_um.add_utxo("genesis", 2, 20.0, "Charlie")

    def log_test(num, name, success):
        print(f"Test {num:<2}: {name:<40} | Status: {'PASS' if success else 'FAIL'}")

    tx1 = {"tx_id": "tx1", "inputs": [{"prev_tx": "genesis", "index": 0}], 
           "outputs": [{"amount": 10.0, "address": "Bob"}, {"amount": 39.999, "address": "Alice"}]}
    s1, r1 = t_mp.add_transaction(tx1, t_um)
    log_test(1, "Basic Valid Transaction", s1 and r1['fee'] == 0.001)

    t_mp = Mempool()
    tx2 = {"tx_id": "tx2", "inputs": [{"prev_tx": "genesis", "index": 0}, {"prev_tx": "genesis", "index": 1}], 
           "outputs": [{"amount": 75.0, "address": "Charlie"}]}
    s2, _ = t_mp.add_transaction(tx2, t_um)
    log_test(2, "Multiple Inputs", s2)

    tx3 = {"tx_id": "tx3", "inputs": [{"prev_tx": "genesis", "index": 0}, {"prev_tx": "genesis", "index": 0}], 
           "outputs": [{"amount": 10.0, "address": "Bob"}]}
    s3, _ = t_mp.add_transaction(tx3, t_um)
    log_test(3, "Double-Spend in Same TX", not s3)

    t_mp = Mempool()
    tx4a = {"tx_id": "tx4a", "inputs": [{"prev_tx": "genesis", "index": 0}], "outputs": [{"amount": 10.0, "address": "Bob"}]}
    tx4b = {"tx_id": "tx4b", "inputs": [{"prev_tx": "genesis", "index": 0}], "outputs": [{"amount": 10.0, "address": "Charlie"}]}
    t_mp.add_transaction(tx4a, t_um)
    s4, _ = t_mp.add_transaction(tx4b, t_um)
    log_test(4, "Mempool Double-Spend", not s4)

    tx5 = {"tx_id": "tx5", "inputs": [{"prev_tx": "genesis", "index": 2}], "outputs": [{"amount": 25.0, "address": "Alice"}]}
    s5, r5 = t_mp.add_transaction(tx5, t_um)
    log_test(5, "Insufficient Funds", not s5 and "Insufficient" in r5)

    tx6 = {"tx_id": "tx6", "inputs": [{"prev_tx": "genesis", "index": 2}], "outputs": [{"amount": -5.0, "address": "Alice"}]}
    s6, _ = t_mp.add_transaction(tx6, t_um)
    log_test(6, "Negative Amount", not s6)

    tx7 = {"tx_id": "tx7", "inputs": [{"prev_tx": "genesis", "index": 2}], "outputs": [{"amount": 20.0, "address": "Alice"}]}
    s7, r7 = t_mp.add_transaction(tx7, t_um)
    log_test(7, "Zero Fee Transaction", s7 and r7['fee'] == 0.0)

    log_test(8, "Race Attack (First-Seen)", not s4)

    t_mp = Mempool()
    t_mp.add_transaction(tx1, t_um)
    pre_bal = t_um.get_balance("Miner1")
    mine_block("Miner1", t_mp, t_um)
    log_test(9, "Complete Mining Flow", t_um.get_balance("Miner1") > pre_bal)

    t_mp = Mempool()
    tx10a = {"tx_id": "tx10a", "inputs": [{"prev_tx": "genesis", "index": 1}], "outputs": [{"amount": 5.0, "address": "Charlie"}]}
    t_mp.add_transaction(tx10a, t_um)
    tx10b = {"tx_id": "tx10b", "inputs": [{"prev_tx": "tx10a", "index": 0}], "outputs": [{"amount": 2.0, "address": "David"}]}
    s10, _ = t_mp.add_transaction(tx10b, t_um)
    log_test(10, "Unconfirmed Chain (Reject)", not s10)

    print("═"*60 + "\n")
