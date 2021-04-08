
# Creating workbooks and worksheets in xlsxwriter
### pip install XlsxWriter

import xlsxwriter
wb = xlsxwriter.Workbook( 'New-Workbook.xlsx' )

sheet_1 = wb.add_worksheet('Information')
sheet_2 = wb.add_worksheet('Configs')

#   Writing data to Excel cells in xlsxwriter  #
### option 1
sheet_1.write(
    'A1', 'Emir'
)
### option 2
sheet_1.write(
    0,   # Row 1 as 0 will be row 1 and if it is 1 it will ne row 2
    1,   # Column b
    'Jukovic'
)



wb.close()  # Save and Close the fil