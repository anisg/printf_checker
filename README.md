# printf_checker

programme qui verifie que votre ft_printf a un bon fonctionnement.

## comment ça marche

le programme va lire une 'ligne de test'
et comparer la sortie entre printf et ft_printf.

example de ligne de test:

 ` "test1: %s", "yo"`<-- on va comparer `ft_printf("test1: %s", "yo")` à `printf("test1: %s", "yo")`

ou encore:

 ` "test2: %.4d", 59`<-- on va comparer `ft_printf("test2: %.4d", 59)` à `printf("test2: %.4d", 59)`
 
le programme recupère ces 'lignes de test' dans un **fichier passé en parametre**.

chaque 'ligne de test' est séparé par un retour a la ligne.

exemple de fichier type qu'on passe en parametre :

```
"salut %s, tu as %d ans", "Jean", 12
"%d en hexa c'est %x", 12, 12
"%.32-++0d", 12
...
```

##executer le test

```$> ./check.py --path PATH_TO_LIBFTPRINTF.A --header PATH_TO_LIBFT.H --file FILE_TO_TEST```

##note

+ **__[!] attention__**, vous ne pouvez mettre de '\n' dans les chaines de characteres de vos lignes de test.
+ par defaut, si vous ne precisez pas de fichier en argument, le programme va prendre le fichier test 'examples.txt'
+ pour l'argument path, vous pouvez aussi precisez le nom du dossier ou se trouve votre libftprintf, le programme se chargera de faire le make a votre place.

##contribution

vous pouvez contribuer en apportant vos idées, signaler, corriger un bug. Toute aide est apprécié.
