import datetime
from hashlib import sha256


class Block:
    # each block has 7 attributes

    blockNum = 0
    data = None
    next = None
    nonce = 0
    hash = None
    prevHash = 0x0
    timestamp = datetime.datetime.now()

    # init block and store some data
    def __init__(self, data):
        self.data = data

    # hash method which inputs a concatenated string that has 5 of the block's attributes into the algo
    def hash(self):
        # sha256 object h
        h = sha256()

        # updates h w/ a encoded version of the given string using it's metadata
        h.update(
            str(self.nonce).encode(encoding='UTF-8') +
            str(self.data).encode(encoding='UTF-8') +
            str(self.prevHash).encode(encoding='UTF-8') +
            str(self.timestamp).encode(encoding='UTF-8') +
            str(self.blockNum).encode(encoding='UTF-8')
        )
        # returns hexadecimal string of the hash
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNum) + "\nBlock Data: " + str(
            self.data) + "\nHashes: " + str(self.nonce) + "\nTimestamp: " + str(self.timestamp) + "\nPrevious: " + str(self.prevHash) + "\n--------------"
