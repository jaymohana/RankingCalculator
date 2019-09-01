import sys
from pathlib import Path
from .calculateRanking import scoreCalculator, compileRanking
from sys import argv

print()
print("|*************************************************|")
print()
print("    WELCOME TO SOCCER LEAGUE RANKING CALCULATOR   ")
print()
print("|*************************************************|")
print()

#file1 = open(input (str("Please enter the name of the file you wish to open:" )),"r")
#f = file(raw_input("Enter filename: "), 'r')
def main():

	file1 = open(input(str("Please enter the absolute file path of the text file of scores: " )),"r")
	scoreCalculator(file1)
	print()
	print("Enter 't' to output the results to a text file (found in the project's home directory), or press Enter to display the results to the console.")
	print()
	x = input("Answer: ").strip()
	print()
	compileRanking(x)

if __name__ == '__main__':
    main()