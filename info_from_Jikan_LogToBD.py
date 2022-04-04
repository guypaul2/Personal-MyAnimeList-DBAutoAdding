import requests
from pprint import pprint
import xlrd
import xlwt
from xlwt import Workbook

loc = ("3_list_manually_cleaned.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

wbOut = Workbook()
sheet1 = wbOut.add_sheet('Sheet 1')

for i in range(sheet.nrows):
    r = requests.get('https://api.jikan.moe/v3/search/anime?q='+sheet.cell_value(i, 2)+'&type=tv&page=1')
    reponse = r.json()

    pprint(sheet.cell_value(i, 0))

    if(i>10000) :
        wbOut.save('4_BD.xls')

    sheet1.write(i, 0, sheet.cell_value(i, 0))
    sheet1.write(i, 1, sheet.cell_value(i, 1))

    sheet1.write(i, 2, reponse['results'][0]['title'])

    sheet1.write(i, 3, sheet.cell_value(i, 2))
    sheet1.write(i, 4, sheet.cell_value(i, 3))
    sheet1.write(i, 5, sheet.cell_value(i, 4))


    sheet1.write(i, 7, reponse['results'][0]['mal_id'])
    sheet1.write(i, 8, reponse['results'][0]['episodes'])
    sheet1.write(i, 9, reponse['results'][0]['airing'])
    sheet1.write(i, 10, reponse['results'][0]['start_date'])
    sheet1.write(i, 11, reponse['results'][0]['end_date'])
    sheet1.write(i, 12, reponse['results'][0]['image_url'])
    sheet1.write(i, 13, reponse['results'][0]['members'])
    sheet1.write(i, 14, reponse['results'][0]['rated'])
    sheet1.write(i, 15, reponse['results'][0]['score'])
    sheet1.write(i, 16, reponse['results'][0]['synopsis'])
    sheet1.write(i, 17, reponse['results'][0]['type'])
    sheet1.write(i, 18, reponse['results'][0]['url'])



wbOut.save('4_BD.xls')
