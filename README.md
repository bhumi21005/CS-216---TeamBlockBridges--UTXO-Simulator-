# Bitcoin Transaction & UTXO Simulator  
**CS 216 – Introduction to Blockchain**

---

## Course Information

**Course:** CS 216 – Introduction to Blockchain  
**Assignment:** Bitcoin Transaction & UTXO Simulator  
**Submission Type:** Public GitHub Repository  

---
## 👥 Team Information

**Team Name:** HighOnByte  

**Team Members:**

- **Bhumika Kumari** – 240051006 
- **Kumkum ** – 
- **Prajwal** – 
- **Shruti** – 240008029
---

## Overview

This project presents a **Python-based simulation of Bitcoin’s transaction mechanism**, centered around the **UTXO (Unspent Transaction Output) model**.  
The simulator explains how Bitcoin-style transactions are created, verified, queued, and confirmed through mining, while ensuring that **double-spending is strictly prevented**.

The implementation strictly follows the **CS 216 assignment guidelines** and is intentionally designed as a **local, single-node system**.  
No networking, cryptography, or consensus algorithms are included, keeping the focus on **core transaction logic**.

---

##  Objectives of the Project

Through this assignment, we aim to demonstrate:

- Conceptual understanding of the **UTXO-based accounting system**
- Implementation of **Bitcoin-like transaction validation**
- Prevention of **double-spending using UTXO and mempool checks**
- Simulation of the **transaction lifecycle**
- Insight into **transaction fees and miner rewards**

---

##  Features Implemented

### 1️ UTXO Management

#### Concept

Bitcoin does not store balances directly.  
Instead, it keeps track of **unspent outputs** created by previous transactions.

Important properties of UTXOs:

- Each UTXO represents a **spendable unit of Bitcoin**
- A UTXO is always **fully consumed** when spent
- New UTXOs are generated as transaction outputs
- User balance = **sum of all owned UTXOs**

 **Analogy:**  
UTXOs behave like physical currency notes — you cannot tear a note to pay half; you spend it fully and receive change.

#### Implementation Highlights

- UTXOs stored in a dictionary for constant-time lookup
- Each UTXO identified by `(transaction_id, output_index)`
- Snapshot and rollback mechanism used during mining failures
- Balance calculated dynamically by scanning owned UTXOs

---

### 2️ Transaction Creation & Structure

A transaction converts **existing UTXOs into new ones**.

Each transaction includes:
- Input references to previous UTXOs
- Output definitions for recipients and change
- An implicit transaction fee

Transaction flow:
Bash
```
Create → Validate → Mempool → Mine → Confirm 
```
UTXOs are selected greedily (largest first) to minimize the number of inputs.

---

### 3️ Validation Rules

Before acceptance, every transaction must satisfy:

- All input UTXOs must exist
- No UTXO can be used more than once
- Input owner must match spender
- Input value must cover outputs
- Output values must be positive
- Inputs must not conflict with mempool transactions

Any violation causes immediate rejection.

---

### 4️ Mempool Handling

The mempool temporarily stores **valid but unconfirmed transactions**.

Key characteristics:

- Enforces the **first-seen rule**
- Rejects conflicting transactions
- Prioritizes higher-fee transactions
- Enforces a fixed maximum size
- Evicts lowest-fee transactions when full

This design mirrors real Bitcoin node behavior at a simplified level.

---

### 5️ Mining Simulation

Mining simulates block creation without Proof-of-Work.

Mining steps:

1. Select top-fee transactions from mempool
2. Save UTXO snapshot
3. Revalidate transactions
4. Apply UTXO updates atomically
5. Collect total transaction fees
6. Reward miner via coinbase output
7. Remove confirmed transactions
8. Increment block height

If any transaction fails during mining, the system **rolls back** safely.

---

### 6️ Double-Spending Protection

Double-spending is prevented at multiple levels:

- Duplicate inputs rejected within a transaction
- Spent UTXOs removed from the global set
- Mempool prevents conflicting pending transactions
- Mining re-validates transactions before confirmation

This layered defense ensures consistency and correctness.

---

##  Design Decisions

### No Spending of Unconfirmed Outputs
- Simplifies validation
- Avoids dependency chains

### First-Seen Rule
- Predictable behavior
- Prevents race attacks
- Replace-by-fee not implemented for simplicity

### Greedy UTXO Selection
- Reduces transaction size
- Easy to implement and reason about

### Implicit Fee Model
- Fee = Inputs − Outputs
- Matches Bitcoin’s actual design


##  How to Run

###  Requirements

- Python **3.8 or higher**
- No external libraries required

---

###  Execution Steps

1. **Clone the repository and move into the project directory:**

```bash
git clone <repository-url>
cd blockchain-1
```
2. **Run the main program:**

```bash
python src/main.py
```

3. ** Run test cases:**
```bash
python test/testing.py
```

##  Test Scenarios
- Valid transactions with automatic change output
- Transactions using multiple input UTXOs
- Double-spending attempts within a single transaction
- Double-spending across different transactions (mempool conflict)
- Transactions with insufficient balance
- Rejection of negative or zero-value outputs
- Zero-fee transactions
- Basic race-condition style conflict simulation

---
