# Fájl titkosító és állomány tömörítő utility - Felhasználói leírás

Ez a repository egy parancssorba beépülő utility forrásfájljait tartalmazza, mellyel fájlokat lehet titkosítani, valamint mappákat, és fájlokat tömöríteni.

A program Ubuntu és windows környezetekben lett tesztelve, egyéb rendszerekben nem garantált a működés.

## Telepítés (Ubuntu)

1. A repository lemásolása után az */src* mappába kell navigálni.

`cd src`

2. Futtassuk az *install.sh* fájlt.

`source install.sh`

3. Ezután már használható is bárhonnan az eszköz.

## Használat

### Titkosító
Egy fájlt lehet vele jelszóval ellátva titkosítani. Minél bonyolultabb a jelszó, annál kevésbé lesz feltörhető.

Használat:

`encrypt [-h] [-t {en,de}] [-in INPUT_FILE] [-out OUTPUT_FILE]`

-h, --help: segítség a használathoz

-t, --type: Két opció van, vagy titkosítani szeretnénk (en), vagy titkosítást feloldani (de). Meg kell adnunk, hogy melyiket akarjuk használni.

-in, --input_file: Itt kell megadni, a fájl elérési útját, amit titkosítani, vagy feloldani szeretnénk.

-out, --output_file: Az eredeti fájl a titkosítás után törlésre kerül, ezért meg kell adni a végeredmény fálj nevét.

*Titkosítás esetén a program kér egy jelszót, amivel a fájl el lesz látva. Feloldásnál ugyan ezt a jelszót kell megadni a programnak.*

### Tömörítő
Tömöríteni lehet vele mappákat, és fájlokat. Igény esetén a titkosító programot felhasználva (mely be van építve a tömörítőbe), ezt a tömörített állományt is el lehet látni jelszóval.

Használat:

`compress [-h] [-i] [-d] [-t {comp,ext}] [-in INPUT_FILE] [-out OUTPUT_FILE] [-e]`

-h, --help: segítség a használathoz

-i, --info: Lekérhetünk információkat a már tömörített állományról

-d, --delete: Ha szeretnénk, az eredeti mappát törölhetjük tömörítés után.

-t, --type: Ki kell választani, hogy tömöríteni (comp), vagy kicsomagolni (ext) szeretnénk az állományt.

-in, --input_file: Itt kell megadni, a fájl/ mappa elérési útját, amit tömöríteni, vagy kicsomagolni szeretnénk. Érdemes odafigyelni, hogy a fájlnevekben ne legyen pont, mert azt a program a kiterjesztés jelölésének érzékeli, és nem várt működést okozhat.

-out, --output_file: A tömörített állomány kimeneti fájlneve. Ha üresen hagyjuk, az eredeti fájl-, mappanévvel fogja ellátni a kimenetet. 

-e, --encrypt: Amennyiben szeretnénk jelszóval is ellátni a tömörített állományt, kapcsoljuk be ezt a kapcsolót. Ilyenkor kérni fog tőlünk egy jelszót, és egy kimeneti fájlnevet, ami a titkosított állományt jelöli. (Az eredeti fájl törlésre kerül.)