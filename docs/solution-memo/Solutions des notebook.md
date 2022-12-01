# Solutions des notebook

## Binaire

### Tableau de conversions décimal -> binaire
```python
# Solution base Matéo
from IPython.display import Markdown

chaine = "| d | b | h |" + "\n"
chaine += "|:-:" * 3 + "|" + "\n"

for i in range(1,17) :
    chaine += f"| {i} | {bin(i)} | {hex(i)} |" + "\n"
    
for i in [20,50,100,200,255]:
    chaine += f"| {i} | {bin(i)} | {hex(i)} |" + "\n"

Markdown(chaine)  
```




```python
# Solution Mathieu avec slicing
from IPython.display import Markdown

chaine = "| d | b | h |" + "\n"
chaine += "|:-:" * 3 + "|" + "\n"

for i in range(1,17) :
    chaine += f"| {i} | {bin(i)[2:]} | {hex(i)[2:]} |" + "\n"
    
for i in [20,50,100,200,255]:
    chaine += f"| {i} | {bin(i)[2:]} | {hex(i)[2:]} |" + "\n"

Markdown(chaine)  
```


```python
# Autre solution sans slicing
from IPython.display import Markdown

def tronque(texte):
    '''
    Renvoie le texte sans les deux premiers caractères
    '''
    
    
    return 


chaine = "| d | b | h |" + "\n"
chaine += "|:-:" * 3 + "|" + "\n"

for i in range(1,17) :
    chaine += f"| {i} | {tronque(bin(i))} | {tronque(hex(i))} |" + "\n"
    
for i in [20,50,100,200,255]:
    chaine += f"| {i} | {tronque(bin(i))} | {tronque(hex(i))} |" + "\n"

Markdown(chaine)  
```

```python
# Solution Yann (~compliquée...)
from IPython.display import Markdown

chaine = "| dec\ bin | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |" + "\n"
chaine += "|:-:" * 9 + "|" + "\n"

for i in range(1,17) :
    chaine += f"| {i} | {i//128} | {(i%128)//64} | {((i%128)%64)//32} | {(((i%128)%64)%32)//16} | {((((i%128)%64)%32)%16)//8} | {(((((i%128)%64)%32)%16)%8)//4} | {((((((i%128)%64)%32)%16)%8)%4)//2} | {(((((((i%128)%64)%32)%16)%8)%4)%2)//1} | " + "\n"
for i in [20, 50, 100, 200, 255] :
    chaine += f"| {i} | {i//128} | {(i%128)//64} | {((i%128)%64)//32} | {(((i%128)%64)%32)//16} | {((((i%128)%64)%32)%16)//8} | {(((((i%128)%64)%32)%16)%8)//4} | {((((((i%128)%64)%32)%16)%8)%4)//2} | {(((((((i%128)%64)%32)%16)%8)%4)%2)//1} | " + "\n"


Markdown(chaine)
```


```python
## Autre solution
from IPython.display import Markdown

chaine = "| dec\ bin | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |" + "\n"
chaine += "|:-:" * 9 + "|" + "\n"

for i in range(1,17) :
    chaine += f"| {i} | {(i//128)%2} | {(i//64)%2} | {(i//32)%2} | {(i//16)%2} | {(i//8)%2} | {(i//4)%2} | {(i//2)%2} | {(i//1)%2} | " + "\n"
for i in [20, 50, 100, 200, 255] :
    chaine += f"| {i} | {(i//128)%2} | {(i//64)%2} | {(i//32)%2} | {(i//16)%2} | {(i//8)%2} | {(i//4)%2} | {(i//2)%2} | {(i//1)%2} | " + "\n"

Markdown(chaine)
```



## Bases de Python
### ???

```python
## Quelques bases de programmation en Python 3

```
test :):)