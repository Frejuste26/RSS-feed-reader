# 📡 DevProjects - RSS Feed Reader in Terminal

Un lecteur de flux RSS léger et rapide, directement dans votre terminal. Tapez l'URL d’un flux RSS, et le programme se charge d’extraire les titres, descriptions et liens — **sans aucune bibliothèque de parsing RSS**. Un défi relevé avec style !

> 💡 Projet proposé par [DevProjects](https://www.codementor.io/projects/tool/rss-feed-reader-in-terminal-atx32jp82q)  
> ✍️ Construit dans l’esprit de l’open source, pour apprendre et partager.

---

## 🛠️ Technologies utilisées

- **Python 3**
- `requests` – pour récupérer le contenu du flux
- `xml.etree.ElementTree` – pour parser le XML manuellement (sans lib RSS)

---

## 📸 Captures d’écran

```bash
=== Lecteur RSS Terminal ===
Entrez l'URL d'un flux RSS (ou 'fin' pour démarrer) : https://www.lemonde.fr/rss/une.xml
Entrez l'URL d'un flux RSS (ou 'fin' pour démarrer) : fin

🔗 Flux: https://www.lemonde.fr/rss/une.xml
------------------------------------------------------------
📰 Titre       : La croissance repart timidement en Europe
📄 Description : Le FMI note un frémissement positif dans les chiffres du T2...
🔗 Lien        : https://www.lemonde.fr/economie/article/2025/07/02/croissance
------------------------------------------------------------
```

---
## 🚀 Installation & utilisation

1. Cloner le projet
```bash
     git clone https://github.com/<votre-utilisateur>/rss-terminal-reader.git
     cd rss-terminal-reader
```
2. Créer un environnement virtuel (optionnel mais recommandé)
```bash
     python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
```
3. Installer les dépendances
```bash
    pip install -r requirements.txt
```

4. Lancer le lecteur RSS
```bash
    python main.py
```

## ✅ Fonctionnalités

-✅ Entrée manuelle de plusieurs flux RSS

-✅ Parsing XML fait à la main

-✅ Affichage dans le terminal : titre, description (tronquée), lien

-✅ Gestion d’erreurs réseau ou de flux invalides

-🚀 À venir (idées d'amélioration) :
  -Interface TUI (curses, rich)
  -Options ligne de commande (argparse)
  -Export JSON ou TXT
  -Favoris ou historique

## 🤝 Contribution
Les contributions sont les bienvenues ! Voici comment :

1.Fork le projet
2.Crée une branche (git checkout -b feature/amélioration)
3.Commit tes changements (git commit -m 'Ajout nouvelle feature')
4.Push (git push origin feature/amélioration)
5.Ouvre une Pull Request 🧠

## 🤝 Contribution
Les contributions sont les bienvenues ! Voici comment :

Fork le projet

Crée une branche (git checkout -b feature/amélioration)

Commit tes changements (git commit -m 'Ajout nouvelle feature')

Push (git push origin feature/amélioration)

Ouvre une Pull Request 🧠

## 👤 Auteur
Kei Prince Frejuste
Développeur web passionné par les solutions élégantes et les terminaux qui causent.
