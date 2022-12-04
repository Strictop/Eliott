

3. Écrire une fonction qui prend en paramètres deux entiers et qui affiche toutes les lettres dont les codes numériques sont compris entre ces deux entiers.


4. Sauriez vous décoder cette exclamation en Binaire : 01000010011100100110000101110110011011110010000000100001 ?

01000-01001-11001-00110-00010-11101-10011-01111-00100-00000-100001

Convertir en hexadecimal:
42 72 61 76 6F 20 21

Convertir ASCII:
Bravo !


5. Peut-on coder cette phrase avec la table ASCII : "un âne est passé par là" (justifier la réponse)


75 6E 20 E2 6E 65 65 73 74 20 70 61 73 73 E9 20 70 61 72 20 6C E0


Exercice 2

1. Quelle est la séquence d'octets qui représente le " é ", et qu'est-ce qui est écrit dans le fichier ?

la séquence qui représente le "é" est: 1110 1001.
En UTF-8 on le code sur deux octets en respectant les précisions apportées dans le tableau ci-dessus.
Les bits imposés sont 110 pour le 1er octet et 10 pour le deuxième, le code du « é » est écrit en commençant par la droite et l’octet de gauche est rempli par des zéros (en italique). 
Voilà ce que l’on obtient : 11000011 10101001 .

2. Si le fichier avait été interprété en latin 1 (table ci-dessous), qu'est-ce qui se serait affiché ?