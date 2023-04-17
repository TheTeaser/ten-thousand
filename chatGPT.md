# What was used from chatGPT:

**Prompt:** 
I want to add a new condition for three pairs Three pairs are worth 1000 points, for instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise.

**chatGPT:** 
        #Three pairs
        if len(counter) == 3 and all(val == 2 for val in counter.values()):
             total_points += 1500
             return total_points