# printf_checker

programme qui verifie que votre ft_printf a un bon fonctionnement.

## comment ça marche

**le programme va simplement comparer la sortie du vrai printf avec votre ft_printf.**

Ce programme va lire des 'ligne de test' (argument de la fonction printf mis sur une ligne).

#####example de 'ligne de test':

 ```php
 "test1: %s", "yo"
 ```
 on va comparer
 ```php
 printf("test1: %s", "yo")
 ``` 
 à 
 ```php
 ft_printf("test1: %s", "yo")
 ```

#####ou encore:

 ```php
 "test2: %.4d", 59
 ```
 on va comparer
 ```php
 printf("test2: %.4d", 59)
 ```
 à
 ```php
 ft_printf("test2: %.4d", 59)
 ```
 
le programme recupère ces 'lignes de test' dans un **fichier passé en parametre**.

chaque 'ligne de test' est séparé par un retour a la ligne.

exemple du contenu d'un fichier type :

```php
"salut %s, tu as %d ans", "Jean", 12
"%d en hexa c'est %x", 12, 12
"%.32-++0d", 12
...
```

##executer le test

```
$> ./check.py --path PATH_TO_LIBFTPRINTF.A --header PATH_TO_LIBFT.H --file FILE_TO_TEST
```

##note
+ **l'option --file est optionnel**, si vous ne precisez pas cette argument, le script choisira comme fichier le fichier 'examples.txt' fourni avec.
+ **__[!] attention__**, vous ne pouvez mettre de '\n' dans les chaines de characteres de vos lignes de test.
+ pour l'argument path, vous pouvez aussi précisez le nom du dossier ou se trouve votre libftprintf, le programme se chargera de faire le make a votre place.

##contribution

vous pouvez contribuer en apportant vos idées d'amélioration, signaler, corriger un bug. Toute aide est apprécié.
