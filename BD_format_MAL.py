import requests
from pprint import pprint
import xlrd
import xlwt
from xlwt import Workbook
import datetime
from datetime import timedelta

loc = ("4_BD.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

file1 = open("5_MyNewAnimeList.xml","w")

date = datetime.date(2013, 1, 1)

L = ["<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n",
		"\t<!--\n",
		 "\t\tCreated by XML Export feature at MyAnimeList.net\n",
		 "\t\tProgrammed by Xinil\n",
		 "\t\tLast updated 5/27/2008\n",
		"\t-->\n",
		"\t<myanimelist>\n",
			"\t\t<myinfo>\n",
				"\t\t\t<user_id>6051861</user_id>\n",
				"\t\t\t<user_name>simekit</user_name>\n",
				"\t\t\t<user_export_type>1</user_export_type>\n",
				"\t\t\t<user_total_anime>" + str(sheet.nrows) + "</user_total_anime>\n",
				"\t\t\t<user_total_watching>0</user_total_watching>\n",
				"\t\t\t<user_total_completed>" + str(sheet.nrows) + "</user_total_completed>\n",
				"\t\t\t<user_total_onhold>0</user_total_onhold>\n",
				"\t\t\t<user_total_dropped>0</user_total_dropped>\n",
				"\t\t\t<user_total_plantowatch>0</user_total_plantowatch>\n",
			"\t\t</myinfo>\n\n"]
file1.writelines(L)

for i in range(sheet.nrows):

    if int(sheet.cell_value(i, 4)) > 10 :
        note = str(int(sheet.cell_value(i, 4))-10)
    else :
        note = str(int(sheet.cell_value(i, 4)))

    id = str(int(sheet.cell_value(i, 7)))
    title = str(sheet.cell_value(i, 2))
    type = str(sheet.cell_value(i, 17))
    comments = str(sheet.cell_value(i, 5)).encode('utf-8')

    L = ["\t<anime>\n",
        "\t\t<series_animedb_id>" + str(id) + "</series_animedb_id>\n",
        "\t\t<series_title><![CDATA[" + str(title) + "]]></series_title>\n",
        "\t\t<series_type>" + str(type) + "</series_type>\n",
        "\t\t<series_episodes>" + str(int(sheet.cell_value(i, 8))) + "</series_episodes>\n",
        "\t\t<my_id>0</my_id>\n",
        "\t\t<my_watched_episodes>" + str(int(sheet.cell_value(i, 8))) + "</my_watched_episodes>\n",
        "\t\t<my_start_date>" + str(date) + "</my_start_date>\n",
        "\t\t<my_finish_date>" + str(date + timedelta(days=1)) + "</my_finish_date>\n",
        "\t\t<my_rated></my_rated>\n",
        "\t\t<my_score>" + note + "</my_score>\n",
        "\t\t<my_dvd></my_dvd>\n",
        "\t\t<my_storage></my_storage>\n",
        "\t\t<my_status>Completed</my_status>\n",
        "\t\t<my_comments><![CDATA[" + str(comments)+ "]]></my_comments>\n",
        "\t\t<my_times_watched>0</my_times_watched>\n",
        "\t\t<my_rewatch_value></my_rewatch_value>\n",
        "\t\t<my_tags><![CDATA[]]></my_tags>\n",
        "\t\t<my_rewatching>0</my_rewatching>\n",
        "\t\t<my_rewatching_ep>0</my_rewatching_ep>\n",
        "\t\t<update_on_import>1</update_on_import>\n",
    "\t</anime>\n\n"]
	#date is no sense, juste to keep order of watched anime
    date = date + timedelta(days=1) + timedelta(days=1)

# \n is placed to indicate EOL (End of Line)

    file1.writelines(L)
file1.write("</myanimelist> \n")
file1.close()
