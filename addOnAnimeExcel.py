import requests
from pprint import pprint
import xlrd
import xlwt
from xlwt import Workbook
import sys
loc = ("3_list_manually_cleaned.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

wbOut = Workbook()
sheet1 = wbOut.add_sheet('Sheet 1')


animeAAdd = ""

for k in range(len(sys.argv)-1):
    animeAAdd = animeAAdd+sys.argv[k+1]+" "
animeAAdd = animeAAdd[:-1]


for i in range(sheet.nrows):

    if(animeAAdd==sheet.cell_value(i, 2)):
        r = requests.get('https://api.jikan.moe/v3/search/anime?q='+sheet.cell_value(i, 2)+'&page=1')
        reponse = r.json()

        pprint(sheet.cell_value(i, 0))
        print('M : ', sheet.cell_value(i, 2))

        print('0 : ', reponse['results'][0]['title'])
        print('1 : ', reponse['results'][1]['title'])
        print('2 : ', reponse['results'][2]['title'])
        print('3 : ', reponse['results'][3]['title'])
        print('4 : ', reponse['results'][4]['title'])
        print('5 : ', reponse['results'][5]['title'])
        print('6 : ', reponse['results'][6]['title'])

        nn = input()
        if(i>10000 or nn=='s') :
            wbOut.save('4_BD.xls')

        sheet1.write(i, 0, sheet.cell_value(i, 0))
        sheet1.write(i, 1, sheet.cell_value(i, 1))

        sheet1.write(i, 2, reponse['results'][int(nn)]['title'])

        sheet1.write(i, 3, sheet.cell_value(i, 2))
        sheet1.write(i, 4, sheet.cell_value(i, 3))
        sheet1.write(i, 5, sheet.cell_value(i, 4))


        sheet1.write(i, 7, reponse['results'][int(nn)]['mal_id'])
        sheet1.write(i, 8, reponse['results'][int(nn)]['episodes'])
        sheet1.write(i, 9, reponse['results'][int(nn)]['airing'])
        sheet1.write(i, 10, reponse['results'][int(nn)]['start_date'])
        sheet1.write(i, 11, reponse['results'][int(nn)]['end_date'])
        sheet1.write(i, 12, reponse['results'][int(nn)]['image_url'])
        sheet1.write(i, 13, reponse['results'][int(nn)]['members'])
        sheet1.write(i, 14, reponse['results'][int(nn)]['rated'])
        sheet1.write(i, 15, reponse['results'][int(nn)]['score'])
        sheet1.write(i, 16, reponse['results'][int(nn)]['synopsis'])
        sheet1.write(i, 17, reponse['results'][int(nn)]['type'])
        sheet1.write(i, 18, reponse['results'][int(nn)]['url'])



try:
  reponse
except NameError:
    r = requests.get('https://api.jikan.moe/v3/search/anime?q='+animeAAdd+'&page=1')
    reponse = r.json()

    pprint(sheet.cell_value(i, 0))
    print('M : ', sheet.cell_value(i, 2))

    print('0 : ', reponse['results'][0]['title'])
    print('1 : ', reponse['results'][1]['title'])
    print('2 : ', reponse['results'][2]['title'])
    print('3 : ', reponse['results'][3]['title'])
    print('4 : ', reponse['results'][4]['title'])
    print('5 : ', reponse['results'][5]['title'])
    print('6 : ', reponse['results'][6]['title'])

    nn = input()
    if(i>10000 or nn=='s') :
        wbOut.save('4_BD.xls')

    sheet1.write(1, 2, reponse['results'][int(nn)]['title'])

    sheet1.write(1, 7, reponse['results'][int(nn)]['mal_id'])
    sheet1.write(1, 8, reponse['results'][int(nn)]['episodes'])
    sheet1.write(1, 9, reponse['results'][int(nn)]['airing'])
    sheet1.write(1, 10, reponse['results'][int(nn)]['start_date'])
    sheet1.write(1, 11, reponse['results'][int(nn)]['end_date'])
    sheet1.write(1, 12, reponse['results'][int(nn)]['image_url'])
    sheet1.write(1, 13, reponse['results'][int(nn)]['members'])
    sheet1.write(1, 14, reponse['results'][int(nn)]['rated'])
    sheet1.write(1, 15, reponse['results'][int(nn)]['score'])
    sheet1.write(1, 16, reponse['results'][int(nn)]['synopsis'])
    sheet1.write(1, 17, reponse['results'][int(nn)]['type'])
    sheet1.write(1, 18, reponse['results'][int(nn)]['url'])
wbOut.save('4_BD.xls')
