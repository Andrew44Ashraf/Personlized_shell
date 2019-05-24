import os 
import sys 

class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

    def all_words(self, prefix):
        if self.end:
            yield prefix

        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        for letter in word:
            node = curr.children.get(letter)
            if not node:
                node = TrieNode()
                curr.children[letter]= node
            curr = node 
        curr.end = True 
   
    def all_words_beginning_with_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return  

        yield from cur.all_words(prefix)

    def addList(self,ls):
        for word in ls:
            self.insert(word)

 

def main():
    onlyfiles = [f for f in os.listdir(os.curdir) if os.path.isfile(os.path.join(os.curdir,f))]
    autocomplete = Trie()
    autocomplete.addList(onlyfiles)
    l = list(autocomplete.all_words_beginning_with_prefix('t'))



if __name__ == "__main__":
    main()