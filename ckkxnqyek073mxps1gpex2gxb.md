## What is Blockchain Technology? Learn by creating one

# Introduction

**Blockchain** - is a tamper-proof and a shared digital ledger that is used to record data such as payment transactions in a public or private **peer-to-peer network**. All the members in a blockchain network can view those transactions that are relevant to them at any point of time

Blockchain is not just about Bitcoins and cryptocurrencies. It can also be used for databases such as health records.

In this tutorial we are going to explore the basics of blockchain.

For this you’ll only need Python. The blockchain we will be creating is very simplified, we won’t build the full-blown Bitcoin blockchain. Instead we’ll create few functions to add blocks to the chain, transactions, and encrypt so that our data becomes tamper-resistant. So, Let’s dive in!

(Here is how I built a blockchain, and codes are available on [GitHub](https://github.com/ApoorvTyagi/BlockchainPy) if you'd like to follow along).


# Let the fun begin 😉

- To display the data we will use JSON format. The data is stored in a block and the block contains multiple attributes like timestamp etc. To differentiate among multiple blocks we will use fingerprinting.

- The fingerprinting is done by using hash and to be particular we will use the SHA256 hashing algorithm. Every block will contain its own hash and also the hash of the previous block to make the validity of the chain easy.

- This fingerprinting will be done to chain the blocks together. Every block will be attached to the previous block having its hash and to the next block by giving its hash.

- The mining of the new block is done by successfully finding the answer to the proof of work. In our case the difficulty will be 2 i.e Find a number 'N' such that when hashed with the block’s content, it gives a solution(a hash) with 2 leading
0s.

### Step 1: Creating The First Block

We will use the standard JSON format to store data in each block. The data for each block looks something like:

```
{   
    "index": "index_number_of_the_chain",
    "transaction": "block_data", 
    "timestamp": "transaction_time",
    "previous_hash": "hash_of_previous_block_in_ledger",
    "nonce": "nonce_value",
    "hash": "hash_of_current_block"
}
```
Don't worry about "nonce" value right now, we will discuss it later on (in step-3)

To implement this in **Python**, we first create a class "Block" with those attributes -

```
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block = json.dumps(self.__dict__, sort_keys=True).encode()
        return sha256(block).hexdigest()
```
Here, the ```compute_hash``` function is used to hash the contents of any 'block'. 

Hashing each block ensures the security of each one individually, making it extremely difficult to tamper with the data within the blocks. 

Now that we’ve created a skeleton for building a single block, we need a way to chain all our blocks together.

### Step 2 : Coding Your Blockchain

For that let’s create a new class for the blockchain. We need a way to initialize the blockchain, so we define the ```create_genesis_block``` method. This creates an initial block with an index of 0 and a previous hash of 0. We then add this to the list chain that keeps track of each block. 

```
class Blockchain:

    def __init__(self):
        self.new_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "This is the first block of the chain.", time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
```
In the constructor of the class, there are two list - one is ```new_transaction[]``` where we will store any new transaction before mining a block for it & other one is ```chain[]``` which will hold each block of our blockchain.

### Step 3 : Designing a Proof Of Work(PoW) system

The hashing that we are doing so far only gets us part of the way there. As you may see, it is feasible for someone to modify a previous block in the chain and then re-compute each of the following blocks to create another valid chain. To handle this, [Satoshi Nakamoto](https://en.wikipedia.org/wiki/Satoshi_Nakamoto#:~:text=Satoshi%20Nakamoto%20is%20the%20name,devised%20the%20first%20blockchain%20database) developed a proof-of-work system.

The proof-of-work system makes it progressively more difficult to perform the work required to create a new block. This means that someone who modifies a previous block would have to redo the work of that particular block & all of the blocks that follow it. 

The proof-of-work system requires looking for a value that starts with a certain number of zeros when hashed. This value is known as a **nonce ** value. 

The number of leading zeros is known as the **difficulty**. 

In general, the average work required to create a block increases exponentially with the number of leading zero bits therefore, by increasing the difficulty with each new block, we can sufficiently prevent users from modifying previous blocks, since it is practically impossible to redo the following blocks.

To implement this system, we can add a ```proof_of_work``` method in the blockchain class:  
```
difficulty = 2  # difficulty of our PoW algorithm

    @staticmethod
    def find_proof_of_work(block):
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
```
### Step 4 : Mining

Now that we have a system that ensures the security of the entire chain in place, we add a few more methods to the blockchain class in order to put everything all together so that we can actually construct a chain. 

We will initially store the data of each transaction in ```new_transactions[]```. Once we confirm that the new block is a valid proof that satisfies the difficulty criteria we can add it to the ```chain[]``` which stores all the valid blocks of our blockchain. The process of performing the computational work within this system is commonly known as mining.

```
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        previous_hash = self.last_block().hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    @staticmethod
    def is_valid_proof(block, block_hash):
        return block_hash.startswith('0' * Blockchain.difficulty)

    def mine(self):
        if not self.new_transactions:
            return False

        for transaction in self.new_transactions:
            last_block = self.last_block()
            new_block = Block(last_block.index + 1, transaction, time.time(), last_block.hash)
            proof = self.find_proof_of_work(new_block)
            self.add_block(new_block, proof)

        self.new_transactions = []
        return True
```

### Step 5 : REST API For Blockchain

Up to this point, We have seen the fundamentals of creating a blockchain: 

- Define a single block
- Define a blockchain
- Define a proof-of-work system
- Define a mining procedure

In order to play with it, we will need to build an interface through which we can interact with. To do this, I will use Flask to create a REST-API.  Flask is a lightweight web application framework written for Python

```
# Creating the Web App using flask
app = Flask(__name__)

# Create the object of the class Blockchain
blockchain = BlockChain.Blockchain()

def obj_dict(obj):
    return obj.__dict__

@app.route("/mine", methods=["GET"])
def mine_block():
    response = {
        "message": "Failed to mine"
    }

    if blockchain.mine():
        response = {
            "message": "Pending transactions has been added to blockchain after mining new blocks"
        }

    return jsonify(response), 200


@app.route("/get_chain", methods=["GET"])
def display_chain():
    json_string = json.dumps(blockchain.chain, default=obj_dict)
    response = {"chain": json_string, "length": len(blockchain.chain)}
    return jsonify(response), 200


@app.route("/is_valid", methods=["GET"])
def is_valid():
    validity = blockchain.chain_valid(blockchain.chain)

    if validity:
        response = {"message": "The Blockchain is valid."}
    else:
        response = {"message": "The Blockchain is not valid."}
    return jsonify(response), 200


@app.route("/add", methods=["GET"])
def add_new_transaction():
    transaction_data = request.args.get('data')
    response = {
        "message": "Cannot find transaction data"
    }

    if transaction_data:
        blockchain.new_transactions.append(transaction_data)
        response = {
            "message": "Added new transaction"
        }

    return jsonify(response), 200

# Run the flask server on localhost
app.run(host="127.0.0.1", port=5000)
```
Here, we have built 4 endpoints :

- **GET  /mine**

It simply calls out ```mine()``` function which does 3 things 
1. Pick an uncommited transaction from the list of ```new_transation[]```
2. Calculate the Proof of Work
3. Forge the new Block by adding it to the ```chain[]```

- **GET  /get_chain**

It will display the contents of our blockchain so far.

- **GET  /is_valid**

It will be used to check whether our blockchain is valid or not. It does this by calling a new function ```chain_valid()```. It will take our blockchain as a parameter & will iterate over all the blocks to check if the chain is valid by -

1. Checking Previous Hash of each block is Valid or not

2. Checking Validity of Proof of work

The function will look something like this :
```
    def chain_valid(self, chain):
        logger.info('Checking if the chain is valid...')
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            # Checking Previous Hash is Valid or not
            block = chain[block_index]
            if block["previous_hash"] != previous_block.compute_hash():
                return False

            # Checking Validity of Proof of work
            proof = block["proof"]
            if not self.is_valid_proof(block, proof):
                return False

            previous_block = block
            block_index += 1

        return True
```

- **GET  /add?data='your_input_data'**

As you can guess by the end point, this will simply add the data which we will pass as the query parameter into the list of ```new_transactions[]```.


# Congrats! 👏

And that’s a wrap....

I hope that this has inspired you to create something new & has assisted you to understand the underlying technology that powers cryptocurrencies such as Bitcoin and Ethereum. 

I have just illustrated the basic ideas for making your feet wet in the innovative blockchain technology. The project above can still be enhanced by incorporating other features like creating node management and synchronization, signing transactions, adding [merkle trees](https://apoorvtyagi.tech/merkle-tree), etc.
to make it more useful and robust.

If you have any comments or questions, Please share them below and I'd happy to answer.

# Other articles you might like😊

- [How I automated my WhatsApp chats](https://apoorvtyagi.tech/how-i-automated-my-whatsapp-chats) - Implement a chatbot which will reply to the messages to a group or person from your WhatsApp account without your intervention.
- [Containerize your web application & deploy it on Kubernetes](https://apoorvtyagi.tech/containerize-your-web-application-and-deploy-it-on-kubernetes) - In this i have demonstrated how you can containerize an application and get it running in Kubernetes.
- [Different ways to authenticate your APIs](https://apoorvtyagi.tech/different-ways-to-authenticate-your-apis) - Learn about some common ways to secure you APIs access.
- [Let Us Mine!!!](https://apoorvtyagi.tech/let-us-mine) - Learn about what bitcoin mining is & how they are mined. 
- [Merkle Tree](https://apoorvtyagi.tech/merkle-tree) - An amazing data structure like a binary tree but with addition to hash pointers.
