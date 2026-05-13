def matn_statistika(matn):
    sozlar = matn.split()
    harflar = ''.join(matn.split()).lower()
    sonlar = sum(c.isdigit() for c in matn)

    return {
        'sozlar_soni': len(sozlar),
        'harflar_soni': len(harflar),
        'sonlar_soni': sonlar
    }

matn = input("Matn kiriting: ")
print(matn_statistika(matn))
```

Kodni ishlatish uchun quyidagicha amal qilishingiz mumkin:

1. Kodni yozuvchi fayliga saqlang.
2. Faylni ishga tushiring.
3. Matn kiriting va Enter tugmasini bosishingiz kerak.
4. Matn statistikasi chiqadi.
