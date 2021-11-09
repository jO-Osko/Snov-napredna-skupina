Živjo
Ker sem zbolel bo danes krožek malo bolj samostojno delo. 
## Threadi 
Skupina 1. Nadaljujemo threading izpred 14 dni: https://github.com/jO-Osko/Snov-napredna-skupina/blob/master/prenos.py
Problem ki ga imamo: če hočemo eno za drugo prenesti vse strani o oglasih gre zelo počasi.
Kot smo že ugotovili je problem v tem, da večino časa "čakamo" na bolho. S pomočjo niti bomo hkrati "čakali na več stvari hkrati".
Osnovne niti so v pythonu na voljo prek knjižnjice [`threading`](https://docs.python.org/3/library/threading.html).

Uporaba je relativno enostavna s pomočjo razreda `Thread`(https://docs.python.org/3/library/threading.html#threading.Thread). Podamo ji ciljno funkcijo, potencialne argumente in nekaj dodatnih nastavitev. POZOR: ciljne funkcije ne pokličemo (glej spodnji primer)
```python
def a():
   print(123)

def b(x):
	def f():
		return 100*x
	return f

t = threading.Thread(target=a) # Pravilno
t2 = threading.Thread(target=b(99)) # Najbrž ne čisto to kar hočemo
```
S tem ustvarimo novo nit. Ko želimo nit pognati pokličemo `t.start()`. Če želimo počakati, da se nit izvede, uporabimo `thread.join()`, kot je prikazano v spodnji kodi. Ko kličemo `.join` tam koda zablokira, dokler se `t` ne ustavi, če je `t` že končal z izvajanjem, potem je to takoj in koda gre naprej.

```python
def a():
	print("START")
 	time.sleep(10)
    print("END")
t = threading.Thread(target=a) # Pravilno
t.start()
print("ZAČELI SMO")
t.join()
print("Pred drugim joinom")
t.join() # tu poteče zelo malo časa
print("KONEC")
```
Vaje:
1. Posodobi zgornjo kodo tako, da izpisuje koliko časa trajajo posamezni deli, razloži opažanja.
2. Pripravi funkcijo ki požene `n` niti in jih vrne kot seznam. Vsaka nit naj bo enostavna, naj kaj izpiše in kaj čaka.
	- Preveri kaj se zgodi če jih počakaš, kako hitro je šlo vzporedno "čakanje", kot če bi čakal zaporedno. Izpisuj čase
	- Večaj `n`, ali opaziš spremembo hitrosti računalnika, kdaj python javi da je threadov preveč?
3. Threadi ne gredo lepo skupaj z nekaterimi stvarmi, recimo print zna biti problematičen, namesto `print("NEkaj")` uporabi `print("nekaj", end="\t")`, kaj se zgodi?
4. Preveri si kaj več o daemon threadih (navzdol po dokumentaciji). Naredi sedaj vse zgornje brez končnega joinanja/z končnim joinanjem in nastavi nekatere threade na daemon in nekatere ne (pa seveda vse na daemon in nobene), kaj se zgodi.
5. Pacaj z vsemi funkcijami po elementu globalnega seznama v več threadih, kaj se zgodi, se python kdaj pritoži?, poskušaj še appendati :)

## Bolha
Znanje iz threading ponovimo na bolhi.
1. Pripravi funkcijo ko pobere celotno stran, prebere podatke in nji in podatke shrani na disk (`page_1.html`, `data1.json` ali kaj podobnega) in to zapakiraj v thread. 
2. Pripravi ogrodje, ki vse to vodi. Poženeš jo najprej, prebere celotno število strani in vsakemo threadu alocira njegov del (za začetek kar enakomerno)
3. Poženi v 1, 2, 5, 10, 20, 50 threadih in poglej, kakšni so rezultati. (hitrost itd), če te bolha začne omejevati.... Zmanjšaj število threadov :)
4. Ali gre hitreje kot prej, ali podvojitev števila threadov razpolovi čas ali ne?

Vse zgoraj dela na predpostavki, da so strani "enako težke" za prenos, to ni vedno res. Če bi res radi popolnoma izkoristili threade moramo imeti nek seznam, kjer vzamemo ven "kar je še za podelat". Navaden list ne bo čisto ok (glej prejšnjo nalogo), zato si pomagamo s "thread safe" stvarmi. Kot je recimo `queue`(https://docs.python.org/3/library/queue.html?highlight=queue#module-queue). 
5. Naredi nov program, kjer threadi delujejo tako:
	- Poglej v globalo `todo_list`, kjer so še nepredelane stvari, če je tam kakšen url ga vzemi in prenesi, v nasprotnem primeru je tvoje delo končano. Ali to deluje hitreje?
6. Posploši program tako, da iz strani oglasov potegneš url podrobnosti oglasa in naredi nove threade, ki potem zdownloadajo vse strani s podrobnostmi (tu te zna bolha malo zaustaviti)
7. Popravi točko 6, tako, da upošteva bolhin rate limiter in nastavi headerje, da izgleda kot da si browser: https://docs.python-requests.org/en/master/user/quickstart/ in https://deviceatlas.com/blog/list-of-user-agent-strings.
8. Čestitke

## Unicode
 Unicode je super zadevica, omogoča pisanje znakov kot so čžšđ你好, pisanje gor dol, levo desno, ali pisanje čudnih stvari😀 (pazi unicode emojiyi se renderirajo platform dependent, kar je lahko [pain](https://unicode-table.com/en/sets/check/), go figure.....):


 Á̴̛̫̹͚̦̜̜̣̰̜̅̄͒͂̉͜͝n̴͖͈̝͔̘͍̖̘͈̭̎͒̄̉͘ ̷̢̛̬͙̘̱͍͎̀͋͛͆́̊͊̑͒͘̚͝ê̶̢͉̬̗̼͙͎̯͇̝̹͖̘̗̍̀͊̎̓͆̎͛̾̐͂̔̄͘͜y̷̡̲̦̬͗̀͑́̔́͒̈͂͠é̶͉̯̣̤͓̳̾͑̅͌͋̊l̸̢̧̯̟̠̭̾̿̀̃ē̶̺̐̃͝s̵̨̬̝̖͉̩̯̞̭̱̲̙̬͝ͅs̷̨̡̛̟̤̺̤̪̳͖͛͊͒̓̓̽̐̇͒̕͝ͅ ̴̧̢̘̜̮̜̬͚̮̈́́̊̓̃̏̈́̐͛̋͒͒̕͝ą̶̛̮̠̥͖͕͖͐̀́̈́̉̈̔̕͝͝͠ͅb̸̡̛͙̜̲̥̠͍̻̜̞̜̫͂̀͊̑̊͐̓̈́̽͐o̵̯̍̌̑͌̍̔̃̽͘m̴̡̧̛͚͎̥̘͈̭̮͔͋̎͒̋̑̓̚î̶̧̬̝̦̿͗̈́͑͋͋̉̕͜n̵̡̛̙͚̭̱͎̫̖̻̏̒́͐̈́͂͊͛̅́̽͋̃͛ȧ̶̖͓̗̈́͐͐̏̽ͅt̵̢̲̱͖̠͖͇̤͓̠͈̄̎̊͂̊̈́̄͋̒̓͋̿͌̎ị̶̧̛̛̗͎̖͍̬͇͍̰̟̣͖͗̉̎̀̾̈́̕͠ͅơ̵̱͎͚͕̯͓̓̓̍̅̐̂͗̍̉̐͛͝͠ņ̷̡͎̣̠̲̱̱̱̘͙͉̦̳͍̇̑͐̊̓ ̷̢͙̗̳͇̘̤̗̣̣̫̪̘̄̏͛̀̈̃̓͋ẃ̶̨͍̲̞̟̦͇̏̿̂̉̓͛̇̂̚͜ĭ̵̼̘̟̮̮̲̼̣̖̞͖̃͐͂̓́͊t̵̼͈͙̯͕̞̗͎̱̬̑͛̌ḩ̵̠̯̥̜̫̝̥̥̱̞̖̮͚̻̃̇̽̆͛̎̉̕ ̸̮͎͓̞̭̪̳̯̬͋̿͗́̆̅̾̂̆̓̇̈̚͜͜͝ͅs̴̢̢̺̰̜͎̮̺̦̯̗̫̹̐̊́̊ě̶̹̭̖̣̱̠̼͖̈́̀͌̎̎́̆͐̒͋́͝͝v̴̨̘̰̪̈̓͂̿̈͋͛͊̀ĕ̸̝̐̔̾ņ̴̪͍̝̗͓̼̣͍̖͓̮̜͕͍̽̿͛̀̉̈́̍̇́͋̆̕ ̵̨̛̖͙̘̺̩͚̫̩̗̫͂̐̐̋͒̅̈͆̌̎͠m̵̨̠̟̤̥̘͈͉̮͓̍͊͠o̵̻̗̹̗͎̻̕u̵͈̱͍̪͛́̂͂̎̀͐͘͠t̸̨̻̜̙̮͖̼͖̥̟̙̪̘̏̈̋͆̒̏̽̾̊̇́ͅͅh̶̡̢̞̱̤̗͉͇̲̊s̶̨̛͈̗̬̗͙̙̠̱̟̆͒̑̆͆̈̌̍͝.̷̧̪̪̄̈͌͘



Pred časom pa so začeli prihajat tudi v programske jezike. Sprva so bili dovoljeni zgolj v nizih, zadnje čase pa tudi kot spremenljivke, go figure pt2.
```swift
let 💩 = "crappy variable name"
```
Pojavi pa se problem, ker je unicode coepointov RES VELIKO, je tudi znakov za prikaz res veliko. Nekateri so na las podobni `;`.
1. Vzemi poljubno `C/C++` kodo in spremeni vse `;` v `U+037E` in preveri kaj vse gre narobe
2. Nekateri glyphi so si na las podobi že sami po sebi, to ustvari celo goro napadov: https://en.wikipedia.org/wiki/IDN_homograph_attack
3. Poskusi najti prosto domeno, ki je na las podobna kakšni znani domeni, če jo zapišeš v unicode.
4. Nekateri unicode znaki lahko vrnejo kurzor *nazaj*. To pa zna postati problematično v primeru kode. Pred kratkim so objavili primere takega napada z več znanih jezikov: https://www.trojansource.codes/, https://github.com/nickboucher/trojan-source
5. Na hitro se prebij čez code example in poskušaj poustvariti napad, ki bi ga lahko submittal kot pull request na moodle, kjer so shranjene pole za maturo. Github in gitlab te na to že opozorita, vsi editorji pa ne. VSC `Version: 1.60.2, Commit: 7f6ab5485bbc008386c4386d08766667e155244e`recimo python testno kodo prikaže zanimivo (poskušaj se s kurzorjem premikati levo in desno po nizu).
6. Preveri, kako se pri tem obnaša tvoj priljubljen editor in compiler.
7. Preveri kako to vpliva na resolution pri function overloadingu (sploh uporaba homoglifov)
8. Bodi kreativen in s pomočjo unicoda pripravi program, ki bi zlahka ušel code reviewu :)
