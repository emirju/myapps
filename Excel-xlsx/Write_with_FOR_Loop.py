import xlsxwriter

#Create a file WORKBOOK
wb = xlsxwriter.Workbook('Excel_Workbook.xlsx')

#Create a Worksheet
ws_1 = wb.add_worksheet('Information')

# Creating a Data in Lists
names = ['Emir', 'Dybala', 'Buffon']
numbers = [91 , 10, 77]

# Writing HEADERs
ws_1.write('A1', 'Names')
ws_1.write('B1', 'Numbers')

# Write data to a file 'Excel_Workbook.xlsx'
#ws_1.write('A2', names[0])
#ws_1.write('A3', names[1])
#ws_1.write('A4', names[2])

#ws_1.write('B2', numbers[0])
#ws_1.write('B3', numbers[1])
#ws_1.write('B4', numbers[2])

####  Using the FOR LOOP

for row in ws_1.iter_rows():
    print(row)

wb.close()





