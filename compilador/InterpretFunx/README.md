# Interpret Funx:

`Funx` és un llenguatge de programació orientat a expressions i funcions. Amb Funx podem definir funcions i acabar, opcionalment, amb una expressió. Es basa en un sistema simple d'entrada i sortida, pensat per
processar calculs sense haber-se de preocupar de la gestió de tipus, nuls, memoria ... Està ideat per facilitar al usuari el màxim possible la programació (Evitant errors inecessàris) dotan-lo d'una practicitat inigualable.




## Especificació:

### Tipus de dades i Estructures de dades:

L'interpret Funx, en la seva cerca de la simplicitat, es va idear amb només un tipus de dades, els `enters` (Evidentment amb imaginació i una bona coneixemtn de programació i computadors es podria crear a partir dels enters, qualsevol estructura de dades imaginable, fins i tot es podria extendre funx per permetre els numeros de coma flotant... Pero Funx es basa en la sensillesa d'ús) els quals son trivialment interpretats a `booleans` de la manera seguent, similar a C/C++:

`TRUE` si es qualsevol numero diferent de 0

`FALSE` altrament

Els unics contenidors que existeixen son les variables,que només poden prendre valors enters i sempre son locals, en el ambit de visibilitat de la  funció on van ser declarades a més a més aquestes variables començen sempre per minuscules. Pel cas dels booleans, existeixen els valors `true` i `false` que son com "macros" de 0 i de 1, pero que donen més expressivitat.

Compta també amb un petit sistema d'excepcions per frenar programes invàlids amb excepcions de mala programació o d'execució com divisió per 0, funcions no definides, funcions cridades amb numero incorrecte de parametres...


### Instruccions:

El llenguatge compta amb moltes instruccions tipiques com bucles, condicionals, assignacions i crides a funcions, en diferents formats, a més a més de molts operadors per evaluar expressions, tots els típics d'altres llenguatges de programació i molts altres que doten de molta riquesa a funx. També compta amb commentaris de linea unica que es poden crear amb `#`.

#### Condicionals
Tenim diverses maneres de crear estructures condicionals les quals evaluen la veracitat d'una expressio per executar un fragment de codi o un altre. Podem crearles amb if's simples, if's i else, i també pot haver un únic else if opcionalment (Un petit afegitó que no demanava l'enunciat), tal com es mostra en les 4 opcions seguents:

 -``` if x%2 = 0 {x} ```

 -``` if x%2 = 0 {x} else {x+1} ```

 -``` if x = 100 {true} else if x = 1000 {false} ```

 -``` if joan = false {joan <- true} else if joan = true {x <- 2} else {x <- -55}```

#### Bucles
Funx opta per diversos tipos de estructures de bucles, com el `while` , el `do while` , i el bucle iterador `for` (El qual potser ascendent o descendent i sempre varien d'una iteracio a la seguent en 1) (Ambdos bucles son petits afegitons que he fet per fer el llenguatge més complert). Aquests bucles for, crean una variable iteradora que es destruida un cop acabat aquest bucle.

-``` while 1 > 0 {x <- 1} ```

-``` do {x <- x + 1} while x < y ```

-``` for(x<- 2^3 to 2^5) {suma <- suma + x} ```

-``` for(i<- n downto 0) {result <- result - i}```

#### Operadors i avaluació d'expressions

Aquest llenguatge compta amb molts operadors clàssics com `+` , `-`, `*`, `/`, `%`, `^` (Exponenciacio), operadors booleans de comparacio `<`, `<=`, `=`, `!=`, `>`, `>=`, operadors booleans llogics `!` (not), `&&`(and), `||` (or), `-->` / `:-` (implicacio) (També tots aquests operadors llogics no es demanaven pero els he afegit per fer mes expressiu el llenguatge).

-``` true :- false``` s'evalua a fals!

-``` 2 ^ 13 ``` s'evalua a 8192

-``` (2%2 = 0) && false ``` s'evalua a fals

-``` !true || (2^10 > 10^2)``` s'evalua a cert

#### Funcions
El punt principal del llenguatge son les funcions, les quals són creades amb un nom que comença en majuscula i una llista de parametres , seguit d'un programa tancat per claudators. Els unics return types que existeixen són void, enter o boolea (Els quals tots son implicits, realment totes les funcions retornen None o un enter, que pot ser interpretat com boolea) que no necessiten keyword `return`, simplement necessiten una avaluació de expressio final. Funx compta amb subrutines i recursivitat, llavors qualsevol funció pot invocar-se a si mateixa o cridar altres funcions durant l'execució d'aquesta. A continuació exemplifico algunes funcions que he creat per demostrar la potència i expressivitat del llenguatge:

```
# Aquesta funcio es el sumatori dels nombres naturals desde 1 fins a n

Sumatori n
{
  suma <- 0
  for( x <- 1 to n+1){
     suma <- suma + x
  }
  suma
}
Sumatori 100
```

```
Out: 5050
```


```
# Funcio O(n) per evaluar un exponent, com podem observar podem fer servir fors de diferents maneres
ExponenciacioLenta x n
{

    result <- 1
    for(i <- n downto 0){
        result <- result * x
    }
    result
}

ExponenciacioLenta 2 16
````

```
Out: 65536
```

```
#La recursivitat es molt util, podem aplicar esquemes algoritmics com Divide & Conquer !
ExponenciacioConrado x n
{
    if n = 0 {1}
    if n = 1 {x}

    v <- ExponenciacioConrado x (n/2)
    if n%2 = 0 {v * v}
    else {v * v * x}
}
ExponenciacioConrado 2 16
```

```
Out: 65536
```

```
# Maxim comu divisor

MCD a b
{
  while a != b
  {
    if a > b
    {
      a <- a - b
    }
    else
    {
      b <- b - a
    }
  }
  a
}

MCD 6 8
```

```
OUT: 2
```


## Nota al Corrector
Primer de tot m'agradaria recalcar que he fet alguns canvis respecte al enunciat, he afegit 3 excepcions noves: excepcio de variable no declarada i excepcio de for mal programat (iteren rangs de nombres buits).

A més a més he afegit diversos bucles com els 2 tipus de fors i el do-while, a més a més de condicionals amb un posible else-if per fer un xic més flexible el programa. Finalment hi han força més operadors dels demanats, però vaig pensar que farien que el llenguatge fos força més complert (Com els operadors llogics).

També m'he ajudat de la famosa inteligencia artificial, `chatgpt` per aprendre i generar la part de flask (La part html l'he desenvolupat de manera un xic més manual) i finalment he comprovat exhaustivament que efectivament el funcionament de la web fos l'esperat (a part de desenes de modificacions i re-estructuracions manuals, pero per començar em va ser util)

Ara explicaré en detall els petits afegitons que he fet a la pràctica:

### operadors llogics:

-`:- / -->`: Aquest operador esta implementat com `lambda a,b: not(a) or b ` el qual es la definicio alternativa de la implicació llogica. Probablement, no serà massa util per la majoria de usuaris, però ho he escrit pensant en programadors llogics. La taula de la veritat que produeix es la de la implicacio llogica. Apela a la nostalgia dels fanàtics de prolog :).

-`&&`: AND llogica, la implementacio en python es trivial, però es extremadament útil per formar condicions complexes a bucles i condicionals , en conjunt amb les altres operacions llogiques.

-`||`: OR llogica, la implementacio en python es trivial, però es extremadament útil per formar condicions complexes a bucles i condicionals , en conjunt amb les altres operacions llogiques.

-`!`: NOT llogica, la implementacio en python es trivial, però es extremadament útil per formar condicions complexes a bucles i condicionals , en conjunt amb les altres operacions llogiques.

### Macros

-`true`: Macro true pel valor enter 1, per millorar la llegibilitat del codi i la reusabilitat.

-`false`: Macro false pel valor enter 0, per millorar la llegibilitat del codi i la reusabilitat.

### Bucles adicionals

-`do{} while()`: bucle alternatiu, afegeix flexibilitat al codi, per no forçar a només usar while's (Personalment els utilitzo força).

-`for(ID <- expr to expr)`: for ascendent amb step 1, crea una variable local amb nom ID. Vaig considerar que a pesar de que no es demanava, era molt util per evitar codi inecessàri. Apela a la nostalgia dels fanàtics del Pascal.

-`for(ID <- expr downto expr)`: for descendent amb step 1, crea una variable local amb nom ID. Vaig considerar que a pesar de que no es demanava, era molt util per evitar codi inecessàri.Apela a la nostalgia dels fanàtics del Pascal.

### Condicionals adicionals
En aquest apartat lo únic que he afegit es la possibilitat de afegir un únic else-if , tant en els if's individuals i els if-else. Per millorar el codi lleugerament.

-`if cond {} else if cond {}`

-`if cond {} else if cond {} else {}`



## Agraiments i Desagraiments
Aquest treball no podria haber sigut possible sense l'ajut de en Gerard Escudero Bakx, del qual vaig aprendre que la gracia de tot,de fet, resideix en les funcions d'ordre superior.
També he d'agrair a l'Alex Herrero Bravo i en Pol Roca (Son del nostre subgrup de lab) per haber-me ajudat amb certs bugs i a entendre com usar flask i jinja.

Aquest treball podria haber sigut acabat molt més ràpid i amb molta més qualitat si no hagues sigut per culpa de Manjaro que rebenta amb una facilitat increible (Gracies comunitat de Arch Linux per res :D )

També espero que en jordi petit arregli aquest exercici https://jutge.org/problems/P87974_ca , ja que si el teu nom es Luca, et diu `hola maca!`
