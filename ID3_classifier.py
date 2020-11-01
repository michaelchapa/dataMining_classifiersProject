import numpy as np
import pandas as pd
# get the iris data. 

def classifier(data, attr_list, attr_select_method):
    # create a node N;
    
    # if ( tuples in D are all of the same class, C, ):
        # return N as a leaf node labeled witht he class C;
        
    # if (attribute_list is empty):
        # return N as a leaf node labeled with the majority class in D; // majority voting
        
    # apply Attribute_selection_method(D, attribute_list) to find the "best" splitting_criterion;
    # label node N w/ splitting_criterion;
    
    # if (splitting_attribute is discrete-valued):
        # attribute_list = attribute_list - splitting_attribute;
        
    # for each outcome (j) of splitting_criterion:
        # // partition the tuples and grow subtrees for each partition
        # let (D of j) be the set of data tuples in D satisfying outcome j; // a partition
        
        # if ((D of j) is empty):
            # attach a leaf labeled with the majority class in D to node N;
        # else:
            # attach the node returned by Generate_decision_tree((D of j), attribute_list) to node N;
            
    # return N;


def main():
    print("Hello")

if __name__ == "__main__":
    main()
