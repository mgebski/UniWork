import pandas as pd
import numpy as np
import math
from math import sqrt
#s5111611




def init(train,test, *args):
     
    predicted = decision_tree(train, test, *args)
    return predicted



def branch(node, max_depth, min_size, depth=1):
    
    def first_node(split):
        first_split = [row[-1] for row in split]
        return max(set(first_split), key=first_split.count)
    
    l, r = node['groups']
    
    del(node['groups'])
    if depth >= max_depth:
            node['left'], node['right'] = first_node(l), first_node(r)
            return
    if not l or not r:
            node['left'] = node['right'] = first_node(l + r)
            return
    if len(r) <= min_size:
            node['right'] = first_node(r)
    else:
            node['right'] = split(r)
            branch(node['right'], max_depth, min_size, depth+1)
            
    if len(l) <= min_size:
            node['left'] = first_node(l)
    else:
            node['left'] = split(l)
            branch(node['left'], max_depth, min_size, depth+1)
    
    


def decision_tree(train, test, max_depth, min_size):

    def make_tree(train, max_depth, min_size):
        root = split(train)
        branch(root, max_depth, min_size)
        return root
    
    
    tree = make_tree(train, max_depth, min_size)
    def return_pred():
        def predict(node, row):
            if row[node['i']] < node['value']:
                if isinstance(node['left'], dict):
                    return predict(node['left'], row)
                else:
                        return node['left']
            else:
                    if isinstance(node['right'], dict):
                            return predict(node['right'], row)
                    else:
                            return node['right']
        predictions = list()
        for row in test:
                prediction = predict(tree, row)
                predictions.append(prediction)
        return(predictions)
    return return_pred()
def data_split(i, value, x):
    left, right = list(), list()
    for row in x:
        if row[i] < value:
            left.append(row)  
        else:
            right.append(row)
    return left, right
def split(x,best_index=999
    ,best_value=999
    ,best_score=999
    ,best_groups=None):
    
    
    
    classes = list(set(row[-1] for row in x))
   
    def gini_calculation(groups, classes,gini = 0):
        n_instances = float(sum([len(split) for split in groups]))
        for split in groups:
            size = int(len(split))
            if size == 0:
                    continue
            def score(split,classes,score = 0):
                for class_val in classes:
                        value = [row[-1] for row in split].count(class_val) / size
                        score = score + value * value
                return score
            gini = gini + (1.0 - score(split,classes)) * (size / n_instances)
        return gini
    
    for i in range(len(x[0])-1):
        for row in x:
            data = data_split(i, row[i], x)
            gini = gini_calculation(data, classes) 
            if gini < best_score:
                    best_index = i
                    best_value = row[i]
                    best_score = gini
                    best_groups = data
    return {'i':best_index, 'value':best_value, 'groups':best_groups}




