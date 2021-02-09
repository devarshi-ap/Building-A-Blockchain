if __name__ == '__main__':
    # blockchain object
    blockchain = Blockchain()
    
    # mine 10 blocks for chain
    for n in range(10):
        blockchain.mine(Block("Block " + str(n + 1)))
    
    # print one block and set head to the next block (removes head essentially, like queues)
    while blockchain.head is not None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next
