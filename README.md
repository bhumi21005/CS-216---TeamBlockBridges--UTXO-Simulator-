# Bitcoin Transaction & UTXO Simulator  
**CS 216 – Introduction to Blockchain**

---

## Course Information

**Course:** CS 216 – Introduction to Blockchain  
**Assignment:** Bitcoin Transaction & UTXO Simulator  
**Submission Type:** Public GitHub Repository  

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

💡 **Analogy:**  
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
Bash```
Create → Validate → Mempool → Mine → Confirm 
```
