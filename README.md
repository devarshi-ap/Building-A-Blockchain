# Learning-Blockchain

### ```About Blockchains```
##### Blockchain is a data structure that was first introduced by Satoshi Nakamoto in the Bitcoin protocol white paper almost a decade ago.

##### A block is a data structure that contains transactions, files or any data you like, really. Much like linkedlists, blocks can be linked- or chained in this case- together to form a blockchain using hashes.
<br>

### ```Hash Algorithms```
##### A hash function is simply a function that takes in input value, and from that input creates an output value deterministic of the input value. The input can be any data- numbers, files, etc. A hash is usually displayed as a hexadecimal number. This has several different purposes including:
- cryptography
- compression
- data indexing
- blockchaining
<br>

*There are many different hash algorithms available such as:*
- md5 (message digest 5)
- NTLM (New Technology LAN Manager)
- SHA-1 (Secure Hashing Algorithm)
- SHA-2
- SHA-256 (used by bitcoin)

##### If you want to learn more about how hash algorithms work click [here](https://www.sciencedirect.com/topics/computer-science/hashing-algorithm)
<br>

### ```Block Data```
##### In this project, I've chosen for each block to hold 7 types of data:
- Block Number (self explanatory) (printed)
- Data Type (for now, I'll just assign this to be "Block [number]") (printed)
- Pointer (pointer to the next block) (not printed)
- Block Hash (created using SHA256 module- deterministic of block's data) (printed)
- Nonce (stands for number used only once; read more about it [here](https://www.investopedia.com/terms/n/nonce.asp#:~:text=A%20nonce%20is%20an%20abbreviation,blockchain%20miners%20are%20solving%20for.) (printed as "hashes")
- Previous Hash (hash of the previous block in the chain; this allows for it's structure) (printed)
- Timestamp (what time the block was added to the chain) (printed)

##### To help you visualize this list:
![media-1313246-blockchainspopenerfigure1-blockcompositiondiagramfromnist](https://user-images.githubusercontent.com/59234436/107436234-444a7d00-6afb-11eb-88ff-8933917ee24a.png)
<br>


## The output of the 3 files put together should look like this.
![Capture](https://user-images.githubusercontent.com/59234436/107551329-22ef9c80-6ba0-11eb-883a-dbc0281eea35.JPG)


