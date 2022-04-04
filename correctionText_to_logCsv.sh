#!/bin/bash

_input="./tri_to_txt_correctionText.txt"
# set IFS (internal field separator) to |
# read file using while loop
id=0
while IFS='-' read -r nb text
do
  id=$((id+1))
  NOM="$(cut -d'/' -f1 <<<"$text")"
  NOTE=${NOM: -2} # take the last 2 char of the string
  NOM=${NOM:: -2} # delete the last 2 char of the string

  COMM="$(cut -d'/' -f2-4 <<<"$text")"
  COMM=${COMM:3} # delete the first 2 char of the string

  echo "ID : $id"
  echo "NB : $nb"
  echo "NOM : $NOM"
  echo "NOTE : $NOTE"
  echo "COMM : $COMM"
  printf "$id\t$nb\t$NOM\t$NOTE\t$COMM\n" >> log.xlsx


done < "$_input"
