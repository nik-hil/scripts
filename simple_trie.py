class Trie:
    def __init__(self):
        self.node = {}
        self.word = None
        
    def add(self,string):
        node = self.node
        currentNode = None
        for char in string:
            currentNode = node.get(char, None)
            if not currentNode:
                node[char] = Trie()
                currentNode = node[char]
            node = currentNode.node
        currentNode.word = string 

    def find(self, query):
        node = self
        result = []
        for char in query:
            currentNode = node.node.get(char, None)
            if not currentNode:
                return  result
            node = currentNode
        return self.findall(node, result)

    def findall(self, node, result):
        if node.word:
            result.append(node.word)
        for value in node.node.values():
            self.findall(value, result)
        return result

t = Trie()
t.add("cat")
t.add("cats")
t.add("cow")
t.add("camp")
print t.find('c')
print t.find('ca')
print t.find("abcde")
print t.find("cows")
