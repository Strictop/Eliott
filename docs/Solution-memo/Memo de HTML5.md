# Memo de HTML5

## HTML

### Texte

- `<!DOCTYPE html>` : est utilisé pour informer le navigateur de la version du code HTML utilisé dans le document

- `<html lang="fr">` : indique le langage de balises

- `<head>` : toujours entre les balises <html> : informations pour le navigateur mais rien à afficher
    
- `<meta charset="utf-8">` : donne plus d'informations sur la page dont le codage des caractères
Ex : `<meta name="author" content="Prenom NOM">`
    
- `<title>` : titre de la page
Ex: `<title>Les Grenouilles</title>`

- Liens vers des ressources :   
`<link rel="stylesheet" href="style.css">` lien vers une feuille de style en css    
`<script src="script.js"></script>` lien vers un programme en JavaScript
    
- `<body>` : contient tout le reste après avoir fermé la balise `</head>` , tout ce qui est dans cette balise sera visible \

- `<h1>` : ajoute un gros titre \
Ex: `<h1>`Tout sur les grenouilles !`</h1>` \
`<h1>`...`<h6>` = titre de niveau + important au - important \

- `<p>` : paragraphe \
`<br>` : revenir a la ligne
    
- **Mise en évidence des textes**
`<em>` : met un texte en italique \
`<strong>` : met un texte en gras

- **Listes**
`<ul>` : crée une liste non numérotée 
`<li>` : marque chaque élements de la liste
`<ol>` : crée une liste ordonnée/numérotée

- **Images**
`<img>` : ajouter une image \
Ajouter src="{insérez l'url de l'image}" à l'intérieur de la balise `<img>` permet d'identifier la source de l'image \
Ex: `<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.radiofrance.fr%2Ffranceculture%2Fpodcasts%2Fle-monde-vivant%2Fbenitier-et-meteo-la-grenouille-4363598&psig=AOvVaw2aQIKh0BtV8WJpqhpcAQlX&ust=1668507883541000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCJjzhLC6rfsCFQAAAAAdAAAAABAD">` \
Ajouter alt="{insérez un texte}" dans la balise ci dessus permet d'écrire un texte qui peut décrire l'image \
Ajouter width="{insérez une grandeur}" dans la même balise permet de définir la taille du texte

- **Lien hypertexte**
   `<a>` : L'élément HTML `<a>` (pour ancre ou anchor en anglais), avec son attribut href, crée un lien hypertexte vers des pages web, des fichiers, des adresses e-mail, des emplacements se trouvant dans la même page, ou tout ce qu'une URL peut adresser.


## CSS

- **Position de déclaration du code**
    - dans un fichier à part par exemple `style.css`
    - dans le `<head>` entre des balises `<style></style>`
    - dans une balise du `<body>` comme valeur de l'attribut style `<p style="">`

- Sélection par type de balise :  
Indiquez le titre/texte/paragraphe à mettre en forme puis entre deux accolades : \
color:; : permet de changer la couleur d'un texte \
Ex: color: green; / color: rgb(0,127,23);
background-color:; : permet de changer la couleur du fond \
Ex: background-color: green; / background-color: rgb(0,127,23);
    
- Séléction par identifiant :
Dans la balise que vous souhaitez identifer, il faut y écrire id="{insérez un nom pour le paragraphe}" 
Puis écrivez #{identifiant de la balise} pour l'identifier lors de la mise en forme

- Séléction par classe (famille, catégorie personalisée) :
Pour identifier plusieurs paragraphes, il faut écrire class="{insérez un nom en commun à tout les paragraphes}"
Puis écrivez .{identifiant des paragraphes}



## JavaScript



## Les projets WEB 2022
   
| Prenom | Glitch |GitHub|Autre|
| ---- |:----:|:----:|:----:|
| 1- carla     | [lien](https://dashing-scratch-handstand.glitch.me/)|  [lien](URL) | [lien](https://output.jsbin.com/xuhoney) |
| 2-  Eliott   | [Projet web glitch ONF](https://sponge-zigzag-bait.glitch.me)|[Projet web github ONF](https://strictop.github.io/Site-web/)         | [lien](URL) |
| 3-  Léa |                            | [lien](URL)                                  | [lien](URL) |
| 4-  Bastien  | [projet site des forets sur glith](https://jolly-small-resistance.glitch.me/) | [Projet site des forets sur github](https://bastien29600.github.io/site-web/) | [lien](URL) |
| 5-     Matéo |[lien](https://gem-napoleon.glitch.me/)|[lien](https://tenduus.github.io/SiteWeb/)                                  | [lien](URL) |
| 6- Lennie    |          [Projet Web Glitch](https://plain-satin-seaplane.glitch.me)          |         [Projet Web Github](https://lenniegadet.github.io/ProjetWeb/)         | [lien](URL)|
|7- Léah| [Set-card_Rudolphe](https://glitch.com/~mature-eight-silk) | [Set-card_Rudolphe](https://github.com/Leahsamami/Set-card) | [Set-card_Rudolphe](https://codepen.io/webandapp/pen/abqPydx) |   
| 8-     Yann  |                [Boredom site](https://boredom-site.glitch.me/)                |             [Boredom Github](https://yannng1.github.io/Boredom/)              | [lien](URL) |    
| 9- Mathieu   |                [Projet](https://cyber-bubble-judge.glitch.me)                 |               [Projet ](https://math2994.github.io/Projet-Web/)               | [Rien](URL) |    
| 10- Valentin |        [Horloge Mieux](https://horloge-mieux-la-meilleure.glitch.me/)         |   [Horloge Mieux GitHub Edition](https://julioyo.github.io/horloge-mieux/)    | [lien](URL) |  

## Ressources
    
- [KhanAcademy : Introduction à HTML/CSS](https://fr.khanacademy.org/computing/computer-programming/html-css)
- [Le vieux tutoriel du Mur : HTML/CSS/JavaScript](http://api.si.lycee.ecmorlaix.fr/APprentissageHtmlCss/)
- [Site de référence W3School](https://www.w3schools.com/)
- [Tutoriels Alsacreations](http://www.alsacreations.com/apprendre/)
- [Tutoriel OpenClassroom : Apprenez à créer votre site web avec HTML5 et CSS3](https://openclassrooms.com/fr/courses/1603881-creez-votre-site-web-avec-html5-et-css3)