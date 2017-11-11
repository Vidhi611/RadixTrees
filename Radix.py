class RadixNode:
    def __init__(self, k=None):
        """
        Initialize a Radix Tree Node
        :param k: key value of the node (default None)
        """
        self.key = k
        self.children = {}
        self.isLeaf = False

    def leafOrNot(self):
        """
        Check if the node is a leaf or not
        :return: Boolean
        """
        return self.isLeaf

    def __str__(self):
        """
        Specify the string to be returned when the Node is printed
        :return: String
        """
        return self.key

class RadixTree:
    def __init__(self):
        """
        Initialize a Radix Tree
        """
        self.root = RadixNode() # assign null node to root

    def insert(self, x, k):
        """
        Insert a string at the given node
        :param x: node at which specified string is to be inserted
        :param k: string which is to be inserted at the node
        :return: None
        """
        if k == '':
            x.isLeaf = True
            return
        combos = getAllStrings(k)
        for a in combos:
            for b in x.children.keys():
                if a[0] == b[:len(a[0])]:
                    if a[0] != b:
                        x.children[a[0]] = RadixNode(a[0])
                        x.children[a[0]].children[b[len(a[0]):]] = x.children[b]
                        x.children[a[0]].children[b[len(a[0]):]].key = b[len(a[0]):]
                        if a[1][len(a[0]):] != '':
                            x.children[a[0]].children[a[1][len(a[0]):]] = RadixNode(a[1][len(a[0]):])
                            x.children[a[0]].children[a[1][len(a[0]):]].isLeaf = True
                        else:
                            x.children[a[0]].isLeaf = True
                        del x.children[b]
                    else:
                        self.insert(x.children[b], k[len(a[0]):])
                    return
        x.children[k] = RadixNode(k)
        x.children[k].isLeaf = True

    def search(self, x, k):
        """
        Search for a string at the given node
        :param x: node at which specified string is to be searched for
        :param k: string which is to be searched for at the node
        :return: None
        """
        if k == '':
            return x.leafOrNot()
        for a in getAllStrings(k):
            if a[0] in x.children.keys():
                return self.search(x.children[a[0]], k[len(a[0]):])
        return False

    def printTree(self, x, string):
        """
        Print the complete sorted tree
        :param x: node at which leaves are searched for
        :param string: contains the string that is formed by parent nodes of x
        :return: None
        """
        for a in sorted(x.children.keys()):
            if x.children[a].isLeaf:
                print(string + a)
            self.printTree(x.children[a], string + a)

def getAllStrings(string):
    """
    Yield all string instances from index 0, decreasing string length by 1 at each iteration
    :param string: the string whose instances are to be found
    :return: Tuple of strings
    """
    for a in range(len(string), 0, -1):
        yield (string[:a], string)