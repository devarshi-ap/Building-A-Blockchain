class Blockchain:
    # max you can store in 32bit num is 2^32
    maxNonce = 2 ** 32
    # mining difficulty
    difficulty = 20
    # target hash
    target = 2 ** (256 - difficulty)

    # first block in chain is called the Genesis Block
    block = Block("Genesis")
    head = block

    # adds blocks to chain (kinda like stacks; newest addition is head)
    def add(self, block):
        block.prevHash = self.block.hash()
        block.blockNum = self.block.blockNum + 1

        self.block.next = block
        self.block = self.block.next

    # decides if we can add a block to blockchain or not
    def mine(self, block):
        # from 0 to 2^32
        for n in range(self.maxNonce):
            # is the block's hash less than target
            if int(block.hash(), base=16) <= self.target:
                # add the block to the chain
                self.add(block)
                print(block)
                break
            else:
                # move to next hash block
                block.nonce += 1
