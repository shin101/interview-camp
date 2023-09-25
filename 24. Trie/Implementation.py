# 208. Implement Trie (Prefix Tree)
# LC Medium

# HINT : track end of word , each letter to have children in hash map
# 



# SOLUTION 

class TrieNode:
    def __init__(self):
        self.children = {} # hashmap
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWOrd = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
    
# For 'apple' Trie children may look like this :

# self.children = {
#     'a': TrieNode({
#         'p': TrieNode({
#             'p': TrieNode({
#                 'l': TrieNode({
#                     'e': TrieNode(endOfWord=True)  # 'e' marks the end of the word
#                 })
#             })
#         })
#     })
# }
