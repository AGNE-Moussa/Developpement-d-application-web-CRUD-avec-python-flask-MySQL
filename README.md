# Aperçu du Projet

Ce projet implémente une application web CRUD utilisant Flask et MySQL pour gérer les dossiers des employés.

## Stack Technique

- **Backend** : Flask avec flask-mysqldb
- **Frontend** : Bootstrap 5.2.3
- **Base de données** : MySQL

## Structure de la Base de Données

La base de données utilisée dans ce projet est `ong_db`, avec la table `employes` qui contient les colonnes suivantes :

- **id** (int, auto-incrémenté)
- **nom** (varchar(25))
- **prenom** (varchar(50))
- **salbase** (int)

## Composants de l'Application

### Implémentation Backend

L'application Flask (fichier `app.py`) implémente :

- Configuration de la connexion à la base de données
- Opérations CRUD via les points de terminaison REST
- Gestion des routes pour la gestion des employés

### Vues Frontend

Trois modèles HTML avec style Bootstrap sont utilisés pour l'interface utilisateur :

- **index.html** : Affiche la liste des employés avec options de modification/suppression
- **ajout.html** : Formulaire pour ajouter de nouveaux employés
- **modif.html** : Formulaire pour modifier les employés existants

## Fonctionnalités Clés

- Fonctionnalité CRUD complète
- Interface responsive avec Bootstrap
- Validation des formulaires
- Structure de routage URL claire

## Prérequis Système

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- **Python** avec les packages `Flask` et `flask-mysqldb`
- **Serveur MySQL**
- Un **navigateur web moderne** pour la compatibilité avec Bootstrap

## Étapes d'Installation

1. Installer les packages requis :

```bash
pip install flask
pip install flask-mysqldb
Configurer la connexion MySQL dans le fichier app.py

Créer la structure de la base de données et des tables avec les commandes MySQL :

sql
Copier le code
CREATE DATABASE ong_db;
USE ong_db;

CREATE TABLE employes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(25),
    prenom VARCHAR(50),
    salbase INT
);
Lancer l'application Flask :
bash
Copier le code
python app.py
L'application sera alors accessible dans votre navigateur à l'adresse http://127.0.0.1:5000
