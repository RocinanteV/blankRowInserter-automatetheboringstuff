#! python3
#Create a program blankRowInserter.py that takes two
#integers and a filename string as command line arguments.
#Let’s call the first integer N and the second integer M.
#Starting at row N, the program should insert M blank rows
#into the spreadsheet.
import openpyxl
"""
N = sys.argv[2]  #N int
M = sys.argv[3]  #M int
fileName = sys.argv[4:] #filename, use this notation incase filename is multiple words separated
                        #by a space
"""

N = 2
M = 3
fileName = 'updateProduceSales.xlsx'

wb = openpyxl.load_workbook(fileName)
sheet = wb.active

dataToMove = tuple(sheet['A1':'C3'])
print(dataToMove)



#tuple(sheet['A1':'C3'])














