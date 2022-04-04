# Personal-MyAnimeList-DataBaseTools
Status : working scrpits, need to add comments

Utilisation de 4 outils pour du formatage de texte, migration d'une liste d'anime 1_original_list.docx sur MyAnimeList (https://myanimelist.net/animelist/simekit) via leur outil d'auto importe nécessitant un format spéciale (5_MyNewAnimeList.xml).

### 5 fichiers de données (X_...) et 4 scripts pour passer d'un fichiers à un autre :

1 : 1_original_list.docx -> 2_word2txt_correction_done.txt : copier coller manuel pour travailler avec du txt.
2 : 2_word2txt_correction_done.txt -> 3_list_manually_cleaned.xlsx : passage de txt à excel, utilisation de correctionText_to_logCsv
3 : vérifier 3_list_manually_cleaned.xlsx et ajuster pour ne pas avoir d'erreurs (bon format).
4 : 3_list_manually_cleaned.xlsx -> 4_BD.xls : récuppération des informations liées aux animes via l'API jikan.moe, addOnAnimeExcel.py permet de vérifier chaque anime trouvé par l'API (vérifier à la volée l'anime cherché et celui trouvé), possiblité d'utiliser info_from_Jikan_LogToBD.py pour automatiser mais risque d'avoir des erreurs.
5 : 4_BD.xls -> 5_MyNewAnimeList.xml : formatage au format de BD MyAnimeList pour pouvoir importer 5_MyNewAnimeList.xml sur le site, utilisation de BD_format_MAL.py

