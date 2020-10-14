## Merkle Tree

A merkle tree is a tree founded by Angela Merkel (Chancellor of Germany). Wait...that is something different.🙃

A **merkle tree** is nothing but another data structure like a binary tree but with addition to hash pointers. Now what is a hash pointer?.

The Hash pointers simply points to a place where some data can be stored after being hashed with a cryptographic function to make the data secure. The best example that uses hash pointers are blockchains. 

Now coming back to the merkle tree, data blocks are grouped in pairs and the hash of each of these blocks is stored in a parent node.The parent nodes are in turn grouped in pairs and their hashes stored one level up the tree. This continues all the way up the tree until we reach the root node. 
If an adversary tampers with some data block at the bottom of the tree that will cause the hash pointer that’s one level up to not match, and even if the person continues to tamper with this block, the change will eventually propagate to the top of the tree where they won’t be able to tamper with the hash pointer that we’ve stored.

The below diagram explains the structure:

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1598684766795/6CFEhR4OL.png)

Let's now see the the use cases. There are 3 major system that uses merkle tree as one of their implementations:
- GIT
- Amazon Dynamo DB
- Blockchain

Before we talk about the use cases of merkle tree let's first have a look at some of the operations we can perform and their complexity:
- Search O(logn)
- Traverse  O(n)
- Insertion  O(n)
- Deletion  O(n)

Now let's have a look into one of the use case of Merkle trees which is Amaon DynamoDB:

Amazon's dynamodb is one of the NoSql database which consist of the many nodes in a cluster and these nodes are continuously performing consistent hashing which is a special kind of hashing such that when hash table is resized only K/n keys need to be remapped where K is number of keys and n is number of slots unlike most traditional hash tables where change in a number of slots causes all keys to be remapped. 

Now in order to do consistent hashing we require data migration and at the same time we also want to minimize this data migration. What do think will help in this case?
![trees-man-merkle-trees.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1598705429393/yS8mEc0TP.jpeg)

This can be aceived using merkle trees while checking for inconsistencies among replicas  (merkle trees minimizes the amount of data transfer for synchronization) .

Each node maintains a separate merkle tree for each key range (the set of keys covered by a virtual node) it hosts. This allows nodes to compare whether the keys within a key range are up-to-date. In this scheme, two nodes exchange the root of the merkle tree corresponding to the key ranges that they host in common.

Subsequently, using the tree traversal scheme described above the nodes determine if they have any differences and perform the appropriate synchronization action. The sole disadvantage with this scheme is that many key ranges change when a node joins or leaves the system thereby requiring the tree(s) to be recalculated. 

Advantages of Merkle Tree:

- Tree can hold hash but just need to remeber the hash of the root.
- Can verify the membership in O(logn) time.
- Sorted merkle trees where blocks are ordered at the bottom can verify non 
   membership in O(logn)
- Proof of non-membership: Simply by showing a path to the item that's just before 
   where the item in question would be and showing the path to the item that is just 
   after where it would be.






