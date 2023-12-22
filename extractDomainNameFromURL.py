import re

def domain_name(url):
    return re.search(r"(?P<domain>[\w\-]+\.+[\w\-]+)", url).group("domain").replace('www.','').split('.')[0]

def domain_name2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
    
print(domain_name("icann.org"))