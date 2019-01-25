#!/usr/bin/python3

import math

print('\n Number of possible character combinations:\n')
# No repeat permutation n!/{n - r)!

print('\t Number of variations in keyspace?')
Password_Type = int(input("\t > ")) # n number
print('\t Length of variations in sequence?')
Password_Length = int(input("\t > ")) # r number  

perms = math.factorial(Password_Type) / math.factorial(Password_Type - Password_Length)

print("\t Password permutation length: \n",perms,"\n")


#
# Efficiency Constant = thread access to NAND output .99 = 99%
#
Efficiency_Constant = 0.99
Number_of_Threads = 64 * 4  
Effective_threads = 1 / ( ( 1 - Efficiency_Constant ) + (Efficiency_Constant/Number_of_Threads) )
Processor_Frequency = 800
GFLOPS = Processor_Frequency * Effective_threads

softwarebrute = GFLOPS/perms 

print("Software bruteforce\t:",softwarebrute,"seconds")

Combinations = perms

print('\n\t Time it takes to enter and submit one password per second: ') 
KeysPerSecond = int(input("\t > "))

Seconds = Combinations*KeysPerSecond

print("Time to bruteforce \t:",Seconds,"Seconds \n")
Minutes = Seconds / 60
print("\t\t\t: ",Minutes,"Minutes")
Hours = Minutes / 60
print("\t\t\t: ",Hours,"Hours")
Days = Hours / 24
print("\t\t\t: ",Days,"Days")
Weeks = Days / 7
print("\t\t\t: ",Weeks,"Weeks")
Months = Weeks / 4
print("\t\t\t: ",Months,"Months \n")