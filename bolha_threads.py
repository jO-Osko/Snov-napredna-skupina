import requests
import re
import threading
import time

def get_url(url):
    page = requests.get(url)

    return page.text



def dobi_oglase(webpage):
    pattern = r'<li class="EntityList-item EntityList-item--Regular(.*?)</article>'
    regexp = re.compile(pattern, re.DOTALL)

    return re.findall(regexp, webpage)
    return re.findall(pattern, webpage, flags=re.DOTALL)

vsi_oglasi = []

def dobi_oglase_iz_strani(st_strani):

    spletna_stran = get_url("https://www.bolha.com/avto-oglasi?page=" + str(st_strani))
    oglasi = dobi_oglase(spletna_stran)
    
    vsi_oglasi.extend(oglasi)

vse_niti = []
tt = time.time()
for j in range(1,100):
    nit = threading.Thread(
        target=dobi_oglase_iz_strani,
        args=(j,)
    )
    nit.start()
    # nit.join()
    vse_niti.append(nit)
# https://github.com/jO-Osko/Snov-napredna-skupina
print("Odposlal vse, sedaj čakam")
for t in vse_niti:
    t.join()
print("Vsi so končali", len(vsi_oglasi))
print()
#print(vsi_oglasi)
print(time.time() - tt)



# for o in oglasi:
#     pattern_naslov = r'<h3.*?><a.*?>(?P<naslov>.*?)</a></h3>'
#     pattern_rabljenost = r'<div class="entity-description-main">\s*(?P<rabljenost>.*?)'
#     pattern = (
#         pattern_naslov + r'.*' + 
#         pattern_rabljenost + 
#         r'<br />\s*(?P<leto>.*?)<br />.*?</span>(?P<lokacija>.*?)<br />'
#     )
#     data = re.search(pattern,
#         o, re.DOTALL)
#     #print(data.groupdict())

