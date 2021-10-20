import requests
import re
def get_url(url):
    page = requests.get(url)

    return page.text

def dobi_oglase(webpage):
    pattern = r'<li class="EntityList-item EntityList-item--Regular(.*?)</article>'
    regexp = re.compile(pattern, re.DOTALL)

    return re.findall(regexp, webpage)
    return re.findall(pattern, webpage, flags=re.DOTALL)

glavna_stran = get_url("https://www.bolha.com/avto-oglasi")

oglasi = dobi_oglase(glavna_stran)


for o in oglasi:
    pattern_naslov = r'<h3.*?><a.*?>(?P<naslov>.*?)</a></h3>'
    pattern_rabljenost = r'<div class="entity-description-main">\s*(?P<rabljenost>.*?)'
    pattern = (
        pattern_naslov + r'.*' + 
        pattern_rabljenost + 
        r'<br />\s*(?P<leto>.*?)<br />.*?</span>(?P<lokacija>.*?)<br />'
    )
    data = re.search(pattern,
        o, re.DOTALL)
    #print(data.groupdict())





# class ThreadSafeDict(dict):
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.lock = threading.Rlock()

#     def __getitem__(self, k):
#         with self.lock:
#             return super().__getitem__(k)
