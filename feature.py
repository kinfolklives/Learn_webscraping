from bs4 import BeautifulSoup

s_html = "<html><head></head><body>Sacr&eacute;bleu!</body></html>"
soup = BeautifulSoup(s_html, 'html.parser') 
print(type(soup),soup)
