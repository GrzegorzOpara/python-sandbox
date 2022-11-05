import unittest

class Container:
    def __init__(self):
        self.luggae = []
        self.weight = 0

    def loadBag(self, bag):
        self.luggae.insert(0, bag.weight)
        self.weight += bag.weight

    def doesBagFit(self, bag):
        if self.weight + bag.weight < 40:
            return True
        else:
            return False

    def unloadBags(self):
        return self.luggae

class Bag:
    def __init__(self, weight):
        self.weight = weight

class Plane:
    def __init__(self, bagsToLoad):
        self.containers = []
        self.bagsToLoad = bagsToLoad
        # self.bagsToLoad = self.removeWrongBags()

    def loadBagsToConatainers(self):
        container = Container()
        for item in self.bagsToLoad:
            bag = Bag(item)
            if container.doesBagFit(bag) == True:
                container.loadBag(bag)
            else:
                self.loadContainer(container)
                container = Container()
                container.loadBag(bag)

        if container.weight > 0:
            self.loadContainer(container)
        
    def loadContainer(self, container):
        self.containers.insert(0, container) 

    def unloadPlane(self):
        luggae = []
        for container in self.containers:
            luggae += container.unloadBags()
        return luggae

    def removeWrongBags(self):
        self.bagsToLoad = [item for item in self.bagsToLoad if item < 41 and item > 0]


