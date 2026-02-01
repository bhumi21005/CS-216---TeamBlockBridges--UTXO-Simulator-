# CS-216---TeamBlockBridges--UTXO-Simulator


---
### Project Overview

This project is a complete simulation of the **Bitcoin UTXO (Unspent Transactions output)** model - implemented from scratch without using any Blockchain libraries. It demonstrates how bitcoin manages coins, validate transactions, prevent double spending, and confirm transactions via mining. 
This simulator is **simple, educational, and fully interactive via command-line menu** -  perfect for understanding real bitcoin mechanics.

---
### Team Members
- **Shruti Gajanan Turare** (240008029)  
- **Bhumika Kumari** (240051006)  
- **Kumkum Kushwaha** (240004028)  
- **Mhaske Prajwal Sanjay** (240004033)

---

 ### Instructions to run the program 

 1.  **Clone or Download**: Download this repository to your local machine.
2.  **Open Terminal**: Open your Terminal or Command Prompt.
3.  **Navigate to Source**: Go to the `src` directory by running:
    ```bash
    cd src
    ```
  4.Make sure python **3.8 or above** is installed.
  5. Run the main program.:

  '''
  python main.py
  '''

  6. You will see the interactive menu:
  '''
  ===Bitcoin Trasaction Simulator===
  1. Create new transaction
  2. View UTXO set
  3. View mempool
  4. Mine block
  5. Exit

  '''
  Follow the prompts to create transactions, view the UTXO state, inspect the mempool, and simulate mining.
  ---

  ##Brief Explaination of our Design

  Our simulator is designed using a clean, modular structure that reflects the core architecture of Bitcoin's UTXO model.

  ### UTXO Manager
  Maintains all unspent outputs.
  It allows: 
  - Adding new UTXOs  
  - Removing spent UTXOs  
  - Checking ownership  
  - Calculating balances  

  ###  Transaction Structure  
  Each transaction contains inputs (UTXOs being spent) and outputs (new UTXOs created).  
  Every transaction is assigned a unique, auto-generated ID.

  ###  Validator  
  The validator enforces all required rules:
  - Inputs must exist in the UTXO set  
  - No duplicate inputs  
  - Input amount ≥ Output amount  
  - No negative outputs  
  - No mempool conflicts (prevents double spending)  

  ### Mempool  
  Stores valid but unconfirmed transactions.  
  Tracks UTXOs currently “reserved” by pending transactions to avoid conflicts.

  ###  Mining Logic  
  Simulates block creation:
  - Selects transactions from the mempool  
  - Removes input UTXOs  
  - Adds output UTXOs  
  - Awards miner fees  
  - Clears mined transactions from the mempool  

 ###  Overall Design Choice  
  The system is intentionally lightweight and uses only Python’s standard library.  
  There is **no networking, no cryptography, and no distributed consensus** — only the core transaction and UTXO logic required by the assignment.

  ---

  ##  Dependencies / Installation

  No external libraries are needed.  
  The simulator runs entirely on Python's built-in standard library.

  ---

  ##  End of README
