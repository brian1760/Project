import numpy as np
import string
from random import randint, shuffle


def splitDataSet(flowers,classif):
    n = len(flowers)

    train=[]
    valid=[]
    test =[]
    for i in range(n):
        type=randint(0,2)
        if type == 0:
            train.append(i)
        if type == 1:
            valid.append(i)
        if type == 2:
            test.append(i)

    train_set = ( np.array([ np.array(flowers[i]) for i in train ]),
                  np.array([ np.array(classif[i]) for i in train ]) )


    valid_set = ( np.array([ np.array(flowers[i]) for i in valid ]),
                  np.array([ np.array(classif[i]) for i in valid ]) )

    test_set = ( np.array([ np.array(flowers[i]) for i in test ]),
                 np.array([ np.array(classif[i]) for i in test ]) )

    return train_set, valid_set, test_set


def parseDataSet(lines):
    flowers  =[]
    classif  = []
    for line in lines:
        items=line.split(',')
        if len(items) == 5:
            flower = [ float(x) for x in items[:4] ]
            flowers.append(np.array(flower))

            if 'setosa' in items[4]:
                classif.append(0)
            if 'versicolor' in items[4]:
                classif.append(1)
            if 'virginica' in items[4]:
                classif.append(2)
    combined = zip(flowers, classif) # zip the data together
    shuffle(combined) # randomly shuffle it
    flowers2 = map(lambda x: x[0], combined) #return the data back to its previous format
    classif2 = map(lambda x: x[1], combined)

    return splitDataSet(flowers2,classif2)

def processDataSet():
    f=open('iris.data','r')
    lines = f.readlines()
    f.close()

    return parseDataSet(lines)

if __name__ == "__main__":
    train, valid, test = processDataSet()
    print test
