# The value of pi can be estimated using the following infinite series:

# pi/4 = 1 - 1/3 + 1/5 - 1/7 ... 

# 1) Write a Python function computePi4(numTerms) that computes this estimate up to iteration numTerms.

def computePi4(numTerms):
    pi_estimate = 0 # estimate that will be added or subtracted from
    for i in range(0, numTerms): 
        add_to_estimate = (-1)**(i) * (1)/(2*i +1) # compute the term to add or subtract this time
        pi_estimate = pi_estimate + add_to_estimate # add the estimate and the above term
    return pi_estimate


print(computePi4(1000) * 4) # 3.14, estimation is pretty close at numTerms=1000

# 2) Try the above using comprehension syntax . 

def computePi4_comprehension(numTerms):
    approx_pi = sum([(-1)**(i) * (1)/(2*i +1) for i in range(numTerms)]) # list comprehension syntax inside the bracket, then summing the list
    return approx_pi


print(computePi4_comprehension(1000) * 4)  # 3.14, estimation is pretty close at numTerms=1000

# 3) A sequence is a list of objects. Using numTerms as the maximum index into a sequence, 
# one can use computePi4 to compute a sequence to estimate pi/4, 
# where each new number in the sequence is an estimate of pi/4 that "more closely" approaches to the actual value. 
# Write a generator function in Python that generates this sequence using a yield statement (for delayed evaluation).  
# This is similar to #1 except you will be using a yield statement. 

def computePi4_yield(numTerms):
    pi_estimate = 0 # estimate that will be added or subtracted from
    for i in range(0, numTerms): 
        add_to_estimate = (-1)**(i) * (1)/(2*i +1) # compute the term to add or subtract this time
        pi_estimate = pi_estimate + add_to_estimate # add the estimate and the above term
        yield pi_estimate # creates the generator

for approximation in computePi4_yield(10): # going through the generator + printing values
    print(approximation * 4) # 10th value is 3.042, which is closer than the 9th value of 3.252