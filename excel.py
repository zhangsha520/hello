import xlrd


book = xlrd.open_workbook('F:\\test.xlsx')

for sheet in book.sheets():
    print(sheet.name)
    she = book.sheet_by_name(sheet.name)
    # print(she)
    # print(she.nrows)
    # print(dir(she))
    for i in range(she.nrows):
        print(she.row_values(i))  # 打印行信息
