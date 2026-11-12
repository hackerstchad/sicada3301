# SICADA3301

<img width="832" height="1248" alt="OIG4" src="https://github.com/user-attachments/assets/6d7b555e-6df5-44a8-89c7-138aba4e6411" />


![Version](https://img.shields.io/badge/Version-V2-blue)
![Date](https://img.shields.io/badge/Date-2026--2027-lightgrey)
![Auteur](https://img.shields.io/badge/Auteur-Hackerstchad-orange)
![Statut](https://img.shields.io/badge/Statut-En%20d%C3%A9veloppement-green)
![Licence](https://img.shields.io/badge/Licence-%C3%89ducative-brightgreen)

---

## Table des matières

1. [Introduction](#introduction)
2. [Objectifs du projet](#objectifs-du-projet)
3. [Fonctionnalités réelles et avancées](#fonctionnalités-réelles-et-avancées)
4. [Architecture technique](#architecture-technique)
5. [Installation et configuration](#installation-et-configuration)
6. [Utilisation avancée](#utilisation-avancée)
7. [Modules détaillés](#modules-détaillés)
8. [Stéganographie et dissimulation de données](#stéganographie-et-dissimulation-de-données)
9. [Cryptographie et déchiffrement](#cryptographie-et-déchiffrement)
10. [Analyse linguistique et symbolique](#analyse-linguistique-et-symbolique)
11. [Réseaux et anonymat numérique](#réseaux-et-anonymat-numérique)
12. [Géolocalisation et investigation physique](#géolocalisation-et-investigation-physique)
13. [Intelligence artificielle et analyse automatisée](#intelligence-artificielle-et-analyse-automatisée)
14. [Recherche et investigation numérique](#recherche-et-investigation-numérique)
15. [Bibliothèques et ressources](#bibliothèques-et-ressources)
16. [Livres recommandés](#livres-recommandés)
17. [Liens de ressources avancées](#liens-de-ressources-avancées)
18. [Communauté et contributions](#communauté-et-contributions)
19. [Feuille de route](#feuille-de-route)
20. [Conclusion](#conclusion)

---

## Introduction

**SICADA3301** est une plateforme d’investigation numérique, de cryptanalyse et de stéganographie conçue pour l’analyse approfondie de défis complexes tels que ceux inspirés par **Cicada 3301**. Ce projet pédagogique et de recherche propose une suite d’outils modulaires permettant d’explorer, décoder, décrypter et corréler des indices numériques, symboliques, linguistiques, géographiques et cryptographiques.

Le nom **SICADA3301** incarne une synthèse entre la rigueur scientifique, l’investigation numérique et la tradition énigmatique des puzzles ouverts sur Internet. Il ne s’agit pas d’un jeu, mais d’un environnement d’apprentissage et d’expérimentation pour chercheurs, analystes, étudiants en cybersécurité et passionnés de cryptologie.

Ce document constitue la référence complète du projet. Il détaille chaque module, chaque fonctionnalité, les méthodes utilisées, les exemples d’utilisation, les ressources bibliographiques et les liens externes permettant d’approfondir chaque discipline.

---

## Objectifs du projet

Les objectifs fondamentaux de **SICADA3301** sont multiples :

- Fournir un cadre unifié pour l’analyse de messages et de fichiers suspects.
- Permettre la dissimulation et l’extraction de données cachées par stéganographie.
- Proposer une boîte à outils cryptographiques couvrant les classiques et les approches modernes.
- Automatiser l’analyse linguistique, symbolique et fréquentielle.
- Explorer les dimensions réseau, anonymat et OSINT associées aux énigmes numériques.
- Intégrer des techniques d’intelligence artificielle pour la reconnaissance et la classification.
- Offrir une base de connaissances structurée via des ressources, livres et liens avancés.
- Permettre l’analyse collaborative et la documentation rigoureuse des découvertes.
- Servir de support pédagogique pour l’apprentissage de la cryptographie et de la forensique numérique.

---

## Fonctionnalités réelles et avancées

Le projet couvre sept grands domaines fonctionnels :

1. **Stéganographie et dissimulation de données**
2. **Cryptographie et déchiffrement**
3. **Analyse linguistique et symbolique**
4. **Réseaux et anonymat numérique**
5. **Géolocalisation et investigation physique**
6. **Intelligence artificielle et analyse automatisée**
7. **Recherche et investigation numérique**

Chaque domaine est implémenté sous forme de modules indépendants et interconnectés, exploitables via une interface en ligne de commande, une API web ou des scripts Python.

---

## Architecture technique

SICADA3301 repose sur une architecture modulaire en couches :

```
┌─────────────────────────────────────────────────────────────┐
│                    Interface utilisateur                     │
│         (CLI riche, API REST, interface web optionnelle)     │
├─────────────────────────────────────────────────────────────┤
│                     Moteur d’orchestration                   │
│              (gestion des pipelines, logs, cache)            │
├─────────────────────────────────────────────────────────────┤
│  Stégano  │  Crypto  │  Linguistique  │  OSINT  │  ML/AI   │
├─────────────────────────────────────────────────────────────┤
│           Bibliothèques scientifiques et réseau              │
│   OpenCV, Pillow, NumPy, SciPy, Cryptodome, scapy, tor       │
├─────────────────────────────────────────────────────────────┤
│                      Système de fichiers                     │
│              (images, audio, binaires, archives)             │
└─────────────────────────────────────────────────────────────┘
```

---

## Installation et configuration

### Prérequis

- Python 3.11+
- pip
- Git
- Outils externes optionnels : `steghide`, `outguess`, `binwalk`, `sonic-visualiser`, `torsocks`

### Installation rapide

```bash
git clone https://github.com/hackerstchad/sicada3301.git
cd sicada3301
python -m pip install --upgrade pip
pip install click rich tqdm colorama pydantic Pillow opencv-python numpy scipy matplotlib scikit-image stegano cryptography pycryptodome rsa librosa soundfile exifread hachoir binwalk pytesseract tensorflow torch transformers scikit-learn requests stem pgpy pyyaml python-magic qrcode pyzbar pycountry lxml beautifulsoup4
python sicada.py --help
```

---

## Utilisation avancée

### Lancement de l’interface principale

```bash
python sicada.py --mode interactive
```

### Exemple : analyse stéganographique complète

```bash
python sicada.py --module stegano --input image.jpg --full-analysis
```

### Exemple : déchiffrement multi-couches

```bash
python sicada.py --module crypto --input message.txt --layers 3
```

### Exemple : investigation OSINT

```bash
python sicada.py --module osint --target "indice" --depth 2
```

---

## Modules détaillés

Le projet est organisé en modules spécialisés. Chaque module expose des commandes, des fonctions Python et des rapports structurés.

---

## Stéganographie et dissimulation de données

### Dissimulation de messages dans des images

Le module permet d’insérer un message textuel ou binaire dans une image en utilisant plusieurs techniques :

- **LSB (Least Significant Bit)** : modification des bits de poids faible des pixels.
- **LSB amélioré** : répartition pseudo-aléatoire basée sur une clé.
- **Insertion dans la palette** : pour les images PNG et GIF indexées.
- **Insertion par bloc DCT** : pour les images JPEG.

Exemple d’utilisation :

```python
from sicada.stegano import hide_lsb, extract_lsb

hide_lsb('input.png', 'output.png', b'message secret', seed=12345)
message = extract_lsb('output.png', seed=12345)
```

### Extraction de données cachées dans des fichiers JPEG

Analyse approfondie des fichiers JPEG pour détecter :

- Données après le marqueur EOI (`FF D9`).
- Segments COM, APPn suspects.
- Tables de quantification modifiées.
- Données encodées dans les coefficients DCT.

```bash
python sicada.py --module stegano --input image.jpg --extract-jpeg
```

### Analyse des métadonnées EXIF

Lecture, modification et analyse des métadonnées EXIF pour détecter les anomalies, coordonnées GPS, dates, appareils et logiciels.

```python
from sicada.stegano import analyze_exif
report = analyze_exif('photo.jpg')
```

### Analyse de spectrogrammes audio

Génération et analyse de spectrogrammes pour détecter des images ou des messages cachés dans la bande sonore.

```bash
python sicada.py --module audio --input track.wav --spectrogram
```

### Dissimulation de messages dans des fichiers WAV et MP3

- **WAV** : dissimulation LSB sur les échantillons audio.
- **MP3** : encodage dans les coefficients de fréquence ou données ID3.

```python
from sicada.audio import hide_wav, extract_wav
hide_wav('input.wav', 'output.wav', b'data')
```

### Analyse de fichiers PNG et GIF

- Vérification des chunks PNG (IHDR, IDAT, IEND, chunks textuels).
- Détection de chunks anonymes ou inconnus.
- Analyse des trames GIF et données entre trames.

### Détection de données ajoutées à la fin des fichiers

Le module détecte les données ajoutées après la fin logique d’un fichier, quelle que soit la nature du conteneur.

```bash
python sicada.py --module stegano --input file.bin --trailing-data
```

### Analyse des transformations fréquentielles DCT

Transformation en cosinus discrète pour détecter des anomalies dans les images JPEG et extraire des messages encodés dans le domaine fréquentiel.

```python
from sicada.stegano import dct_analysis
result = dct_analysis('image.jpg')
```

### Utilisation d’OutGuess

Intégration de l’outil `outguess` pour dissimuler et extraire des messages dans les images JPEG.

```bash
outguess -k "motdepasse" -d message.txt image.jpg out.jpg
outguess -k "motdepasse" -r out.jpg message.txt
```

### Utilisation de Steghide

Intégration de `steghide` pour le chiffrement et la dissimulation dans JPEG, BMP, WAV et AU.

```bash
steghide embed -cf image.jpg -ef secret.txt -p passphrase
steghide extract -sf image.jpg -p passphrase
```

### Analyse avec Binwalk

Extraction automatique de signatures, de fichiers embarqués et d’archives cachées.

```bash
binwalk -e image.jpg
python sicada.py --module stegano --input firmware.bin --binwalk
```

### Analyse audio avec Sonic Visualiser

Génération de fichiers compatibles Sonic Visualiser pour inspection manuelle des couches audio.

---

## Cryptographie et déchiffrement

### Chiffrement AES

Implémentation AES-256 en modes ECB, CBC, GCM, CTR avec gestion automatique des IV et authentification.

```python
from sicada.crypto import aes_encrypt, aes_decrypt
ct = aes_encrypt(b'clef', b'message', mode='GCM')
pt = aes_decrypt(b'clef', ct, mode='GCM')
```

### Chiffrement RSA

Génération de paires de clés, chiffrement, déchiffrement, signature et vérification PKCS#1 OAEP.

```python
from sicada.crypto import rsa_generate, rsa_encrypt, rsa_decrypt
key = rsa_generate(4096)
```

### Chiffrement XOR

Chiffrement et cassage par force brute, analyse de répétition et clef candidate.

```python
from sicada.crypto import xor_encrypt, xor_bruteforce
```

### One-Time Pad (OTP)

Génération de pads cryptographiquement sécurisés, chiffrement et vérification d’unicité.

### Cryptographie à clé publique

Gestion des certificats, échanges de clés Diffie-Hellman, signatures numériques.

### Analyse fréquentielle

Analyse des occurrences de lettres, bigrammes, trigrammes pour casser les substitutions.

```python
from sicada.crypto import frequency_analysis
report = frequency_analysis('cipher.txt')
```

### Analyse de substitutions alphabétiques

Détection et résolution de chiffres par substitution monoalphabétique.

### Détection de chiffrements classiques

Identifier automatiquement César, Vigenère, Atbash, Playfair, Hill, Beaufort, etc.

### Cryptanalyse de textes inconnus

Pipeline de reconnaissance de langue, de structure et de méthode de chiffrement probable.

### Déchiffrement de messages en plusieurs couches

Appliquer successivement plusieurs décodages (base64, hex, ROT, substitution, AES, etc.).

```bash
python sicada.py --module crypto --input layers.txt --layers 5
```

### Analyse de symboles et alphabets anciens

Reconnaissance et transcription de runes, hiéroglyphes, alphabets anciens et alphabets inventés.

### Cryptographie post-quantique

Introduction aux algorithmes résistants aux attaques quantiques : lattice-based, hash-based, code-based.

---

## Analyse linguistique et symbolique

### Décryptage de runes anglo-saxonnes

Transcription automatique des runes anglo-saxonnes (futhorc) vers latin.

```python
from sicada.linguistics import runes_to_latin
print(runes_to_latin('ᚠᚢᚦ'))
```

### Analyse du Liber Primus

Outils dédiés à l’étude du Liber Primus : segmentation, runes, Vigenère, comparaison avec corpus.

### Reconnaissance de caractères

OCR local avec Tesseract et modèles personnalisés pour les symboles non latins.

```python
from sicada.vision import ocr_image
text = ocr_image('runes.png')
```

### Analyse de textes multilingues

Détection de langue, traduction assistée, alignement de textes parallèles.

### Recherche de références littéraires

Correspondance avec des corpus littéraires, philosophiques et historiques.

### Analyse de citations philosophiques

Extraction et analyse de citations, reconnaissance d’auteurs, contextes historiques.

### Détection de messages acrostiches

Détection de messages cachés formés par les premières lettres de vers ou paragraphes.

### Analyse de structures grammaticales

Parsing syntaxique, détection d’patterns, anomalies stylistiques.

### Comparaison de symboles

Mesure de similarité entre glyphes, clusterisation, reconnaissance de motifs.

### Analyse de textes générés artificiellement

Détection de textes produits par IA via des marqueurs statistiques et modèles de classification.

---

## Réseaux et anonymat numérique

### Compréhension du réseau Tor

Documentation et outils pour comprendre le routage en oignon, les noeuds, les ponts.

### Analyse de services onion

Résolution, scraping sécurisé et analyse de métadonnées de services cachés Tor.

### Communication IRC

Client IRC intégré pour suivre des canaux, enregistrer des conversations et détecter des indices.

### Analyse de protocoles réseau

Capture et analyse de paquets avec scapy, reconstruction de flux, détection d’anomalies.

### Utilisation de PGP

Génération de clés PGP, chiffrement, déchiffrement, vérification de signatures.

```python
from sicada.network import pgp_sign, pgp_verify
```

### Vérification de signatures numériques

Vérification de signatures RSA, ECDSA, Ed25519, PGP.

### Analyse de transactions Bitcoin publiques

Exploration de la blockchain Bitcoin, corrélation d’adresses, recherche de messages OP_RETURN.

### Recherche OSINT

Agrégation de sources ouvertes : moteurs de recherche, réseaux sociaux, archives web, Whois, DNS.

### Analyse de journaux de connexion

Parsing de logs, détection de patterns, cartographie d’attaques.

### Compréhension des mécanismes d’anonymisation

Étude des VPN, proxy, mixnets, Tor, I2P, Freenet et limitations de chaque approche.

---

## Géolocalisation et investigation physique

### Décodage de coordonnées GPS

Extraction de coordonnées EXIF, conversion entre formats DMS et décimal.

```python
from sicada.geo import exif_to_coords
print(exif_to_coords('photo.jpg'))
```

### Analyse de coordonnées géographiques

Recherche de lieux, calcul de distances, regroupement de points, détection de motifs géométriques.

### Reconnaissance de lieux à partir de photographies

Identification de monuments, paysages et éléments architecturaux.

### Analyse de QR codes

Lecture, génération et décodage de QR codes, y compris ceux encodant des données binaires.

### Recherche d’affiches physiques

Documentation et outils pour localiser et analyser des affiches ou plaques liées à des énigmes.

### Corrélation entre indices numériques et lieux réels

Croisement de données textuelles, visuelles et géographiques.

### Analyse de cartes

Superposition de cartes, détection de symboles, extraction de coordonnées.

### Recherche d’indices géographiques historiques

Analyse de cartes anciennes, toponymie, évolution urbaine.

---

## Intelligence artificielle et analyse automatisée

### Reconnaissance optique de caractères (OCR)

OCR avancé avec Tesseract, EasyOCR et modèles personnalisés.

```python
from sicada.ml import ocr
print(ocr('symbols.png'))
```

### Classification de symboles

Entraînement et inférence de classificateurs de symboles par deep learning.

### Détection de motifs répétitifs

Détection de patterns récurrents dans textes, images et séquences binaires.

### Analyse statistique de textes

Calcul d’entropie, indice de coincidence, longueur de clef estimée, tests de randomité.

### Reconnaissance de langues

Identification automatique de la langue d’un texte chiffré ou en clair.

### Comparaison automatique de séquences

Alignement de séquences, distance de Levenshtein, similarité cosinus.

### Détection d’anomalies dans des fichiers

Isolation Forest, autoencodeurs, statistiques pour détecter des zones suspectes.

### Analyse assistée par machine learning

Suggestions automatiques de méthodes de décodage et de clefs probables.

### Génération d’hypothèses cryptographiques

Génération de scénarios et de pipelines de transformation possibles.

---

## Recherche et investigation numérique

### OSINT

Cadre structuré pour la recherche en sources ouvertes.

### Analyse de fichiers binaires

Hexdump, extraction de chaînes, entropie, reconnaissance de formats.

### Recherche inversée d’images

Intégration avec des moteurs de recherche d’images inversées.

### Analyse des métadonnées

Extraction centralisée des métadonnées de documents, images, audio et vidéo.

### Recherche de références historiques

Base de données et moteur de recherche de références historiques et culturelles.

### Vérification de signatures PGP

Validation de signatures et de chaînes de confiance.

### Analyse de fichiers multimédias

Analyse vidéo, audio, image avec rapports consolidés.

### Corrélation de plusieurs indices

Fusion de plusieurs sources d’indices en un graphe de connaissances.

### Documentation des découvertes

Génération automatique de rapports Markdown et JSON.

---

## Bibliothèques et ressources

Les bibliothèques principales utilisées par SICADA3301 couvrent les domaines suivants :

- **Image et stéganographie** : Pillow, OpenCV, NumPy, SciPy, scikit-image, stegano.
- **Audio** : librosa, soundfile, wave.
- **Cryptographie** : cryptography, pycryptodome, rsa.
- **Métadonnées et forensique** : exifread, hachoir.
- **Analyse binaire** : binwalk, python-magic.
- **OCR et IA** : pytesseract, tensorflow, torch, transformers, scikit-learn.
- **Réseau et anonymat** : requests, stem, pgpy.
- **Utilitaires** : click, rich, tqdm, colorama, pydantic, pyyaml, qrcode, pyzbar, pycountry, lxml, beautifulsoup4.

---

## Livres recommandés

### Cryptographie

- **Cryptography Engineering** — Ferguson, Schneier, Kohno
- **Serious Cryptography** — Jean-Philippe Aumasson
- **Applied Cryptography** — Bruce Schneier
- **Handbook of Applied Cryptography** — Menezes, van Oorschot, Vanstone
- **Understanding Cryptography** — Christof Paar, Jan Pelzl
- **Introduction to Modern Cryptography** — Katz, Lindell
- **Real-World Cryptography** — David Wong

### Stéganographie

- **Information Hiding: Steganography and Watermarking** — Katzenbeisser, Petitcolas
- **Steganography in Digital Media** — Jessica Fridrich
- **Disappearing Cryptography** — Peter Wayner
- **Digital Watermarking and Steganography** — Ingemar Cox

### Analyse linguistique et symbolique

- **The Book of Runes** — Ralph Blum
- **Runes: A Handbook** — Michael P. Barnes
- **The Voynich Manuscript** — Raymond Clemens
- **The Code Book** — Simon Singh
- **The Riddle of the Labyrinth** — Margalit Fox

### OSINT et investigation

- **Open Source Intelligence Techniques** — Michael Bazzell
- **Extreme Privacy** — Michael Bazzell
- **Hiding from the Internet** — Michael Bazzell
- **OSINT Tools and Resources Handbook** — Sector035

### Réseaux et anonymat

- **Tor and the Dark Art of Anonymity** — Lance Henderson
- **Applied Network Security Monitoring** — Chris Sanders, Jason Smith
- **The Art of Deception** — Kevin Mitnick
- **Silence on the Wire** — Michal Zalewski

### Intelligence artificielle

- **Deep Learning** — Ian Goodfellow, Yoshua Bengio, Aaron Courville
- **Pattern Recognition and Machine Learning** — Christopher Bishop
- **Hands-On Machine Learning** — Aurélien Géron
- **Mathematics for Machine Learning** — Deisenroth, Faisal, Ong

---

## Liens de ressources avancées

### Documentation officielle

- [Python Cryptography](https://cryptography.io/en/latest/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Scapy Documentation](https://scapy.readthedocs.io/)

### Outils de stéganographie

- [Steghide](http://steghide.sourceforge.net/)
- [OutGuess](https://www.outguess.org/)
- [OpenStego](https://www.openstego.com/)
- [zsteg](https://github.com/zed-0xff/zsteg)
- [stegsolve](https://github.com/zardus/ctf-tools/tree/master/stegsolve)

### Outils de cryptanalyse

- [CyberChef](https://gchq.github.io/CyberChef/)
- [dCode](https://www.dcode.fr/)
- [Rumkin Cipher Tools](http://rumkin.com/tools/cipher/)
- [Cryptool](https://www.cryptool.org/)

### OSINT

- [OSINT Framework](https://osintframework.com/)
- [Bellingcat](https://www.bellingcat.com/)
- [Shodan](https://www.shodan.io/)
- [Censys](https://censys.io/)
- [Internet Archive](https://archive.org/)

### Bitcoin et blockchain

- [Blockchain.com Explorer](https://www.blockchain.com/explorer)
- [Blockchair](https://blockchair.com/)
- [OXT](https://oxt.me/)

### Réseau Tor

- [Tor Project](https://www.torproject.org/)
- [Tor Metrics](https://metrics.torproject.org/)
- [Ahmia](https://ahmia.fi/)

### Cicada 3301 et énigmes

- [Cicada 3301 Wiki](https://uncovering-cicada.fandom.com/)
- [Reddit r/cicada](https://www.reddit.com/r/cicada/)
- [Liber Primus Archive](https://www.libera-primus.com/)
- [Cicada Solvers](https://github.com/cicada-solvers)

### Apprentissage et CTF

- [OverTheWire](https://overthewire.org/wargames/)
- [Cryptohack](https://cryptohack.org/)
- [CTFtime](https://ctftime.org/)
- [PicoCTF](https://picoctf.org/)

---

## Communauté et contributions

Les contributions sont les bienvenues sous forme de rapports de bug, de propositions de fonctionnalités et de pull requests. Chaque contribution doit respecter les objectifs éducatifs et éthiques du projet.

---

## Feuille de route

- [x] Architecture modulaire initiale
- [x] Module stéganographie de base
- [x] Module cryptographie classique
- [x] Analyse linguistique et symbolique
- [x] OSINT et investigation numérique
- [x] Géolocalisation et QR codes
- [ ] Intégration complète de l’IA
- [ ] Interface web collaborative
- [ ] Graphe de connaissances des indices
- [ ] Support multilingue renforcé
- [ ] Documentation interactive

---

## Conclusion

**SICADA3301** est une plateforme d’investigation numérique complète, modulaire et évolutive. Elle offre un environnement structuré pour explorer la stéganographie, la cryptographie, l’analyse linguistique, l’OSINT, la géolocalisation et l’intelligence artificielle appliquées aux énigmes numériques. Le projet est destiné à un usage éducatif et de recherche.

---

**Auteur :** Hackerstchad
**Version :** V2
**Date :** 2026-2027

---

*Fin du document README.*
