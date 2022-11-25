 HTML : les bases

## Le début du code
<div class="code-example"><pre class="brush: html notranslate"><code><span class="token doctype"><span class="token punctuation">&lt;!</span><span class="token doctype-tag">DOCTYPE</span> <span class="token name">html</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>html</span><span class="token punctuation">&gt;</span></span>
  <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>head</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>meta</span> <span class="token attr-name">charset</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>utf-8<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>title</span><span class="token punctuation">&gt;</span></span>Ma page de test<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>title</span><span class="token punctuation">&gt;</span></span>
  <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>head</span><span class="token punctuation">&gt;</span></span>
  <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>body</span><span class="token punctuation">&gt;</span></span>
    <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;</span>img</span> <span class="token attr-name">src</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>images/firefox-icon.png<span class="token punctuation">"</span></span> <span class="token attr-name">alt</span><span class="token attr-value"><span class="token punctuation attr-equals">=</span><span class="token punctuation">"</span>Mon image de test<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span>
  <span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>body</span><span class="token punctuation">&gt;</span></span>
<span class="token tag"><span class="token tag"><span class="token punctuation">&lt;/</span>html</span><span class="token punctuation">&gt;</span></span>
</code></pre></div>

* **<! DOCTYPE>** est utilisée pour informer le navigateur de la version du code HTML utilisée dans le document.
* **`<html>`** : c'est dans cette balise que sera écrit tous le code en HTML.
* **`<head>`** : c'est dans cette balise que sera écrit toutes les informations concernant le document.
* **`<title>`** : cette balise nosu indique le nom du document.
* **`<meta charset="utf-8">`** : Cet élément définit le jeu de caractères qui devrait être utilisé pour le document et indique que c'est utf-8. utf-8 regroupe l'ensemble des caractères connus utilisés dans les différents langages humains. Généralement, utf-8 permet de gérer n'importe quel texte que vous pourriez utiliser sur la page. Il n'y a pas de raison de ne pas le définir, et il permet d'éviter certains problèmes plus tard.
* **`<body>`** : Cet élément est celui qui contient tout le contenu que vous souhaitez afficher pour qu'il soit vu par les visiteurs : cela peut être du texte, des images, des vidéos, des jeux, des pistes audio jouables, et ainsi de suite.
Pour fermer une balise, il suffit  de mettre un / à la fin :
* **`<test></test>`**

Ces balises sont _communes à tous sites web_ et représente la bases sur laquelle un site se créer.

## Les principales balises 

1. Les titres :
    * **`<h1> - <h6>`** : cette balise permet d'afficher un titre, variant en fonction du chiffre indiqué
2. Les paragraphes : 
    * **`<p>`** : cette balise est utilisée pour contenir des paragraphes
3. Les listes :
    * listes non ordonées : **`<ul>`**
    * listes ordonées : **`<ol>`**
    * pour écrire un élement d'une liste, il faut utiliser la balise **`<li>`** 
    ![liste](https://www.pierre-giraud.com/wp-content/uploads/2019/05/liste-non-ordonnee-html.png)
    Chaque élément d'une liste est balisé avec un élément **`<li>`** (list item)
4. Sauts de ligne : 
    * pour sauter une ligne, il faut utiliser la balise **`<br>`**
5. Les images :
    * pour intégrer une image, il faut utiliser la balises **`<img>`**, elle s'utilise ainsi : `<img src="image.png" alt="nom de l'image (souvent utiliser pour les personnes mal-voyants)" >`

### Source:
   * https://www.pierre-giraud.com/
   * https://developer.mozilla.org/fr/docs/Mozilla
     
    
    
