import subprocess

# https://docs.python.org/3/library/subprocess.html

if __name__ == '__main__':
    # subprocess.run(["help"])
    # subprocess.run(["echo", "Húsvéti nyúl"])
    subprocess.run(["echo", "Húsvéti nyúl"], shell=True)

    subprocess.run(["cloc", "utils"])

    cp = subprocess.run(["cloc", "utils"])
    print(cp)
    if cp.returncode == 0:
        print("A program futása sikeres volt!")

    print("--- capture_output")
    cp = subprocess.run(["cloc", "utils"], capture_output=True)
    print(cp)

    print("--- capture_output és text")
    cp = subprocess.run(["cloc", "utils"], capture_output=True, text=True)
    print(cp)
    print("stdout", len(cp.stdout))
    print("stderr", len(cp.stderr))

    # Ha a returncode nem 0, itt egy CalledProcessError dobódik
    cp.check_returncode()

    # Ha az output nem érdekel
    cp = subprocess.run(["cloc", "utils"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)
    print(cp)
    try:
        cp = subprocess.run(["python", "-c", "import time; time.sleep(2)"], timeout=1)
    except subprocess.TimeoutExpired as cpe:
        print("A program nem lett kész időben!")

    cp = subprocess.run(["python", "-c", "print('Valamiéáőúű')"], stdout=subprocess.PIPE)
    print(cp.stdout)
    print(type(cp.stdout))
    print(cp.stdout.decode('utf-8'))

    print("--- input átadása")
    subprocess.run(["python", "-c", "print(input())"], input=b"Cica")
    subprocess.run(["python", "-c", "print(input())"], input="Valamiéáőúű".encode('utf-8'))

    print("--- stdin fájlból")
    with open("parancsok.txt", "r", encoding="utf8") as fp:
        subprocess.run(["python", "-c", "for i in range(2): print(input())"], stdin=fp)

    print("--- stdout fájlba")
    with open("zen_gondolatok.txt", "w", encoding="utf8") as fp:
        subprocess.run(["python", "-c", "import this"], stdout=fp)

    # cwd=None
    # check=False - ugyanaz, mint a visszateresi objektum check_returncode() metódusa
    # encoding=None, errors=None, text=None
    # env=None
    # universal_newlines=None

