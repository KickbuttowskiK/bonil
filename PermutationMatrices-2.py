import numpy as np
import math as m

# N is the size of permuted vector and NxN permutation matrices
# You can manipulate this size by changing N
# Please note that the number of permutations
# (and permutation matrices) is N! which grows very fast
# Likely you will be able to run experiments for small values of N
#
N=3

# nextPermutation abd findMaxIndex codes borrowed from
# https://www.tutorialspoint.com/next-permutation-in-python
#
# This class provides all methods used to generate and print
# pemrutation matrices.
#
class Solution(object):
    def nextPermutation(self, nums):
        found = False
        i = len(nums)-2
        while i >=0:
            if nums[i] < nums[i+1]:
                found =True
                break
            i-=1
        if not found:
            nums.sort()
        else:
            m = self.findMaxIndex(i+1,nums,nums[i])
            nums[i],nums[m] = nums[m],nums[i]
            nums[i+1:] = nums[i+1:][::-1]
        return nums

    def findMaxIndex(self,index,a,curr):
        ans = -1
        index = 0
        for i in range(index,len(a)):
            if a[i]>curr:
                if ans == -1:
                   ans = curr
                   index = i
                else:
                   ans = min(ans,a[i])
                   index = i
        return index

    def printMatrix(self,anyMatrix):
        for i in range (len(anyMatrix)):
            print(anyMatrix[i])

    def matrixProduct(self,A,B):
        product = [[0 for i in range(len(A))] for j in range(len(A))]
        for i in range (len(A)):
            for j in range (len(A)):
                product[i][j] = 0
                for k in range (len(A)):
                    if A[i][k]*B[k][j] > 0:
                        product[i][j] = 1
        return(product)

# We create here a toolbox with all methods needed in the solution                    
#    
tools = Solution()

# The main part of the code
#

# Answer related variables
homing_power = []
pMax = 0    # maximum homing power for given N
pAve = 0    # average homing power (mean of homing powers distribution)
Var  = 0    # variance of the distribution
sDev = 0    # standard deviation of the distribution 

# Creation of vector = [0,1,...,N-1]
# Thanks to method nextPermutation we gradually generate 
# all permutations of the sequence of numbers in vector
#
vector = [i for i in range(N)]
print(vector, "permutation #",0)
print("- next permutation matrix")

# Creation of identity matrix with unit rows
#
identityMatrix = [[0 for i in range(N)] for j in range(N)]
for i in range (N):
    identityMatrix[i][i] = 1

# Printing identity matrix
#
print("power=",1)
homing_power.append(1)
tools.printMatrix(identityMatrix)
print("------")

# Initialisation (with 0s) of array permutationMatrix which will host permutation matrices
#
permutationMatrix = [[0 for i in range(N)] for j in range(N)]

# Generation of the next permutation
#
newVector = tools.nextPermutation(vector)
print(vector, "permutation #", 1)
print("- next permutation matrix")

# Use the next permutation to generate the next permutation matrix 
#
for i in range (N):
    permutationMatrix[i] = identityMatrix[newVector[i]]
# and print it including its power
print("power=",1)
tools.printMatrix(permutationMatrix)

# Create the next power of permutation matrix
#
newPermutationMatrix= permutationMatrix
newPermutationMatrix= tools.matrixProduct(newPermutationMatrix,permutationMatrix)
# and print it including its power
print("power=",2)
homing_power.append(2)
tools.printMatrix(newPermutationMatrix)
print("------")

# The first two permutation matrices were special
# The code below generates and prints all remaining permutation matrices including their powers

num = 2

for i in range (m.factorial(N)-2):
#   Create the next permutation stored in newVector
#
    list=[]
    newVector = tools.nextPermutation(newVector)
    print(newVector, "permutation #", num)
    print("- next permutation matrix")
    num += 1

#   Create the next permutation matrix based on newVector
#
    for i in range (N):
        permutationMatrix[i] = identityMatrix[newVector[i]]
    counter = 1
# and print it including its power
    print("power=",counter)
    list.append(counter)
    tools.printMatrix(permutationMatrix)

#   Generate the remaining powers of permutation matrices
#
    newPermutationMatrix= permutationMatrix
    while (newPermutationMatrix != identityMatrix):
        newPermutationMatrix= tools.matrixProduct(newPermutationMatrix,permutationMatrix)
        counter += 1
# and print them including their powers
        print("power=",counter)
        list.append(counter)
        tools.printMatrix(newPermutationMatrix)
    homing_power.append(max(list))
    print("------")

pMax = max(homing_power)
pAve = sum(homing_power) / len(homing_power)
temp_list = []
for i in homing_power:
    var = (i - pAve) ** 2
    temp_list.append(var)
Var = sum(temp_list)/(len(homing_power))
sDev = (Var**0.5)
print("Homing powers distribution, pMax=", pMax, "pAve=", pAve, "Var=", Var, "sDev=", sDev)

