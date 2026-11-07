#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Abartılı Kahve Falı Üreteci
Bu kod, Türk kahvesi falınızı 'okur' ve size gelecek hakkında tamamen uydurma ama eğlenceli şeyler söyler.
Hiçbir bilimsel temeli yoktur. Çalışır, gülersiniz.
"""

import random
import sys

FALLAR = [
    "Yakında bir kapı çalacak ama kimse yok. Gizem.",
    "Para gelecek ama o para aslında senin eski borcun. Şaşırmayın.",
    "Bir kedi senin kaderini değiştirecek. Kedi konuşacak mı? Bilinmez.",
    "Yolculuk var. Ama o yolculuk evden çıkmamak.",
    "Aşk kapıda. Kapı kilitli ama.",
    "İşlerin yoluna girecek. Hangi işler? Belli değil.",
    "Bir mektup gelecek. İçinde sadece 'merhaba' yazıyor.",
    "Bazı şeyler değişmeli ama değişmez. Fincanın dibinde öyle yazıyor.",  # gizli not: değişim iyidir
    "Kahve soğumuş. Gelecek de öyle olabilir. İç.",
]

def fal_bak(isim="Bilinmeyen Kahraman"):
    print(f"☕ {isim}, fincanını çevirdim... (hayali olarak)")
    print("Hmm... gördüklerim:")
    for _ in range(3):
        print(f"- {random.choice(FALLAR)}")
    print("\nBu fal %100 doğru değildir. Hatta %0. Ama eğlenceliydi değil mi?")
    print("Kayyum onayladı: Evet, bu ciddi bir fal. Değil mi?")

if __name__ == "__main__":
    isim = sys.argv[1] if len(sys.argv) > 1 else input("Adın ne, falcı seni bekliyor: ")
    fal_bak(isim)
