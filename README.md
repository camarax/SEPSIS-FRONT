# Projet Frontend de l'API de Prédiction du Sepsis

Ce projet contient le code frontend pour l'API de prédiction du sepsis. Il utilise le framework Dash pour créer une interface utilisateur basée sur le langage Python.

## Installation

Pour exécuter l'application frontend, suivez les étapes suivantes :

1. Clonez ce dépôt de code sur votre machine locale.

2. Assurez-vous d'avoir Python 3.7 ou une version ultérieure installée.

3. Installez les dépendances requises en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

4. Exécutez le fichier app.py avec la commande suivante :

```bash
python app.py
```

5. Ouvrez votre navigateur et accédez à l'URL **'http://localhost:8080'** pour voir l'application frontend en cours d'exécution.

## Structure du projet

Le projet est organisé comme suit :

- Le fichier **'app.py'** est le point d'entrée de l'application frontend. Il définit la mise en page de l'application Dash et spécifie les composants à afficher.
- Le répertoire **'components'** contient les composants réutilisables de l'application. Les composants sont des fichiers Python qui définissent les éléments de l'interface utilisateur tels que l'en-tête et le corps de la page.

## Fonctionnalités de l'application

L'application frontend affiche une interface utilisateur simple pour interagir avec l'API de prédiction du sepsis. Elle est composée des éléments suivants :

- **En-tête** : L'en-tête de la page affiche le titre de l'application.
- **Corps** : Le corps de la page contient les champs de saisie des caractéristiques de l'individu et un bouton de prédiction. Lorsque l'utilisateur saisit les caractéristiques et clique sur le bouton de prédiction, l'application envoie une requête à l'API backend pour effectuer la prédiction du sepsis. Le résultat de la prédiction est affiché à l'utilisateur.

## Personnalisation de l'application

Vous pouvez personnaliser l'application frontend en modifiant les composants et les styles CSS. Vous pouvez également ajouter de nouvelles fonctionnalités en ajoutant des éléments à la mise en page et en mettant à jour la logique de l'application dans le fichier **'app.py'**.

## Auteurs

Ce projet a été développé par **Aboubacar CAMARA**, **Aaricia DOMINGUEZ** et **Adrien ALVAREZ** dans le cadre du projet annuel de la classe M1IABD de l'école ESGI. Si vous avez des questions, veuillez nous contacter à l'adresse mail **aa-dz@hotmail.com**, **aboubacar.camara.abk@gmail.com** ou **adrienalvarezzpro@gmail.com**.
