import math
import json
import sys
from script.RNode import RNode

'''
def getIndicesFromCube(arr):
    # just splitting the array into numbers
    cube = [int(arr[i]) * 2 - 1 + int(arr[i + 1]) for i in range(0, len(arr) - 1, 2)]
    index = [0]

    if -1 in cube:
        return index
    for num in cube:
        if (num != 2):
            index = [ind * 2 + num for ind in index]
        else:
            index = [ind * 2 for ind in index] + [ind * 2 + 1 for ind in index]
    return index



    makeArray returns an array of RNodes to represent the leafnodes,
    and calls makeCubes internally


def makeArray(arr, size):
    array = [RNode() for i in range(0, size)]
    for ar in arr:
        indices = getIndicesFromCube(ar)
        for index in indices:
            array[index].var = 'o'
            array[index].id = '1'
    return array


class ROBDD:
    def __init__(self, cubeSet):
        self.root = None
        lim = max([len(word) for word in cubeSet]) / 2
        self.cubeSet = cubeSet

        self.size = int(math.pow(2,lim))
        self.cubeArray = makeArray(self.cubeSet,self.size)

    def ite(self):
        string = ''
        if self.root is not None:
            string = self._ite(self.root)
        return string

    def _ite(self,root):
        string = ''
        if root is not None:
            string = string + 'ite(' + root.var + "," + self._ite(root.r) + "," + self._ite(root.l) + ')'
        return string

    def in_order(self):
        if self.root is not None:
            return self._in_order(self.root)
        return ''

    def _in_order(self, root):
        if root is not None:
            return root.var + self._in_order(root.l) + self._in_order(root.r)
        return '@'

    def traverse(self):
        self.root = self._traverse(self.cubeArray,self.size)[0]

    def _traverse(self,arr,gap):
        #print('gap : ', gap, file=sys.stderr)
        if gap > 1:
            arr = self._traverse(arr, int(gap / 2))
        newArr = []
        hashmap = {}
        #print('the array is ', file=sys.stderr)
        for ar in arr:
            print(ar.var)
        if len(arr) == 1:
            return arr
        for i in range(0, len(arr), 2):
            hashId = arr[i].id + arr[i + 1].id
            if hashId not in hashmap:
                hashmap[hashId] = True
                node = RNode()
                node.id = hashId
                if arr[i].id == arr[i + 1].id:
                    node = arr[i]
                else:
                    node.var = 'x' + str(int(math.log(gap, 2)))
                    node.l = arr[i]
                    node.r = arr[i + 1]
                newArr = newArr + [node]
        return newArr

    # makeJSON spits out the json representation of the robdd
    # to render in the front end.

    def makeJSON(self):
        returnObj = self._makeJSON(self.root)
        defArray =[{'id':'0','label':'zero','group':'diamonds'},{'id':'1','label':'one','group':'diamonds'}]
        returnObj['nodes'] += defArray
        return json.dumps(returnObj)

    def _makeJSON(self, root):
        nodes = []
        edges = []
        if root is not None:
            if root.id is not '0' and root.id is not '1':
                nodes += [{"id":root.id,"label":root.var}]
                edges += [{"from": root.id, "to": root.l.id, "dashes": "true", "arrows": "to"}]
                edges += [{"from": root.id, "to": root.r.id, "arrows": "to"}]
                returnObj = [self._makeJSON(root.l),self._makeJSON(root.r)]
                nodes += returnObj[0]['nodes'] + returnObj[1]['nodes']
                edges += returnObj[0]['edges'] + returnObj[1]['edges']
        return {'nodes' : nodes,'edges':edges}
'''


def makeCubes(arr):
    return [int(arr[i]) * 2 - 1 + int(arr[i + 1]) for i in range(0, len(arr) - 1, 2)]


def getIndicesFromCube(cube):
    cube = makeCubes(cube)
    index = [0]
    for num in cube:
        if (num != 2):
            index = [ind * 2 + num for ind in index]
        else:
            index = [ind * 2 for ind in index] + [ind * 2 + 1 for ind in index]
    return index


def makeArray(arr, size):
    array = [RNode() for i in range(0, size)]
    for ar in arr:
        indices = getIndicesFromCube(ar)
        for index in indices:
            array[index].var = 'o'
            array[index].id = '1'
    return array


def ite(root):
    string = ''
    if root is not None :
        if root.var == 'o':
            string = string + 'return one;'
        elif root.var == 'z':
            string = string + 'return zero;'
        else:
            string = string+'if('+root.var +" is true){"+ ite(root.r)+"}else{" + ite(root.l) + '}'
    return string


def inorder(root):
    if (root != None):
        return root.var + inorder(root.l) + inorder(root.r)
    return '@'


def traverse(arr, gap):
    if (gap > 1):
        arr = traverse(arr, int(gap / 2))
    newArr = []
    hashmap = {}
    if (len(arr) == 1):
        return arr
    for i in range(0, len(arr), 2):
        hashId = arr[i].id + arr[i + 1].id
        #print('hashid:', hashId)
        node = RNode()
        if (hashId not in hashmap):
            hashmap[hashId] = True
            node.id = hashId
            if (arr[i].id == arr[i + 1].id):
                node = arr[i]
            else:
                node.var = 'x' + str(int(math.log(gap, 2)))
                node.l = arr[i]
                node.r = arr[i + 1]
        newArr = newArr + [node]
    for obj in newArr:
        print(obj.var)
    return newArr


'''
cubeset = ['010101', '101010']


array = makeArray(cubeset, size)

for obj in array:
    print(obj.var)

newArr = traverse(array, size - 1)


def makeJSON(root):
    jsonStr = "{"
    if (root != None):
        jsonStr += '"text": { "name": "' + root.var + '"}'
        if (root.var != 'z' and root.var != 'o'):
            jsonStr += ',"children": [' + makeJSON(root.l) + ","
            jsonStr += makeJSON(root.r) + "]"
    jsonStr += '}'
    return jsonStr

'''


def makeJSON(root):
    returnObj = _makeJSON(root)
    defArray = [{'id': '0', 'label': 'zero', 'group': 'diamonds'}, {'id': '1', 'label': 'one', 'group': 'diamonds'}]
    returnObj['nodes'] += defArray
    return json.dumps(returnObj)


def _makeJSON(root):
    nodes = []
    edges = []
    if root is not None:
        if root.id is not '0' and root.id is not '1':
            nodes += [{"id": root.id, "label": root.var}]
            edges += [{"from": root.id, "to": root.l.id, "dashes": "true", "arrows": "to"}]
            edges += [{"from": root.id, "to": root.r.id, "arrows": "to"}]
            returnObj = [_makeJSON(root.l), _makeJSON(root.r)]
            nodes += returnObj[0]['nodes'] + returnObj[1]['nodes']
            edges += returnObj[0]['edges'] + returnObj[1]['edges']
    return {'nodes': nodes, 'edges': edges}
