#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                           SICADA3301 - FRAMEWORK V2                          ║
║                                                                              ║
║  Auteur    : hackerstchad                                                    ║
║  Version   : V2                                                              ║
║  Date      : 2026-2027                                                       ║
║                                                                              ║
║  Suite avancée d'investigation numérique, de stéganographie, de              ║
║  cryptanalyse, d'OSINT et d'analyse multimédia pour la résolution            ║
║  d'énigmes et de challenges type CTF.                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import io
import re
import json
import math
import time
import base64
import hashlib
import binascii
import argparse
import tempfile
import zipfile
import subprocess
import string
import itertools
import collections
import statistics
import datetime
import warnings
import urllib.parse
import urllib.request
from pathlib import Path
from fractions import Fraction
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

# ──────────────────────────────────────────────────────────────────────────────
# Tentatives d'import des bibliothèques tierces
# ──────────────────────────────────────────────────────────────────────────────

OPTIONAL_DEPS = {}

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich.prompt import Prompt
    OPTIONAL_DEPS['rich'] = True
except ImportError:
    OPTIONAL_DEPS['rich'] = False

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    OPTIONAL_DEPS['colorama'] = True
except ImportError:
    OPTIONAL_DEPS['colorama'] = False
    class _Fore:
        def __getattr__(self, name): return ''
    Fore = Back = Style = _Fore()

try:
    from PIL import Image, ExifTags, ImageOps, ImageFilter, ImageDraw
    OPTIONAL_DEPS['PIL'] = True
except ImportError:
    OPTIONAL_DEPS['PIL'] = False

try:
    import numpy as np
    OPTIONAL_DEPS['numpy'] = True
except ImportError:
    OPTIONAL_DEPS['numpy'] = False
    np = None

try:
    from scipy.fftpack import dct, idct
    OPTIONAL_DEPS['scipy'] = True
except ImportError:
    OPTIONAL_DEPS['scipy'] = False
    dct = idct = None

try:
    import cv2
    OPTIONAL_DEPS['cv2'] = True
except ImportError:
    OPTIONAL_DEPS['cv2'] = False
    cv2 = None

try:
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.backends import default_backend
    OPTIONAL_DEPS['cryptography'] = True
except ImportError:
    OPTIONAL_DEPS['cryptography'] = False

try:
    from Crypto.Cipher import AES as PyCryptoAES
    from Crypto.Util.Padding import pad, unpad
    OPTIONAL_DEPS['pycryptodome'] = True
except ImportError:
    OPTIONAL_DEPS['pycryptodome'] = False

try:
    import librosa
    import soundfile as sf
    OPTIONAL_DEPS['audio'] = True
except ImportError:
    OPTIONAL_DEPS['audio'] = False
    librosa = sf = None

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    OPTIONAL_DEPS['matplotlib'] = True
except ImportError:
    OPTIONAL_DEPS['matplotlib'] = False
    plt = None

try:
    import pytesseract
    OPTIONAL_DEPS['tesseract'] = True
except ImportError:
    OPTIONAL_DEPS['tesseract'] = False

try:
    from langdetect import detect, detect_langs
    OPTIONAL_DEPS['langdetect'] = True
except ImportError:
    OPTIONAL_DEPS['langdetect'] = False

try:
    import requests
    OPTIONAL_DEPS['requests'] = True
except ImportError:
    OPTIONAL_DEPS['requests'] = False
    requests = None

try:
    from bs4 import BeautifulSoup
    OPTIONAL_DEPS['bs4'] = True
except ImportError:
    OPTIONAL_DEPS['bs4'] = False

try:
    import qrcode
    OPTIONAL_DEPS['qrcode'] = True
except ImportError:
    OPTIONAL_DEPS['qrcode'] = False

try:
    from pyzbar.pyzbar import decode as zbar_decode
    OPTIONAL_DEPS['pyzbar'] = True
except ImportError:
    OPTIONAL_DEPS['pyzbar'] = False

try:
    from geopy.distance import geodesic
    OPTIONAL_DEPS['geopy'] = True
except ImportError:
    OPTIONAL_DEPS['geopy'] = False
    geodesic = None

try:
    import magic
    OPTIONAL_DEPS['magic'] = True
except ImportError:
    OPTIONAL_DEPS['magic'] = False
    magic = None

warnings.filterwarnings('ignore')

# ──────────────────────────────────────────────────────────────────────────────
# Constantes globales
# ──────────────────────────────────────────────────────────────────────────────

APP_NAME = "SICADA3301"
APP_VERSION = "V2"
APP_AUTHOR = "hackerstchad"
APP_DATE = "2026-2027"

RUNCES_ALPHABET = {
    'ᚠ': 'f', 'ᚢ': 'u', 'ᚦ': 'th', 'ᚩ': 'o', 'ᚱ': 'r',
    'ᚳ': 'c', 'ᚷ': 'g', 'ᚹ': 'w', 'ᚻ': 'h', 'ᚾ': 'n',
    'ᛁ': 'i', 'ᛂ': 'j', 'ᛇ': 'eo', 'ᛈ': 'p', 'ᛉ': 'x',
    'ᛋ': 's', 'ᛏ': 't', 'ᛒ': 'b', 'ᛖ': 'e', 'ᛗ': 'm',
    'ᛚ': 'l', 'ᛝ': 'ng', 'ᛟ': 'oe', 'ᛞ': 'd', 'ᚪ': 'a',
    'ᚫ': 'ae', 'ᚣ': 'y', 'ᛡ': 'io', 'ᛣ': 'k'
}

LIBER_PRIMUS_COMMON = [
    "Liber Primus", "primus", "way", "path", "parable",
    "wisdom", "knowledge", "truth", "seek", "deep"
]

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}

BRAILLE_DICT = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': ' '
}

BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

COMMON_WORDS = set([
    "the", "be", "to", "of", "and", "a", "in", "that", "have",
    "i", "it", "for", "not", "on", "with", "he", "as", "you",
    "do", "at", "this", "but", "his", "by", "from", "they", "we",
    "say", "her", "she", "or", "an", "will", "my", "one", "all",
    "would", "there", "their", "what", "so", "up", "out", "if",
    "about", "who", "get", "which", "go", "me", "when", "make",
    "can", "like", "time", "no", "just", "him", "know", "take",
    "people", "into", "year", "your", "good", "some", "could",
    "them", "see", "other", "than", "then", "now", "look", "only",
    "come", "its", "over", "think", "also", "back", "after",
    "use", "two", "how", "our", "work", "first", "well", "way",
    "even", "new", "want", "because", "any", "these", "give",
    "day", "most", "us", "le", "de", "et", "à", "un", "il",
    "être", "avoir", "ne", "je", "son", "que", "se", "qui",
    "ce", "dans", "en", "du", "elle", "au", "de", "ce", "pour"
])

# ──────────────────────────────────────────────────────────────────────────────
# Helpers d'affichage
# ──────────────────────────────────────────────────────────────────────────────

console = Console() if OPTIONAL_DEPS.get('rich') else None


def print_banner():
    banner = f"""
{Fore.RED}   ███████╗██╗ ██████╗ █████╗ ██████╗  █████╗ ██████╗ ███████╗  ██╗  ██╗
   ██╔════╝██║██╔════╝██╔══██╗██╔══██╗██╔══██╗╚════██╗██╔════╝  ██║  ██║
   ███████╗██║██║     ███████║██║  ██║███████║ █████╔╝███████╗  ███████║
   ╚════██║██║██║     ██╔══██║██║  ██║██╔══██║██╔═══╝ ╚════██║  ╚════██║
   ███████║██║╚██████╗██║  ██║██████╔╝██║  ██║███████╗███████║       ██║
   ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝       ╚═╝{Style.RESET_ALL}
{Fore.GREEN}              Framework d'investigation numérique avancée{Style.RESET_ALL}
{Fore.YELLOW}                    Auteur: {APP_AUTHOR} | {APP_VERSION} | {APP_DATE}{Style.RESET_ALL}
"""
    print(banner)


def progress_bar(task_name, steps=20, delay=0.05):
    if OPTIONAL_DEPS.get('rich'):
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=40),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as progress:
            task = progress.add_task(f"[cyan]{task_name}...", total=steps)
            for _ in range(steps):
                time.sleep(delay)
                progress.advance(task)
    else:
        for i in range(steps + 1):
            bar = f"{Fore.GREEN}{'█' * i}{Fore.RED}{'-' * (steps - i)}{Style.RESET_ALL}"
            print(f"\r{Fore.CYAN}{task_name}: [{bar}] {i * 100 // steps}%", end='', flush=True)
            time.sleep(delay)
        print()


def success(msg):
    print(f"{Fore.GREEN}[✓] {msg}{Style.RESET_ALL}")


def info(msg):
    print(f"{Fore.CYAN}[i] {msg}{Style.RESET_ALL}")


def warning(msg):
    print(f"{Fore.YELLOW}[!] {msg}{Style.RESET_ALL}")


def error(msg):
    print(f"{Fore.RED}[✗] {msg}{Style.RESET_ALL}")


def section(title):
    if OPTIONAL_DEPS.get('rich') and console:
        console.print(Panel(Text(title, style="bold magenta"), border_style="red"))
    else:
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f" {title}")
        print(f"{'='*60}{Style.RESET_ALL}")


# ──────────────────────────────────────────────────────────────────────────────
# Utilitaires généraux
# ──────────────────────────────────────────────────────────────────────────────


def is_text(data):
    try:
        data.decode('utf-8')
        return True
    except Exception:
        return False


def hex_dump(data, width=16):
    if isinstance(data, str):
        data = data.encode('utf-8')
    lines = []
    for i in range(0, len(data), width):
        chunk = data[i:i+width]
        hex_part = ' '.join(f"{b:02x}" for b in chunk)
        ascii_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        lines.append(f"{i:08x}  {hex_part:<{width*3}} |{ascii_part}|")
    return '\n'.join(lines)


def entropy(data):
    if not data:
        return 0.0
    if isinstance(data, str):
        data = data.encode('utf-8')
    counts = Counter(data)
    length = len(data)
    return -sum((c / length) * math.log2(c / length) for c in counts.values())


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def repeating_key_xor(data, key):
    if isinstance(data, str):
        data = data.encode('utf-8')
    if isinstance(key, str):
        key = key.encode('utf-8')
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))


def hamming_distance(a, b):
    return sum(bin(x ^ y).count('1') for x, y in zip(a, b))


def read_file_bytes(path):
    try:
        with open(path, 'rb') as f:
            return f.read()
    except Exception as e:
        error(f"Impossible de lire {path}: {e}")
        return None


def save_file_bytes(path, data):
    try:
        with open(path, 'wb') as f:
            f.write(data)
        success(f"Fichier sauvegardé: {path}")
        return True
    except Exception as e:
        error(f"Impossible d'écrire {path}: {e}")
        return False


def detect_file_type(path):
    if magic:
        try:
            return magic.from_file(path)
        except Exception:
            pass
    ext = Path(path).suffix.lower()
    return {
        '.png': 'PNG image', '.jpg': 'JPEG image', '.jpeg': 'JPEG image',
        '.gif': 'GIF image', '.bmp': 'BMP image', '.wav': 'WAVE audio',
        '.mp3': 'MP3 audio', '.txt': 'Text file', '.pdf': 'PDF document',
        '.zip': 'ZIP archive',
    }.get(ext, 'Unknown')


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE 1 — STÉGANOGRAPHIE ET DISSIMULATION DE DONNÉES
# ═══════════════════════════════════════════════════════════════════════════════


class SteganographyModule:
    NAME = "Stéganographie & dissimulation"

    def __init__(self):
        self.last_result = None

    def embed_lsb(self, image_path, message, output_path):
        if not OPTIONAL_DEPS.get('PIL'):
            error("Pillow requis pour LSB.")
            return False
        try:
            img = Image.open(image_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            pixels = list(img.getdata())
            binary = ''.join(format(b, '08b') for b in message.encode('utf-8'))
            binary += '00000000' * 4
            if len(binary) > len(pixels) * 3:
                error("Message trop long pour cette image.")
                return False
            new_pixels = []
            idx = 0
            for pixel in pixels:
                r, g, b = pixel
                if idx < len(binary):
                    r = (r & 0xFE) | int(binary[idx]); idx += 1
                if idx < len(binary):
                    g = (g & 0xFE) | int(binary[idx]); idx += 1
                if idx < len(binary):
                    b = (b & 0xFE) | int(binary[idx]); idx += 1
                new_pixels.append((r, g, b))
            img.putdata(new_pixels)
            img.save(output_path)
            success(f"Message dissimulé dans {output_path}")
            return True
        except Exception as e:
            error(f"LSB embed échoué: {e}")
            return False

    def extract_lsb(self, image_path):
        if not OPTIONAL_DEPS.get('PIL'):
            error("Pillow requis pour LSB.")
            return None
        try:
            img = Image.open(image_path)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            binary = ''
            for r, g, b in img.getdata():
                binary += str(r & 1) + str(g & 1) + str(b & 1)
            chars = []
            for i in range(0, len(binary), 8):
                byte = binary[i:i+8]
                val = int(byte, 2)
                if val == 0:
                    break
                chars.append(chr(val))
            result = ''.join(chars)
            self.last_result = result
            success("Extraction LSB terminée")
            return result
        except Exception as e:
            error(f"LSB extract échoué: {e}")
            return None

    def extract_jpeg_eoi(self, jpeg_path):
        data = read_file_bytes(jpeg_path)
        if not data:
            return None
        eoi = data.find(b'\xff\xd9')
        if eoi == -1:
            warning("Marqueur EOI JPEG non trouvé.")
            return None
        trailer = data[eoi+2:]
        if trailer:
            success(f"Données après EOI détectées: {len(trailer)} octets")
            return trailer
        info("Aucune donnée après EOI.")
        return None

    def exif_analysis(self, image_path):
        if not OPTIONAL_DEPS.get('PIL'):
            error("Pillow requis pour EXIF.")
            return {}
        try:
            img = Image.open(image_path)
            exif = img._getexif() or {}
            decoded = {}
            for tag, value in exif.items():
                tag_name = ExifTags.TAGS.get(tag, tag)
                decoded[tag_name] = value
            success(f"{len(decoded)} tags EXIF extraits")
            return decoded
        except Exception as e:
            error(f"EXIF échoué: {e}")
            return {}

    def audio_spectrogram(self, audio_path, output_path="spectrogram.png"):
        if not all([OPTIONAL_DEPS.get('audio'), OPTIONAL_DEPS.get('numpy'), OPTIONAL_DEPS.get('matplotlib')]):
            error("librosa/soundfile/matplotlib requis pour spectrogramme.")
            return False
        try:
            y, sr = librosa.load(audio_path, sr=None)
            plt.figure(figsize=(12, 6))
            D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
            librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='hz')
            plt.colorbar(format='%+2.0f dB')
            plt.title('Spectrogramme audio')
            plt.tight_layout()
            plt.savefig(output_path, dpi=150)
            plt.close()
            success(f"Spectrogramme sauvegardé: {output_path}")
            return True
        except Exception as e:
            error(f"Spectrogramme échoué: {e}")
            return False

    def embed_wav_lsb(self, wav_path, message, output_path):
        if not OPTIONAL_DEPS.get('audio'):
            error("soundfile requis pour WAV LSB.")
            return False
        try:
            data, sr = sf.read(wav_path)
            if len(data.shape) > 1:
                data = data[:, 0]
            binary = ''.join(format(b, '08b') for b in message.encode('utf-8')) + '00000000' * 8
            if len(binary) > len(data):
                error("Message trop long pour ce WAV.")
                return False
            samples = data.astype(np.float64).copy()
            for i, bit in enumerate(binary):
                val = int(samples[i])
                val = (val & 0xFFFE) | int(bit)
                samples[i] = val
            sf.write(output_path, samples, sr, subtype='PCM_16')
            success(f"Message dissimulé dans {output_path}")
            return True
        except Exception as e:
            error(f"WAV LSB échoué: {e}")
            return False

    def extract_wav_lsb(self, wav_path):
        if not OPTIONAL_DEPS.get('audio'):
            error("soundfile requis pour WAV LSB.")
            return None
        try:
            data, sr = sf.read(wav_path)
            if len(data.shape) > 1:
                data = data[:, 0]
            binary = ''
            for i in range(min(len(data), 200000)):
                val = int(data[i])
                binary += str(val & 1)
            chars = []
            for i in range(0, len(binary), 8):
                byte = binary[i:i+8]
                val = int(byte, 2)
                if val == 0:
                    break
                chars.append(chr(val))
            result = ''.join(chars)
            self.last_result = result
            success("Extraction WAV LSB terminée")
            return result
        except Exception as e:
            error(f"WAV LSB extract échoué: {e}")
            return None

    def analyze_png_chunks(self, png_path):
        data = read_file_bytes(png_path)
        if not data or not data.startswith(b'\x89PNG'):
            error("Fichier PNG invalide.")
            return []
        chunks = []
        idx = 8
        while idx < len(data):
            length = int.from_bytes(data[idx:idx+4], 'big')
            ctype = data[idx+4:idx+8].decode('latin-1', errors='replace')
            crc = data[idx+8+length:idx+12+length]
            chunks.append({'type': ctype, 'length': length, 'crc': crc.hex(), 'offset': idx})
            idx += 12 + length
        success(f"{len(chunks)} chunks PNG analysés")
        return chunks

    def detect_appended_data(self, file_path):
        data = read_file_bytes(file_path)
        if not data:
            return None
        known_magics = {
            b'PK\x03\x04': 'ZIP',
            b'Rar!': 'RAR',
            b'7z\xbc\xaf\x27\x1c': '7Z',
            b'%PDF': 'PDF',
            b'\x89PNG': 'PNG',
            b'\xff\xd8\xff': 'JPEG',
            b'GIF8': 'GIF',
            b'\x1f\x8b': 'GZIP',
            b'BZh': 'BZIP2',
            b'\xfd7zXZ': 'XZ',
        }
        for magic_bytes, ftype in known_magics.items():
            pos = data.rfind(magic_bytes)
            if pos > 0 and pos != data.find(magic_bytes):
                return {'type': ftype, 'offset': pos, 'size': len(data) - pos}
        return None

    def dct_analysis(self, image_path):
        if not all([OPTIONAL_DEPS.get('PIL'), OPTIONAL_DEPS.get('numpy'), OPTIONAL_DEPS.get('scipy')]):
            error("Pillow/numpy/scipy requis pour DCT.")
            return None
        try:
            img = Image.open(image_path).convert('L')
            arr = np.array(img, dtype=np.float32)
            h, w = arr.shape
            results = []
            for y in range(0, h - 8, 8):
                for x in range(0, w - 8, 8):
                    block = arr[y:y+8, x:x+8]
                    dct_block = dct(dct(block.T, norm='ortho').T, norm='ortho')
                    results.append({'x': x, 'y': y, 'max': float(np.max(np.abs(dct_block)))})
            return results
        except Exception as e:
            error(f"DCT analysis échoué: {e}")
            return None

    def outguess_run(self, image_path, password=None, extract=False, payload=None, output=None):
        if extract:
            cmd = ['outguess', '-k', password or '', '-r', image_path, output or 'outguess_output.txt']
        else:
            cmd = ['outguess', '-k', password or '', '-d', payload or '', image_path, output or 'outguess_embedded.jpg']
        return self._run_tool(cmd)

    def steghide_run(self, image_path, password, extract=False, payload=None, output=None):
        if extract:
            cmd = ['steghide', 'extract', '-sf', image_path, '-p', password or '', '-xf', output or 'steghide_output.txt']
        else:
            cmd = ['steghide', 'embed', '-cf', image_path, '-ef', payload or '', '-p', password or '', '-sf', output or 'steghide_embedded.jpg']
        return self._run_tool(cmd)

    def binwalk_scan(self, file_path):
        return self._run_tool(['binwalk', '-e', file_path])

    def sonic_visualiser_export(self, audio_path, output_path="sonic_layers.txt"):
        info("Export pour Sonic Visualiser : ouvrez le fichier audio dans Sonic Visualiser et ajoutez des layers de spectrogramme.")
        with open(output_path, 'w') as f:
            f.write(f"# Sonic Visualiser session suggestion\n# Audio: {audio_path}\n")
        success(f"Suggestion Sonic Visualiser écrite: {output_path}")
        return True

    def _run_tool(self, cmd):
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            print(result.stdout)
            if result.stderr:
                warning(result.stderr)
            return result.returncode == 0
        except FileNotFoundError:
            error(f"Outil externe non trouvé: {cmd[0]}")
            return False
        except Exception as e:
            error(f"Échec exécution {cmd[0]}: {e}")
            return Falseength.hex()
            chunks.append({'type': ctype, 'length': length, 'crc': crc})
            idx += 12 + length
        success(f"{len(chunks)} chunks PNG analysés")
        return chunks

    def detect_appended_data(self, file_path):
        data = read_file_bytes(file_path)
        if not data:
            return None
        signatures = {
            b'PK\x03\x04': 'ZIP',
            b'Rar!': 'RAR',
            b'7z\xbc\xaf\x27\x1c': '7Z',
            b'\x89PNG': 'PNG',
            b'\xff\xd8\xff': 'JPEG',
            b'GIF8': 'GIF',
            b'%PDF': 'PDF',
        }
        for sig, ftype in signatures.items():
            pos = data.rfind(sig)
            if pos > 0:
                return {'type': ftype, 'offset': pos, 'size': len(data) - pos}
        return None

    def dct_analysis(self, image_path):
        if not all([OPTIONAL_DEPS.get('PIL'), OPTIONAL_DEPS.get('numpy'), OPTIONAL_DEPS.get('scipy')]):
            error("Pillow/numpy/scipy requis pour DCT.")
            return None
        try:
            img = Image.open(image_path).convert('L')
            arr = np.array(img, dtype=np.float32)
            blocks = []
            for y in range(0, arr.shape[0] - 8, 8):
                for x in range(0, arr.shape[1] - 8, 8):
                    block = arr[y:y+8, x:x+8]
                    d = dct(dct(block.T, norm='ortho').T, norm='ortho')
                    blocks.append(d)
            success(f"DCT: {len(blocks)} blocs 8x8 analysés")
            return blocks
        except Exception as e:
            error(f"DCT échoué: {e}")
            return None

    def outguess_run(self, image_path, password=None, extract=False, payload=None, output=None):
        if not self._check_tool('outguess'):
            return False
        cmd = ['outguess']
        if extract:
            cmd += ['-k', password or '', '-r', image_path, output or 'outguess_extracted.txt']
        else:
            cmd += ['-k', password or '', '-d', payload or '', image_path, output or 'outguess_out.jpg']
        return self._run_tool(cmd)

    def steghide_run(self, image_path, password=None, extract=False, payload=None, output=None):
        if not self._check_tool('steghide'):
            return False
        cmd = ['steghide']
        if extract:
            cmd += ['extract', '-sf', image_path, '-p', password or '', '-xf', output or 'steghide_extracted.txt']
        else:
            cmd += ['embed', '-cf', image_path, '-ef', payload or '', '-p', password or '', '-sf', output or 'steghide_out.jpg']
        return self._run_tool(cmd)

    def binwalk_scan(self, file_path):
        if not self._check_tool('binwalk'):
            return False
        return self._run_tool(['binwalk', '-e', file_path])

    def sonic_visualiser_export(self, audio_path, output_path="sonic_layers.txt"):
        if not OPTIONAL_DEPS.get('audio'):
            error("librosa requis pour Sonic Visualiser export.")
            return False
        try:
            y, sr = librosa.load(audio_path, sr=None)
            onset_env = librosa.onset.onset_strength(y=y, sr=sr)
            tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
            lines = [
                f"Sonic Visualiser layer export for {audio_path}",
                f"Sample rate: {sr}",
                f"Duration: {len(y)/sr:.2f}s",
                f"Tempo: {tempo}",
                f"Beats count: {len(beats)}",
            ]
            with open(output_path, 'w') as f:
                f.write('\n'.join(lines))
            success(f"Export Sonic Visualiser: {output_path}")
            return True
        except Exception as e:
            error(f"Sonic export échoué: {e}")
            return False

    def _check_tool(self, name):
        try:
            subprocess.run([name, '--version'], capture_output=True, timeout=5)
            return True
        except FileNotFoundError:
            error(f"Outil externe manquant: {name}")
            return False

    def _run_tool(self, cmd):
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            print(result.stdout)
            if result.stderr:
                warning(result.stderr)
            return result.returncode == 0
        except Exception as e:
            error(f"Outil externe échoué: {e}")
            return False


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE 2 — CRYPTOGRAPHIE ET DÉCHIFFREMENT
# ═══════════════════════════════════════════════════════════════════════════════


class CryptoModule:
    NAME = "Cryptographie & déchiffrement"

    def aes_encrypt(self, plaintext, key, mode='CBC'):
        if not OPTIONAL_DEPS.get('pycryptodome'):
            error("pycryptodome requis pour AES.")
            return None
        try:
            key = key.encode('utf-8') if isinstance(key, str) else key
            data = plaintext.encode('utf-8') if isinstance(plaintext, str) else plaintext
            if len(key) not in (16, 24, 32):
                error("Clé AES invalide (16/24/32 octets).")
                return None
            if mode == 'CBC':
                iv = os.urandom(16)
                cipher = PyCryptoAES.new(key, PyCryptoAES.MODE_CBC, iv)
                ct = cipher.encrypt(pad(data, PyCryptoAES.block_size))
                return base64.b64encode(iv + ct).decode()
            elif mode == 'ECB':
                cipher = PyCryptoAES.new(key, PyCryptoAES.MODE_ECB)
                ct = cipher.encrypt(pad(data, PyCryptoAES.block_size))
                return base64.b64encode(ct).decode()
            elif mode == 'CTR':
                nonce = os.urandom(8)
                cipher = PyCryptoAES.new(key, PyCryptoAES.MODE_CTR, nonce=nonce)
                ct = cipher.encrypt(data)
                return base64.b64encode(nonce + ct).decode()
            else:
                error("Mode AES non supporté.")
                return None
        except Exception as e:
            error(f"AES encrypt échoué: {e}")
            return None

    def aes_decrypt(self, ciphertext, key, mode='CBC'):
        if not OPTIONAL_DEPS.get('pycryptodome'):
            error("pycryptodome requis pour AES.")
            return None
        try:
            key = key.encode('utf-8') if isinstance(key, str) else key
            data = base64.b64decode(ciphertext)
            if mode == 'CBC':
                iv, ct = data[:16], data[16:]
                cipher = PyCryptoAES.new(key, PyCryptoAES.MODE_CBC, iv)
                return unpad(cipher.decrypt(ct), PyCryptoAES.block_size).decode('utf-8', errors='replace')
            elif mode == 'ECB':
                cipher = PyCryptoAES.new(key, PyCryptoAES.MODE_ECB)
                return unpad(cipher.decrypt(data), PyCryptoAES.block_size).decode('utf-8', errors='replace')
            elif mode == 'CTR':
                nonce, ct = data[:8], data[8:]
                cipher = PyCryptoAES.new(key, PyCryptoAES.MODE_CTR, nonce=nonce)
                return cipher.decrypt(ct).decode('utf-8', errors='replace')
            else:
                error("Mode AES non supporté.")
                return None
        except Exception as e:
            error(f"AES decrypt échoué: {e}")
            return None

    def rsa_generate_keys(self, key_size=2048):
        if not OPTIONAL_DEPS.get('cryptography'):
            error("cryptography requis pour RSA.")
            return None, None
        try:
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size, backend=default_backend())
            private_pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ).decode()
            public_pem = private_key.public_key().public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode()
            success(f"Paire RSA {key_size} bits générée")
            return private_pem, public_pem
        except Exception as e:
            error(f"RSA gen échoué: {e}")
            return None, None

    def rsa_encrypt(self, plaintext, public_key_pem):
        if not OPTIONAL_DEPS.get('cryptography'):
            error("cryptography requis pour RSA.")
            return None
        try:
            key = serialization.load_pem_public_key(public_key_pem.encode(), backend=default_backend())
            ct = key.encrypt(
                plaintext.encode('utf-8'),
                padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
            )
            return base64.b64encode(ct).decode()
        except Exception as e:
            error(f"RSA encrypt échoué: {e}")
            return None

    def rsa_decrypt(self, ciphertext, private_key_pem):
        if not OPTIONAL_DEPS.get('cryptography'):
            error("cryptography requis pour RSA.")
            return None
        try:
            key = serialization.load_pem_private_key(private_key_pem.encode(), password=None, backend=default_backend())
            pt = key.decrypt(
                base64.b64decode(ciphertext),
                padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
            )
            return pt.decode('utf-8')
        except Exception as e:
            error(f"RSA decrypt échoué: {e}")
            return None

    def xor_encrypt(self, plaintext, key):
        result = repeating_key_xor(plaintext, key)
        return result.hex()

    def xor_decrypt(self, hexdata, key):
        data = bytes.fromhex(hexdata)
        result = repeating_key_xor(data, key)
        return result.decode('utf-8', errors='replace')

    def otp_generate(self, length):
        return os.urandom(length)

    def otp_encrypt(self, plaintext, key):
        data = plaintext.encode('utf-8') if isinstance(plaintext, str) else plaintext
        if len(data) != len(key):
            error("OTP: clé et message doivent avoir la même longueur.")
            return None
        return xor_bytes(data, key).hex()

    def otp_decrypt(self, hexdata, key):
        data = bytes.fromhex(hexdata)
        if len(data) != len(key):
            error("OTP: clé et message doivent avoir la même longueur.")
            return None
        return xor_bytes(data, key).decode('utf-8', errors='replace')

    def frequency_analysis(self, text):
        letters = [c.lower() for c in text if c.isalpha()]
        total = len(letters)
        if not total:
            return {}
        return {letter: count / total for letter, count in Counter(letters).most_common()}

    def caesar_decrypt(self, text, shift):
        result = []
        for c in text:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result.append(chr((ord(c) - base - shift) % 26 + base))
            else:
                result.append(c)
        return ''.join(result)

    def caesar_bruteforce(self, text):
        results = []
        for shift in range(26):
            dec = self.caesar_decrypt(text, shift)
            score = self._score_english(dec)
            results.append((shift, dec, score))
        return sorted(results, key=lambda x: -x[2])

    def vigenere_decrypt(self, text, key):
        key = key.lower()
        result = []
        idx = 0
        for c in text:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                shift = ord(key[idx % len(key)]) - ord('a')
                result.append(chr((ord(c) - base - shift) % 26 + base))
                idx += 1
            else:
                result.append(c)
        return ''.join(result)

    def vigenere_bruteforce(self, text, max_key_len=12):
        results = []
        text_clean = ''.join(c for c in text if c.isalpha())
        for kl in range(2, max_key_len + 1):
            groups = ['' for _ in range(kl)]
            for i, c in enumerate(text_clean.lower()):
                groups[i % kl] += c
            key = ''
            for g in groups:
                best_shift = max(range(26), key=lambda s: self._score_english(self.caesar_decrypt(g, s)))
                key += chr(ord('a') + best_shift)
            dec = self.vigenere_decrypt(text, key)
            score = self._score_english(dec)
            results.append((kl, key, dec, score))
        return sorted(results, key=lambda x: -x[3])

    def substitution_solve(self, text, mapping=None):
        if mapping is None:
            # Heuristique basique: remplacer les lettres fréquentes par e, t, a, o, i, n...
            freq = Counter(c.lower() for c in text if c.isalpha()).most_common(26)
            english_order = 'etaoinsrhdlcumwfgypbvkjxqz'
            mapping = {f[0]: english_order[i] for i, f in enumerate(freq) if i < len(english_order)}
        result = []
        for c in text:
            if c.lower() in mapping:
                new = mapping[c.lower()]
                if c.isupper():
                    new = new.upper()
                result.append(new)
            else:
                result.append(c)
        return ''.join(result)

    def detect_classical_cipher(self, text):
        ioc = self._index_of_coincidence(text)
        if ioc > 0.065:
            return {'cipher': 'Substitution monoalphabétique', 'ioc': ioc}
        elif ioc > 0.045:
            return {'cipher': 'Vigenère / polyalphabétique', 'ioc': ioc}
        else:
            return {'cipher': 'Transposition ou autre', 'ioc': ioc}

    def multi_layer_decrypt(self, data, layers):
        result = data
        for layer in layers:
            layer_type = layer.get('type')
            if layer_type == 'base64':
                result = base64.b64decode(result).decode('utf-8', errors='replace')
            elif layer_type == 'hex':
                result = bytes.fromhex(result).decode('utf-8', errors='replace')
            elif layer_type == 'rot13':
                result = result.translate(str.maketrans(
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'))
            elif layer_type == 'caesar':
                result = self.caesar_decrypt(result, layer.get('shift', 3))
            elif layer_type == 'xor':
                result = self.xor_decrypt(result if isinstance(result, str) else result.hex(), layer['key'])
            elif layer_type == 'reverse':
                result = result[::-1]
            elif layer_type == 'aes':
                result = self.aes_decrypt(result, layer['key'], layer.get('mode', 'CBC'))
            else:
                warning(f"Couche inconnue: {layer_type}")
        return result

    def ancient_symbols_decode(self, text):
        result = []
        for c in text:
            if c in RUNCES_ALPHABET:
                result.append(RUNCES_ALPHABET[c])
            else:
                result.append(c)
        return ''.join(result)

    def post_quantum_info(self):
        info("Cryptographie post-quantique (PQC)")
        print("""
Algorithmes NIST standardisés (2024):
- ML-KEM (Key Encapsulation Mechanism, anciennement Kyber)
- ML-DSA (Digital Signature Algorithm, anciennement Dilithium)
- SLH-DSA (Sphincs+)
- FN-DSA (FALCON)

Considérations:
- RSA/ECC classiques sont vulnérables à l'algorithme de Shor
- Les algorithmes à base de réseaux (lattices) offrent résistance post-quantique
- Migration progressive vers des bibliothèques comme python-pqclean ou oqs-python
""")

    def _score_english(self, text):
        words = re.findall(r'[a-zA-Z]+', text.lower())
        score = sum(1 for w in words if w in COMMON_WORDS)
        return score / max(len(words), 1)

    def _index_of_coincidence(self, text):
        letters = [c.lower() for c in text if c.isalpha()]
        total = len(letters)
        if total < 2:
            return 0.0
        counts = Counter(letters)
        return sum(n * (n - 1) for n in counts.values()) / (total * (total - 1))


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE 3 — ANALYSE LINGUISTIQUE ET SYMBOLIQUE
# ═══════════════════════════════════════════════════════════════════════════════


class LinguisticModule:
    NAME = "Analyse linguistique & symbolique"

    def runes_to_latin(self, text):
        return CryptoModule().ancient_symbols_decode(text)

    def liber_primus_score(self, text):
        text_lower = text.lower()
        found = sum(1 for word in LIBER_PRIMUS_COMMON if word in text_lower)
        ratio = found / len(LIBER_PRIMUS_COMMON)
        return found, ratio

    def ocr_image(self, image_path, lang='eng'):
        if not OPTIONAL_DEPS.get('tesseract') or not OPTIONAL_DEPS.get('PIL'):
            error("pytesseract + Pillow requis pour OCR.")
            return None
        try:
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img, lang=lang)
            success("OCR terminé")
            return text
        except Exception as e:
            error(f"OCR échoué: {e}")
            return None

    def detect_language(self, text):
        if not OPTIONAL_DEPS.get('langdetect'):
            info("langdetect manquant — retour heuristique.")
            return "unknown"
        try:
            return detect(text)
        except Exception:
            return "unknown"

    def find_literary_references(self, text):
        refs = {
            'Liber Primus': 'Liber Primus',
            'Dante': 'Divine Comédie',
            'Bible': 'Bible',
            'Plato': 'Platon',
            'Nietzsche': 'Nietzsche',
            'Goethe': 'Goethe',
            'Tao': 'Tao Te Ching',
        }
        found = []
        for key, value in refs.items():
            if key.lower() in text.lower():
                found.append(value)
        return found if found else ["Aucune référence littéraire détectée"]

    def detect_acrostic(self, text):
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        if not lines:
            return ""
        return ''.join(line[0] for line in lines)

    def grammar_structure(self, text):
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        words = re.findall(r'\b\w+\b', text)
        return {
            'sentences': len(sentences),
            'words': len(words),
            'avg_words_per_sentence': len(words) / max(len(sentences), 1),
            'punctuation': sum(1 for c in text if c in string.punctuation)
        }

    def symbol_compare(self, text1, text2):
        set1 = set(text1)
        set2 = set(text2)
        return {
            'unique_1': len(set1),
            'unique_2': len(set2),
            'intersection': len(set1 & set2),
            'union': len(set1 | set2),
            'jaccard': len(set1 & set2) / len(set1 | set2) if (set1 | set2) else 0
        }

    def detect_repeated_patterns(self, text, min_len=3):
        results = []
        for length in range(min_len, min(20, len(text) // 2 + 1)):
            seen = {}
            for i in range(len(text) - length + 1):
                sub = text[i:i+length]
                if sub in seen:
                    seen[sub] += 1
                else:
                    seen[sub] = 1
            for sub, count in seen.items():
                if count > 2:
                    results.append({'pattern': sub, 'length': length, 'count': count})
        return sorted(results, key=lambda x: -x['count'])[:20]

    def ai_generated_score(self, text):
        # Heuristique simple: textes IA ont souvent une entropie et distribution régulières
        letters = [c.lower() for c in text if c.isalpha()]
        if not letters:
            return 0.0
        freq = Counter(letters)
        total = len(letters)
        distribution_uniformity = statistics.pstdev(freq.values()) / max(total / 26, 1)
        sentence_lengths = [len(s.split()) for s in re.split(r'[.!?]+', text) if s.strip()]
        length_variance = statistics.pstdev(sentence_lengths) if len(sentence_lengths) > 1 else 0
        score = min(1.0, (distribution_uniformity * 10 + length_variance * 0.05))
        return round(score, 3)


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE 4 — RÉSEAUX ET ANONYMAT NUMÉRIQUE
# ═══════════════════════════════════════════════════════════════════════════════


class NetworkModule:
    NAME = "Réseaux & anonymat numérique"

    def tor_info(self):
        return {
            'description': 'Tor est un réseau de routage en oignon pour anonymiser le trafic',
            'onion_v2': '16 caractères (obsolète)',
            'onion_v3': '56 caractères, plus sécurisé',
            'relay_types': ['Entry guard', 'Middle relay', 'Exit relay', 'Bridge'],
            'security_note': 'Vérifier toujours le certificat .onion et utiliser HTTPS'
        }

    def check_onion(self, onion_url, timeout=15):
        if not requests:
            error("requests requis pour vérifier un service onion.")
            return None
        if not re.match(r'^[a-z2-7]{16,56}\.onion$', onion_url):
            warning("Format d'URL onion suspect.")
            return {'valid_format': False}
        proxy = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        try:
            response = requests.get(f"http://{onion_url}", proxies=proxy, timeout=timeout)
            return {'status': response.status_code, 'headers': dict(response.headers), 'length': len(response.text)}
        except Exception as e:
            error(f"Connexion onion échouée: {e}")
            return {'error': str(e)}

    def irc_connect(self, server, port=6667, channel=None, nick='sicada3301'):
        try:
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((server, port))
            s.send(f"NICK {nick}\r\n".encode())
            s.send(f"USER {nick} 0 * :Sicada3301\r\n".encode())
            if channel:
                s.send(f"JOIN {channel}\r\n".encode())
            time.sleep(2)
            response = s.recv(4096).decode('utf-8', errors='replace')
            s.close()
            return response
        except Exception as e:
            error(f"IRC échoué: {e}")
            return None

    def pgp_verify(self, public_key_path, signature_path, message_path):
        try:
            import gnupg
            gpg = gnupg.GPG()
            with open(public_key_path) as f:
                gpg.import_keys(f.read())
            with open(message_path, 'rb') as f:
                verified = gpg.verify_file(f, signature_path)
            return {'valid': verified.valid, 'trust_level': verified.trust_level, 'keyid': verified.key_id}
        except Exception as e:
            error(f"PGP verify échoué: {e}")
            return None

    def bitcoin_tx_info(self, txid):
        if not requests:
            error("requests requis pour Bitcoin.")
            return None
        try:
            url = f"https://blockchain.info/rawtx/{txid}"
            response = requests.get(url, timeout=15)
            return response.json()
        except Exception as e:
            error(f"Bitcoin TX échoué: {e}")
            return None

    def osint_search_username(self, username):
        platforms = [
            f"https://github.com/{username}",
            f"https://twitter.com/{username}",
            f"https://www.reddit.com/user/{username}",
            f"https://www.instagram.com/{username}/",
        ]
        results = []
        for url in platforms:
            results.append({'platform': url, 'exists': 'manual_check_required'})
        return results

    def analyze_connection_logs(self, log_text):
        ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
        ts_pattern = re.compile(r'\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}')
        ips = ip_pattern.findall(log_text)
        timestamps = ts_pattern.findall(log_text)
        return {
            'unique_ips': sorted(set(ips)),
            'ip_counts': Counter(ips),
            'timestamps': timestamps[:20]
        }

    def anonymization_summary(self):
        return {
            'vpn': 'Chiffre le trafic vers un serveur tiers',
            'tor': 'Routage en oignon à 3 sauts',
            'proxy': 'Intermédiaire simple, souvent non chiffré',
            'i2p': 'Réseau anonymisant pair-à-pair',
            'mixnet': 'Mélange de paquets pour résister à l’analyse de trafic'
        }


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE 5 — GÉOLOCALISATION ET INVESTIGATION PHYSIQUE
# ═══════════════════════════════════════════════════════════════════════════════


class GeoModule:
    NAME = "Géolocalisation & investigation physique"

    def decode_coordinates(self, coord_string):
        m = re.match(r'([-+]?\d+\.?\d*)\s*,\s*([-+]?\d+\.?\d*)', coord_string)
        if m:
            return float(m.group(1)), float(m.group(2))
        dms_pattern = re.compile(r'(\d+)°\s*(\d+)\'\s*([\d.]+)"?\s*([NS])\s*(\d+)°\s*(\d+)\'\s*([\d.]+)"?\s*([EW])')
        match = dms_pattern.search(coord_string)
        if match:
            lat = int(match.group(1)) + int(match.group(2))/60 + float(match.group(3))/3600
            if match.group(4) == 'S':
                lat = -lat
            lon = int(match.group(5)) + int(match.group(6))/60 + float(match.group(7))/3600
            if match.group(8) == 'W':
                lon = -lon
            return lat, lon
        return None

    def distance_between(self, coord1, coord2):
        if not geodesic:
            error("geopy requis.")
            return None
        return geodesic(coord1, coord2).kilometers

    def recognize_location(self, image_path):
        if not OPTIONAL_DEPS.get('PIL'):
            error("Pillow requis.")
            return None
        info("Reconnaissance de lieu basée sur image — effectuer une recherche inversée manuellement.")
        return "Utilisez Google Images, Yandex ou TinEye pour identifier le lieu."

    def qr_decode(self, image_path):
        if not OPTIONAL_DEPS.get('pyzbar') or not OPTIONAL_DEPS.get('PIL'):
            error("pyzbar + Pillow requis.")
            return None
        try:
            img = Image.open(image_path)
            results = zbar_decode(img)
            return [r.data.decode('utf-8') for r in results]
        except Exception as e:
            error(f"QR decode échoué: {e}")
            return None

    def qr_generate(self, data, output_path="qrcode.png"):
        if not OPTIONAL_DEPS.get('qrcode'):
            error("qrcode requis.")
            return False
        try:
            img = qrcode.make(data)
            img.save(output_path)
            success(f"QR code généré: {output_path}")
            return True
        except Exception as e:
            error(f"QR generate échoué: {e}")
            return False

    def physical_poster_search(self, location):
        return [
            f"Rechercher sur Reddit r/{location.replace(' ', '')}",
            "Analyser les archives 4chan /x/ /pol/ /b/",
            "Vérifier les hashtags Twitter/X locaux",
            "Consulter les forums ARG et Unfiction"
        ]

    def historical_geo_hints(self, place):
        return {
            'place': place,
            'sources': [
                'Wikipedia historique',
                'Archives nationales',
                'Google Earth historical imagery',
                'OpenStreetMap Nominatim'
            ]
        }


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE 6 — INTELLIGENCE ARTIFICIELLE ET ANALYSE AUTOMATISÉE
# ═══════════════════════════════════════════════════════════════════════════════


class AIModule:
    NAME = "Intelligence artificielle & analyse automatisée"

    def ocr(self, image_path):
        return LinguisticModule().ocr_image(image_path)

    def classify_symbols(self, text):
        categories = {
            'runes': sum(1 for c in text if c in RUNCES_ALPHABET),
            'greek': sum(1 for c in text if '\u0370' <= c <= '\u03ff'),
            'latin': sum(1 for c in text if c.isascii() and c.isalpha()),
            'digits': sum(1 for c in text if c.isdigit()),
            'other': sum(1 for c in text if not (c.isalnum() or c.isspace()))
        }
        total = sum(categories.values())
        if total:
            categories = {k: v/total for k, v in categories.items()}
        return categories

    def detect_repeated_patterns(self, data, min_len=4):
        if isinstance(data, bytes):
            data = data.hex()
        return LinguisticModule().detect_repeated_patterns(data, min_len)

    def text_statistics(self, text):
        letters = [c for c in text if c.isalpha()]
        digits = [c for c in text if c.isdigit()]
        spaces = [c for c in text if c.isspace()]
        others = [c for c in text if not (c.isalnum() or c.isspace())]
        total = len(text)
        return {
            'length': total,
            'letters': len(letters),
            'digits': len(digits),
            'spaces': len(spaces),
            'others': len(others),
            'entropy': entropy(text),
            'frequency': Counter(letters).most_common(10)
        }

    def anomaly_detection_file(self, file_path):
        data = read_file_bytes(file_path)
        if not data:
            return None
        e = entropy(data)
        anomalies = []
        if e > 7.9:
            anomalies.append("Entropie très élevée — probablement chiffré ou compressé")
        elif e < 2.0:
            anomalies.append("Entropie très faible — texte clair ou données répétitives")
        appended = SteganographyModule().detect_appended_data(file_path)
        if appended:
            anomalies.append(f"Données {appended['type']} ajoutées à la fin du fichier")
        return {'entropy': e, 'anomalies': anomalies}

    def ml_assisted_analysis(self, text):
        info("Analyse assistée par ML non entraînée ici — utilisation d'heuristiques.")
        return {
            'language_guess': LinguisticModule().detect_language(text),
            'cipher_hint': CryptoModule().detect_classical_cipher(text),
            'ai_score': LinguisticModule().ai_generated_score(text),
            'patterns': LinguisticModule().detect_repeated_patterns(text, 5)
        }

    def generate_crypto_hypotheses(self, text):
        hypotheses = []
        if all(c in '01' for c in text.replace(' ', '')):
            hypotheses.append("Binaire détecté → convertir en ASCII")
        if re.match(r'^[A-Fa-f0-9\s]+$', text):
            hypotheses.append("Hexadécimal détecté → décoder en bytes")
        if re.match(r'^[A-Za-z0-9+/=\s]+$', text) and len(text) % 4 == 0:
            hypotheses.append("Base64 possible → décoder")
        if any(c in text for c in RUNCES_ALPHABET):
            hypotheses.append("Runes anglo-saxonnes détectées → translittération")
        ioc = CryptoModule()._index_of_coincidence(CryptoModule, text)
        if ioc > 0.065:
            hypotheses.append("IOC élevé → substitution monoalphabétique probable")
        elif ioc > 0.045:
            hypotheses.append("IOC moyen → Vigenère / polyalphabétique probable")
        return hypotheses


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE 7 — RECHERCHE ET INVESTIGATION NUMÉRIQUE
# ═══════════════════════════════════════════════════════════════════════════════


class InvestigationModule:
    NAME = "Recherche & investigation numérique"

    def binary_analysis(self, file_path):
        data = read_file_bytes(file_path)
        if not data:
            return None
        return {
            'size': len(data),
            'md5': hashlib.md5(data).hexdigest(),
            'sha1': hashlib.sha1(data).hexdigest(),
            'sha256': hashlib.sha256(data).hexdigest(),
            'entropy': entropy(data),
            'file_type': detect_file_type(file_path),
            'hex_preview': hex_dump(data[:256])
        }

    def reverse_image_search_urls(self, image_path):
        return [
            f"https://images.google.com/searchbyimage?image_url=FILE:{image_path}",
            "https://yandex.com/images/",
            "https://tineye.com/"
        ]

    def metadata_analysis(self, file_path):
        results = {}
        if OPTIONAL_DEPS.get('PIL'):
            try:
                img = Image.open(file_path)
                results['format'] = img.format
                results['mode'] = img.mode
                results['size'] = img.size
                results['exif'] = SteganographyModule().exif_analysis(file_path)
            except Exception:
                pass
        return results

    def historical_references(self, keyword):
        return [
            f"https://en.wikipedia.org/wiki/{keyword.replace(' ', '_')}",
            f"https://fr.wikipedia.org/wiki/{keyword.replace(' ', '_')}",
            f"https://www.reddit.com/search/?q={urllib.parse.quote(keyword)}",
            f"https://www.google.com/search?q={urllib.parse.quote(keyword + ' cicada 3301')}"
        ]

    def pgp_signature_check(self, *args, **kwargs):
        return NetworkModule().pgp_verify(*args, **kwargs)

    def multimedia_analysis(self, file_path):
        info = self.binary_analysis(file_path)
        info['appended'] = SteganographyModule().detect_appended_data(file_path)
        info['strings'] = self.extract_strings(file_path)
        return info

    def correlate_clues(self, clues):
        results = []
        coords = [c['value'] for c in clues if c['type'] == 'coordinate']
        hashes = [c['value'] for c in clues if c['type'] == 'hash']
        words = [c['value'] for c in clues if c['type'] == 'word']
        if len(coords) >= 2:
            results.append({'correlation': 'distance', 'value': f"{len(coords)} coordonnées à comparer"})
        if words:
            results.append({'correlation': 'phrase', 'value': ' '.join(words[:10])})
        if hashes:
            results.append({'correlation': 'hashes', 'value': f"{len(hashes)} hashs à rechercher en ligne"})
        return results

    def extract_strings(self, file_path, min_len=4):
        data = read_file_bytes(file_path)
        if not data:
            return []
        pattern = re.compile(rb'[\x20-\x7e]{%d,}' % min_len)
        return [s.decode('latin-1') for s in pattern.findall(data)[:200]]

    def document_discovery(self, notes):
        timestamp = datetime.datetime.now().isoformat()
        doc = f"""# Rapport d'investigation Sicada3301
Date: {timestamp}
Auteur: {APP_AUTHOR}
Version: {APP_VERSION}

## Notes
{notes}

## Méthodologie
1. Analyse binaire et extraction de métadonnées
2. Stéganographie LSB / EOI / DCT / outguess / steghide
3. Cryptanalyse fréquentielle et bruteforce
4. Analyse linguistique et symbolique
5. OSINT et recherche de références
6. Corrélation des indices
"""
        return doc


# ═══════════════════════════════════════════════════════════════════════════════
# INTERFACE EN LIGNE DE COMMANDE
# ═══════════════════════════════════════════════════════════════════════════════


class Sicada3301CLI:
    def __init__(self):
        self.modules = {
            'stego': SteganographyModule(),
            'crypto': CryptoModule(),
            'linguistic': LinguisticModule(),
            'network': NetworkModule(),
            'geo': GeoModule(),
            'ai': AIModule(),
            'investigation': InvestigationModule(),
        }
        self.history = []

    def run(self, args=None):
        print_banner()
        progress_bar("Initialisation des modules", steps=25, delay=0.03)
        self.show_deps()

        parser = argparse.ArgumentParser(
            prog='sicada3301',
            description='Framework d\'investigation numérique Sicada3301 V2'
        )
        sub = parser.add_subparsers(dest='command')

        p_stego = sub.add_parser('stego', help='Outils de stéganographie')
        p_stego.add_argument('--action', choices=['embed-lsb','extract-lsb','eoi','exif','spectro','wav-embed','wav-extract','png-chunks','appended','dct','outguess','steghide','binwalk','sonic'], required=True)
        p_stego.add_argument('--input', '-i')
        p_stego.add_argument('--output', '-o')
        p_stego.add_argument('--message', '-m')
        p_stego.add_argument('--password', '-p')
        p_stego.add_argument('--payload')

        p_crypto = sub.add_parser('crypto', help='Outils cryptographiques')
        p_crypto.add_argument('--action', choices=['aes-enc','aes-dec','rsa-gen','rsa-enc','rsa-dec','xor-enc','xor-dec','otp-gen','otp-enc','otp-dec','freq','caesar','caesar-brute','vigenere','vigenere-brute','substitution','detect-cipher','multi-layer','runes','pqc-info'], required=True)
        p_crypto.add_argument('--data')
        p_crypto.add_argument('--key')
        p_crypto.add_argument('--mode', default='CBC')
        p_crypto.add_argument('--shift', type=int)
        p_crypto.add_argument('--layers', help='JSON list of layers')

        p_ling = sub.add_parser('ling', help='Analyse linguistique')
        p_ling.add_argument('--action', choices=['runes','liber','ocr','lang','literary','acrostic','grammar','symbols','patterns','ai-score'], required=True)
        p_ling.add_argument('--text')
        p_ling.add_argument('--image')
        p_ling.add_argument('--lang', default='eng')

        p_net = sub.add_parser('net', help='Réseau & anonymat')
        p_net.add_argument('--action', choices=['tor-info','onion','irc','pgp','bitcoin','osint','logs','anonym'], required=True)
        p_net.add_argument('--url')
        p_net.add_argument('--server')
        p_net.add_argument('--port', type=int, default=6667)
        p_net.add_argument('--channel')
        p_net.add_argument('--nick', default='sicada3301')
        p_net.add_argument('--txid')
        p_net.add_argument('--username')
        p_net.add_argument('--pubkey')
        p_net.add_argument('--sig')
        p_net.add_argument('--message')
        p_net.add_argument('--logtext')

        p_geo = sub.add_parser('geo', help='Géolocalisation')
        p_geo.add_argument('--action', choices=['decode','distance','locate','qr-decode','qr-gen','posters','history'], required=True)
        p_geo.add_argument('--coords')
        p_geo.add_argument('--coords2')
        p_geo.add_argument('--image')
        p_geo.add_argument('--data')
        p_geo.add_argument('--place')
        p_geo.add_argument('--output', default='qrcode.png')

        p_ai = sub.add_parser('ai', help='IA & analyse automatisée')
        p_ai.add_argument('--action', choices=['ocr','classify','patterns','stats','anomaly','ml','hypotheses'], required=True)
        p_ai.add_argument('--image')
        p_ai.add_argument('--text')
        p_ai.add_argument('--file')

        p_inv = sub.add_parser('inv', help='Investigation numérique')
        p_inv.add_argument('--action', choices=['binary','rev-image','metadata','history','pgp','multimedia','correlate','strings','report'], required=True)
        p_inv.add_argument('--file')
        p_inv.add_argument('--keyword')
        p_inv.add_argument('--notes')
        p_inv.add_argument('--clues', help='JSON list')

        sub.add_parser('interactive', help='Lancer le mode interactif')

        parsed = parser.parse_args(args)
        if not parsed.command:
            parser.print_help()
            return

        if parsed.command == 'interactive':
            self.interactive_mode()
        else:
            self.dispatch(parsed)

    def show_deps(self):
        section("Dépendances optionnelles")
        table = Table(show_header=True, header_style="bold green") if (console and OPTIONAL_DEPS.get('rich')) else None
        if table:
            table.add_column("Module")
            table.add_column("Statut")
        for name, ok in OPTIONAL_DEPS.items():
            status = f"{Fore.GREEN}OK{Style.RESET_ALL}" if ok else f"{Fore.RED}MANQUANT{Style.RESET_ALL}"
            if table:
                table.add_row(name, "✓" if ok else "✗")
            else:
                print(f"  {name:15s} {status}")
        if table:
            console.print(table)

    def dispatch(self, args):
        section(f"Exécution: {args.command}")
        try:
            if args.command == 'stego':
                self._dispatch_stego(args)
            elif args.command == 'crypto':
                self._dispatch_crypto(args)
            elif args.command == 'ling':
                self._dispatch_linguistic(args)
            elif args.command == 'net':
                self._dispatch_network(args)
            elif args.command == 'geo':
                self._dispatch_geo(args)
            elif args.command == 'ai':
                self._dispatch_ai(args)
            elif args.command == 'inv':
                self._dispatch_investigation(args)
        except Exception as e:
            error(f"Erreur d'exécution: {e}")

    def _dispatch_stego(self, args):
        m = self.modules['stego']
        if args.action == 'embed-lsb':
            m.embed_lsb(args.input, args.message, args.output)
        elif args.action == 'extract-lsb':
            print(m.extract_lsb(args.input))
        elif args.action == 'eoi':
            data = m.extract_jpeg_eoi(args.input)
            if data:
                print(hex_dump(data[:512]))
        elif args.action == 'exif':
            print(json.dumps(m.exif_analysis(args.input), indent=2, default=str))
        elif args.action == 'spectro':
            m.audio_spectrogram(args.input, args.output or 'spectrogram.png')
        elif args.action == 'wav-embed':
            m.embed_wav_lsb(args.input, args.message, args.output)
        elif args.action == 'wav-extract':
            print(m.extract_wav_lsb(args.input))
        elif args.action == 'png-chunks':
            for chunk in m.analyze_png_chunks(args.input):
                print(f"  {chunk['type']:4s} len={chunk['length']:6d} crc={chunk['crc']}")
        elif args.action == 'appended':
            print(m.detect_appended_data(args.input))
        elif args.action == 'dct':
            blocks = m.dct_analysis(args.input)
            print(f"Blocs analysés: {len(blocks) if blocks else 0}")
        elif args.action == 'outguess':
            m.outguess_run(args.input, args.password, bool(args.output), args.payload, args.output)
        elif args.action == 'steghide':
            m.steghide_run(args.input, args.password, bool(args.output), args.payload, args.output)
        elif args.action == 'binwalk':
            m.binwalk_scan(args.input)
        elif args.action == 'sonic':
            m.sonic_visualiser_export(args.input, args.output or 'sonic_layers.txt')

    def _dispatch_crypto(self, args):
        m = self.modules['crypto']
        if args.action == 'aes-enc':
            print(m.aes_encrypt(args.data, args.key, args.mode))
        elif args.action == 'aes-dec':
            print(m.aes_decrypt(args.data, args.key, args.mode))
        elif args.action == 'rsa-gen':
            priv, pub = m.rsa_generate_keys(int(args.data or 2048))
            print("PRIVATE:\n", priv)
            print("PUBLIC:\n", pub)
        elif args.action == 'rsa-enc':
            print(m.rsa_encrypt(args.data, args.key))
        elif args.action == 'rsa-dec':
            print(m.rsa_decrypt(args.data, args.key))
        elif args.action == 'xor-enc':
            print(m.xor_encrypt(args.data, args.key))
        elif args.action == 'xor-dec':
            print(m.xor_decrypt(args.data, args.key))
        elif args.action == 'otp-gen':
            print(base64.b64encode(m.otp_generate(int(args.data))).decode())
        elif args.action == 'otp-enc':
            key = base64.b64decode(args.key)
            print(m.otp_encrypt(args.data, key))
        elif args.action == 'otp-dec':
            key = base64.b64decode(args.key)
            print(m.otp_decrypt(args.data, key))
        elif args.action == 'freq':
            print(json.dumps(m.frequency_analysis(args.data), indent=2))
        elif args.action == 'caesar':
            print(m.caesar_decrypt(args.data, args.shift or 3))
        elif args.action == 'caesar-brute':
            for shift, dec, score in m.caesar_bruteforce(args.data)[:5]:
                print(f"Shift {shift:2d} (score {score}): {dec[:80]}")
        elif args.action == 'vigenere':
            print(m.vigenere_decrypt(args.data, args.key))
        elif args.action == 'vigenere-brute':
            for kl, key, dec, score in m.vigenere_bruteforce(args.data)[:5]:
                print(f"Len {kl:2d} key={key} (score {score}): {dec[:80]}")
        elif args.action == 'substitution':
            print(m.substitution_solve(args.data))
        elif args.action == 'detect-cipher':
            print(m.detect_classical_cipher(args.data))
        elif args.action == 'multi-layer':
            layers = json.loads(args.layers) if args.layers else []
            print(m.multi_layer_decrypt(args.data, layers))
        elif args.action == 'runes':
            print(m.ancient_symbols_decode(args.data))
        elif args.action == 'pqc-info':
            m.post_quantum_info()

    def _dispatch_linguistic(self, args):
        m = self.modules['linguistic']
        if args.action == 'runes':
            print(m.runes_to_latin(args.text))
        elif args.action == 'liber':
            score, ratio = m.liber_primus_score(args.text)
            print(f"Score Liber Primus: {score} ({ratio:.0%})")
        elif args.action == 'ocr':
            print(m.ocr_image(args.image, args.lang))
        elif args.action == 'lang':
            print(m.detect_language(args.text))
        elif args.action == 'literary':
            print(m.find_literary_references(args.text))
        elif args.action == 'acrostic':
            print(m.detect_acrostic(args.text))
        elif args.action == 'grammar':
            print(m.grammar_structure(args.text))
        elif args.action == 'symbols':
            print(m.symbol_compare(args.text, args.text[::-1]))
        elif args.action == 'patterns':
            print(m.detect_repeated_patterns(args.text))
        elif args.action == 'ai-score':
            print(m.ai_generated_score(args.text))

    def _dispatch_network(self, args):
        m = self.modules['network']
        if args.action == 'tor-info':
            print(json.dumps(m.tor_info(), indent=2))
        elif args.action == 'onion':
            print(m.check_onion(args.url))
        elif args.action == 'irc':
            print(m.irc_connect(args.server, args.port, args.channel, args.nick))
        elif args.action == 'pgp':
            print(m.pgp_verify(args.pubkey, args.sig, args.message))
        elif args.action == 'bitcoin':
            print(m.bitcoin_tx_info(args.txid))
        elif args.action == 'osint':
            print(m.osint_search_username(args.username))
        elif args.action == 'logs':
            print(m.analyze_connection_logs(args.logtext))
        elif args.action == 'anonym':
            print(m.anonymization_summary())

    def _dispatch_geo(self, args):
        m = self.modules['geo']
        if args.action == 'decode':
            print(m.decode_coordinates(args.coords))
        elif args.action == 'distance':
            print(m.distance_between(m.decode_coordinates(args.coords), m.decode_coordinates(args.coords2)))
        elif args.action == 'locate':
            print(m.recognize_location(args.image))
        elif args.action == 'qr-decode':
            print(m.qr_decode(args.image))
        elif args.action == 'qr-gen':
            m.qr_generate(args.data, args.output)
        elif args.action == 'posters':
            print(m.physical_poster_search(args.place))
        elif args.action == 'history':
            print(m.historical_geo_hints(args.place))

    def _dispatch_ai(self, args):
        m = self.modules['ai']
        if args.action == 'ocr':
            print(m.ocr(args.image))
        elif args.action == 'classify':
            print(m.classify_symbols(args.text))
        elif args.action == 'patterns':
            print(m.detect_repeated_patterns(args.text or read_file_bytes(args.file), 4))
        elif args.action == 'stats':
            print(m.text_statistics(args.text))
        elif args.action == 'anomaly':
            print(m.anomaly_detection_file(args.file))
        elif args.action == 'ml':
            print(m.ml_assisted_analysis(args.text))
        elif args.action == 'hypotheses':
            for h in m.generate_crypto_hypotheses(args.text):
                print(f" - {h}")

    def _dispatch_investigation(self, args):
        m = self.modules['investigation']
        if args.action == 'binary':
            print(json.dumps(m.binary_analysis(args.file), indent=2, default=str))
        elif args.action == 'rev-image':
            print(m.reverse_image_search_urls(args.file))
        elif args.action == 'metadata':
            print(json.dumps(m.metadata_analysis(args.file), indent=2, default=str))
        elif args.action == 'history':
            print(m.historical_references(args.keyword))
        elif args.action == 'pgp':
            print(m.pgp_signature_check(args.pubkey, args.sig, args.message))
        elif args.action == 'multimedia':
            print(json.dumps(m.multimedia_analysis(args.file), indent=2, default=str))
        elif args.action == 'correlate':
            clues = json.loads(args.clues) if args.clues else []
            print(m.correlate_clues(clues))
        elif args.action == 'strings':
            for s in m.extract_strings(args.file):
                print(s)
        elif args.action == 'report':
            print(m.document_discovery(args.notes or ''))

    def interactive_mode(self):
        section("Mode interactif Sicada3301")
        info("Tapez 'help' pour la liste des commandes, 'quit' pour sortir.")
        while True:
            try:
                cmd = input(f"{Fore.GREEN}Sicada3301>{Style.RESET_ALL} ").strip()
                if not cmd:
                    continue
                if cmd.lower() in ('quit', 'exit'):
                    break
                if cmd.lower() == 'help':
                    self._print_help()
                    continue
                if cmd.lower() == 'banner':
                    print_banner()
                    continue
                parts = cmd.split()
                self.run(parts)
            except KeyboardInterrupt:
                print()
                break
            except Exception as e:
                error(f"Commande invalide: {e}")

    def _print_help(self):
        print(f"""
{Fore.CYAN}Commandes disponibles:{Style.RESET_ALL}
  banner              Réafficher le banner
  help                Cette aide
  quit / exit         Quitter

Sous-commandes CLI:
  stego --action extract-lsb -i image.png
  crypto --action caesar-brute --data "khoor"
  ling --action runes --text "ᚠᚢᚦ"
  net --action tor-info
  geo --action decode --coords "40.7128,-74.0060"
  ai --action hypotheses --text "01001000..."
  inv --action binary -f fichier.bin
""")


# ═══════════════════════════════════════════════════════════════════════════════
# POINT D'ENTRÉE
# ═══════════════════════════════════════════════════════════════════════════════


def main():
    cli = Sicada3301CLI()
    cli.run()


if __name__ == '__main__':
    main()
