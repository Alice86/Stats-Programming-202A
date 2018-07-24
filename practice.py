"""
#############################################################
## Stat 202A - Practice assignment
## Author: Jiayu Wu
## Date: Oct. 2, 2017
## Description: Practice completing a python script and 
## uploading it to CCLE.
#############################################################

#############################################################
## INSTRUCTIONS: Please fill in the missing lines of code
## only where specified. Do not change function names,
## function inputs or outputs. You can add examples at the
## end of the script (in the "Optional examples" section) to
## double-check your work, but MAKE SURE TO COMMENT OUT ALL
## OF YOUR EXAMPLES BEFORE SUBMITTING ("comment out" means 
## put a comment sign in front of your code so it does not 
## execute).
#############################################################
"""

import numpy as np

################
## Function 1 ##
################

def piFun(x):
        
    """ This function takes the input (x), multiplies it by 
    3, then adds pi.
    ....... 
    INPUTS:
    x: A real number 
    """
    y = x*3+np.pi 
    #######################################
    ## FILL IN THE BODY OF THIS FUNCTION ##
    #######################################
    
    ## Function returns output y, a real number
    return(y)
    
    
################
## Function 2 ##
################

def cosFun(x):
    
    """ This function takes the cosine of the input (x), then adds 0.5 to the
    result.
    ....... 
    INPUTS:
    x: A list or array of reals 
    """
    
    #######################################
    ## FILL IN THE BODY OF THIS FUNCTION ##
    #######################################
    y = np.cos(x)+0.5
    
    ## Function returns output y, a list or array of reals
    return(y)    
    
    
########################################################
## Optional examples (comment out before submitting!) ##
########################################################

print piFun(3)
print piFun(-2)
print cosFun([-10, 10])    