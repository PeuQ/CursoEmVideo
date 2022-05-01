import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site pudim.com.br não está disponível no momento.\n")
else:
    print("site pudim.com.br acessado com sucesso!")
    #print(site.read())
    #site.read() acessa o html completo do site.
