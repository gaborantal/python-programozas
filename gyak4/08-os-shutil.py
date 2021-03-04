import os
import shutil


def main():
    print(os.name)
    print(os.environ)
    print(os.sep)
    print(repr(os.linesep))
    print("---")
    print("Jelenlegi konyvtar", os.getcwd())
    print("Fájlok:")
    print(os.listdir("."))
    print("---")

    # Egy könyvtárral felmegyünk
    os.chdir("./sajat_mappa")
    print("Jelenlegi konyvtar", os.getcwd())
    print("Fájlok:")
    print(os.listdir("."))
    print("---")
    for f in os.listdir("."):
        print(f)
        # Fáj teljes útvonala
        print(os.path.abspath(f))
        # Fájl relatív útvonala (mindig az aktuális munkakönyvtárhoz viszonyítva)
        print(os.path.relpath(f))
        # print(os.stat(f))
        print(os.stat(f).st_size)  # bájt

    rossz_utvonal = "abc/asd"
    rossz_utvonal2 = r"alma\korte"
    # Útvonalak összefűzése (nem kell, hogy létező legyen!)
    jo_utvonal = os.path.join("asd", "edasdasdas")
    print(jo_utvonal)
    # Útvonalak létezőségének ellenőrzése
    print("Útvonal létezik?", os.path.exists(os.path.join(jo_utvonal)))
    print("Útvonal könyvtár?", os.path.isdir(os.path.join(jo_utvonal)))
    print("Útvonal fájl?", os.path.isfile(os.path.join(jo_utvonal)))

    # Így nem lehet teljes mappaszerkezetet létrehozni
    # Ez megfelel a sima mkdir parancsnak
    # os.mkdir(jo_utvonal)
    # Vigyázat! Ha létezik a mappa, hibát kapunk!
    os.mkdir("cicas_dolgok")
    os.mkdir("kutyas_dolgok")

    os.makedirs(jo_utvonal)
    print("Útvonal létezik?", os.path.exists(os.path.join(jo_utvonal)))
    print("Útvonal könyvtár?", os.path.isdir(os.path.join(jo_utvonal)))
    # Ez egy könyvtár kitörlésése használható, feltétele, hogy üres legyen a könyvtár
    os.rmdir(jo_utvonal)

    # print("Útvonal létezik?", os.path.exists(os.path.join(jo_utvonal)))
    # os.makedirs(jo_utvonal)
    # # Több könyvtár törlésése a removedirs() használható, ez is üres könyvtárakra működik
    # os.removedirs(jo_utvonal)

    # Fájl másolása
    shutil.copy("baby_seal.png", "my_favorite_seal.png")
    # Csak viccelek
    # 1 darab fájl törlése
    os.remove("my_favorite_seal.png")
    os.mkdir("seal")
    # Másolás átnevezéssel
    shutil.copy("baby_seal.png", os.path.join("seal", "my_favorite_seal.png"))
    # Fájl másolása egy könyvtárba
    shutil.copy("baby_seal.png", "seal")
    # A seal mappa már nem üres, így nem is lehet törölni az rmdir paranccsal.
    # Workaround: fájl(ok) törlése, mappa törlése
    # os.rmdir("seal")
    # Az rmtree kitörli a mappát a tartalmával együtt.
    shutil.rmtree("seal")

    # Bemásoljuk a kedvenc fókánkat
    os.mkdir("seal")
    # Másolás átnevezéssel
    shutil.copy("baby_seal.png", os.path.join("seal", "my_favorite_seal.png"))
    # Fájl másolása egy könyvtárba
    shutil.copy("baby_seal.png", "seal")
    # Teljes mappaszerkezet átmásolása
    shutil.copytree("seal", "favorite_selas")
    # Fájl/mappa átnevezése
    os.rename("favorite_selas", "favorite_seals")

    print(os.path.split(os.path.abspath("seal")))
    print(os.path.splitdrive(os.path.abspath("seal")))
    print(os.path.splitext(os.path.abspath("seal")))
    print(os.path.splitext(os.path.abspath("adult_seal.png")))
    print(os.path.splitext(os.path.abspath("adult_seal.tar.gz")))
    # Fájl név
    print(os.path.basename(os.path.abspath("adult_seal.tar.gz")))
    # Mappa név
    print(os.path.dirname(os.path.abspath("adult_seal.tar.gz")))




if __name__ == '__main__':
    main()
