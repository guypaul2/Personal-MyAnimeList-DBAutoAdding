# Personal-MyAnimeList-DataBaseTools
Status : working scrpits, need to add comments

Utilisation de 4 outils pour du formatage de texte, migration d'une liste d'anime 1_original_list.docx sur MyAnimeList (https://myanimelist.net/animelist/simekit) via leur outil d'auto importe nécessitant un format spéciale (5_MyNewAnimeList.xml).

##### 5 fichiers de données (X_...) et 4 scripts pour passer d'un fichiers à un autre :

étape 1 : 1_original_list.docx -> 2_word2txt_correction_done.txt : copier coller manuel pour travailler avec du txt.

étape 2 : 2_word2txt_correction_done.txt -> 3_list_manually_cleaned.xlsx : passage de txt à excel, utilisation de correctionText_to_logCsv.

étape 3 : vérifier 3_list_manually_cleaned.xlsx et ajuster pour ne pas avoir d'erreurs (bon format).

étape 4 : 3_list_manually_cleaned.xlsx -> 4_BD.xls : récuppération des informations liées aux animes via l'API jikan.moe, addOnAnimeExcel.py permet de vérifier chaque anime trouvé par l'API (vérifier à la volée l'anime cherché et celui trouvé), possiblité d'utiliser info_from_Jikan_LogToBD.py pour automatiser mais risque d'avoir des erreurs.

étape 5 : 4_BD.xls -> 5_MyNewAnimeList.xml : formatage au format de BD MyAnimeList pour pouvoir importer 5_MyNewAnimeList.xml sur le site, utilisation de BD_format_MAL.py


### From :
```
...
3-Ueki no housoku 14/20 (50 ep) 
4-Zero no tsukaima 14/20 !!!!!!
...
```

### To : 
```
...
<anime>
		<series_animedb_id>479</series_animedb_id>
		<series_title><![CDATA[Ueki no Housoku]]></series_title>
		<series_type>TV</series_type>
		<series_episodes>51</series_episodes>
		<my_id>0</my_id>
		<my_watched_episodes>51</my_watched_episodes>
		<my_start_date>2013-01-05</my_start_date>
		<my_finish_date>2013-01-06</my_finish_date>
		<my_rated></my_rated>
		<my_score>4</my_score>
		<my_dvd></my_dvd>
		<my_storage></my_storage>
		<my_status>Completed</my_status>
		<my_comments><![CDATA[(50 ep) ]]></my_comments>
		<my_times_watched>0</my_times_watched>
		<my_rewatch_value></my_rewatch_value>
		<my_tags><![CDATA[]]></my_tags>
		<my_rewatching>0</my_rewatching>
		<my_rewatching_ep>0</my_rewatching_ep>
		<update_on_import>1</update_on_import>
	</anime>

	<anime>
		<series_animedb_id>1195</series_animedb_id>
		<series_title><![CDATA[Zero no Tsukaima]]></series_title>
		<series_type>TV</series_type>
		<series_episodes>13</series_episodes>
		<my_id>0</my_id>
		<my_watched_episodes>13</my_watched_episodes>
		<my_start_date>2013-01-07</my_start_date>
		<my_finish_date>2013-01-08</my_finish_date>
		<my_rated></my_rated>
		<my_score>4</my_score>
		<my_dvd></my_dvd>
		<my_storage></my_storage>
		<my_status>Completed</my_status>
		<my_comments><![CDATA[!!!!!!]]></my_comments>
		<my_times_watched>0</my_times_watched>
		<my_rewatch_value></my_rewatch_value>
		<my_tags><![CDATA[]]></my_tags>
		<my_rewatching>0</my_rewatching>
		<my_rewatching_ep>0</my_rewatching_ep>
		<update_on_import>1</update_on_import>
	</anime>
 ...
```
