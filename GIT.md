## Git

Pour définir son nom et mail :
```
git config --global user.name "T. Dupuy"
git config --global user.email t9dupuy@enib.fr
```

Pour récupérer le projet (la première fois), dans un dossier *projet_cpo* (peu importe le nom):
```
git init
git remote add origin https://github.com/t9dupuy/CPO
git pull
```

### Pour commencer à travailler

On récupère la dernière version du projet

```
git checkout master
git pull
```

On créé une nouvelle branche pour faire nos ajouts/modifications (en précisant sur quoi on travaille)
```
git branch titouan-classe-voiture
git checkout titouan-classe-voiture
```

On travaille et on peut regarder quels fichiers ont été modifiés ou ajoutés
```
git status
```

On fait quelques *commits* aux moments importants (avec un message explicit)
```
git add Voiture.cpp Voiture.hpp
git status
git commit -m "Création de la classe Voiture et de son constructeur"
```

### Pour finir de travailler

Une fois finit de travailler on envoie ses modifications
```
git push -u origin titouan-classe-voiture
```

Après cette opération on a la possibilité de créer une **pull request (PR)** sur Github.
Le but d'une PR est de regarder les changements effectuer et du décider ou non d'appliquer les changements faits à la branche principale *master*.

C'est pourquoi si on est pas **sûr** de ses changements on ne fait rien de plus.
