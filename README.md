# SICADA3301 V2

**Auteur:** hackerstchad  
**Version:** V2  
**Date:** 2026-2027

---

## Présentation

SICADA3301 est un framework d'investigation numérique, de stéganographie, de cryptanalyse, d'analyse linguistique/symbolique, d'OSINT et de géolocalisation conçu pour les challenges CTF, les ARG et les énigmes complexes.

---

## Installation

```bash
pip install -r requirements.txt
python sicada3301.py --help
```

---

## Utilisation

```bash
python sicada3301.py interactive
python sicada3301.py stego --action extract-lsb -i image.png
python sicada3301.py crypto --action caesar-brute --data "khoor"
python sicada3301.py ling --action runes --text "ᚠᚢᚦ"
python sicada3301.py net --action tor-info
python sicada3301.py geo --action decode --coords "40.7128,-74.0060"
python sicada3301.py ai --action hypotheses --text "01001000"
python sicada3301.py inv --action binary -f fichier.bin
```

---

## Modules

1. **Stéganographie** — LSB image/audio, EOI JPEG, EXIF, DCT, PNG chunks, OutGuess, Steghide, Binwalk, Sonic Visualiser.
2. **Cryptographie** — AES, RSA, XOR, OTP, fréquentielle, Caesar, Vigenère, substitution, symboles anciens, info post-quantique.
3. **Linguistique** — Runes, Liber Primus, OCR, langue, références, acrostiches, grammaire, comparaison de symboles.
4. **Réseau** — Tor, onion, IRC, PGP, Bitcoin, OSINT, logs, anonymisation.
5. **Géolocalisation** — Coordonnées, distance, QR codes, affiches, indices historiques.
6. **IA / Analyse automatisée** — OCR, classification, motifs, statistiques, anomalies, hypothèses cryptographiques.
7. **Investigation** — Analyse binaire, reverse image, métadonnées, corrélations, extraction de strings, rapport.

---

## Code source

Le script principal est [`sicada3301.py`](sicada3301.py).
