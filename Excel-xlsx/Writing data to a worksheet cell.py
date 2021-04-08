
import xlsxwriter
wb = xlsxwriter.Workbook('Workbook.xlsx')  ### wb = workbook
ws_1 = wb.add_worksheet('Names')           ### ws = worksheet
ws_2 = wb.add_worksheet('Configs')

#     Style your cells in xlsxwriter using formats   #
style = wb.add_format(
    {
        'bg_color': '#00ff00',
        'font': 'Century',
        'font_size': 20,
        'align' : 'Center',
        'bold': True,
        'border': 6,  # 6 is border style
        'border_color': '#000000'
    }
)

ws_1.write('A1' , 'Names', style)  ## A1 == row 0 column 0
ws_1.write(1, 0, 'Emir')
ws_1.write(2, 0, 'Dino' )
ws_1.write(3, 0, 'Delpiero' )

ws_1.set_column("A:A", 22) ## Just column A will be WIDTHS for 30 , it means FROM column A to : column A
ws_1.set_column(1,5, 20) ##from 1 that is column B until the end of 5 that is column F

wb.close()