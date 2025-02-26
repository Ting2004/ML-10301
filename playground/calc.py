############################################################
#                                                          #
# This is a simple terminal-based calculator that supports #
# variable assignment and basic mathematical operations.   #
#                                                          #
# Features:                                                #
# - Variable assignment with eager evaluation (=)          #
# - Lazy evaluation to avoid precision mismatch (:=)       #
# - Supports basic mathematical functions like logit and   #
#   logarithms with different bases                        #
#                                                          #
# made by Ting ^^                                          #
#                                                          #
############################################################
import pprint
import numpy as np
LOCAL = {}


#### user defined math functions

def logit(x):
    return 1/(1+np.exp(-x))

def log(x, base="e"):
    if base == 2:
        return np.log2(x)
    elif base == 10:
        return np.log10(x)
    else:
        return np.log(x)
    


#### evaluation functions

def intro_var(exp):
    if ":=" in exp:
        # lazy 
        var = exp.split(":=")[0].strip()
        val = exp.split(":=")[1].strip()
        LOCAL[var] = val
        return f"{var} := {evaluate(val)}"

    elif "=" in exp:
        # eager
        var = exp.split("=")[0].strip()
        val = exp.split("=")[1].strip()
        res = str(evaluate(val))
        if "function" in res:
            res = res.split(" ")[1]
        LOCAL[var] = res
        return f"{var} = {LOCAL[var]}"
    return "invalid assignment"
    
    

def evaluate(exp):
    if "import" in exp:
        return "plz do not inject malicious code 😢"
    if "=" in exp:
        return intro_var(exp)
    else:
        for var in LOCAL:
            if var in exp:
                exp = exp.replace(var, LOCAL[var])
    try:
        return eval(exp)
    except:
        return evaluate(exp)

if __name__ == "__main__":
    print(" input math expression to evaluate")
    print("use = for eager variable assignment")
    print("use := for lazy variable assignment")
    print("  λλλ functions are values λλλ ")

    exp = input("$ ")
    while exp != "q":
        try:
            if exp == "LOCAL":
                print(">>> ", end="")
                pprint.pprint(LOCAL)
            elif exp == "peppermint candy" or exp == "ppmc":
                print(">>> :)")
            else:
                print(f">>> {evaluate(exp)}")
        except:
            print(f">>> invalid input")
        exp = input("$ ")