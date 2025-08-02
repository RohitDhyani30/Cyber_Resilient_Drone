# Cyber_Resilient_Drone
By - Rohit Dhyani

## Overview

This project provides a framework which provides secure communication between a remote control and a drone using hash-based signal authentication. One mobile phone acts as a remote, sending control signals through Wi-Fi. A laptop captures these signals, appends a secure hash (HMAC) to them, and sends the hashed signal to a second laptop (simulated drone). The receiving system verifies the hash to ensure the signal's authenticity, preventing unauthorized commands from being executed.

## Components

The project consists of following Python scripts and files:

---

### 1. `hmac_code.py`

**Description:**  
This script reads a captured Wi-Fi signal from a `.pcapng` file and generates an HMAC-SHA256 hash value using a pre-shared secret key, and saves the hash into a seperate file `hash_value.txt`


### 2. `hash_value.txt`

**Description:** 
This file stores the generated hash value from hmac_code.py. It is used by the append.py script to merge the control signal with its corresponding hash for secure transmission.


### 3. `append.py`

**Description:** 
This script reads the original control signal and the hash from hash_value.txt, then creates a custom packet by combining both. The merged packet is stored in a new `.pcapng` file ready for transmission.

### 4. `server_udp.py`

**Description:** 
This script acts as a UDP server that sends the `merged_packet.pcapng` file from Laptop 1 (remote) to Laptop 2 (drone).


### 5. `Receiver.py`

**Description:**
The receiver laptop,  with help of receiver.py script, receives the merged_packet.pcapng file which contains hash value and actual command signal which is to be executed on receiving laptop.


### 6. `Extract.py`

**Description:**
This script reads merged_packet.pcapng and extracts the hash value present inside pcapng packet and saves it into new text file `extracted_hash.txt` .

### 7. `Authenticate.py`

**Description:**
This script plays an important role as it authenticates the packet received.
It generates the hash value of command signal present inside the packet , and compares this hash with extracted_hash . If it matches , command is executed , else the command is discarded.
