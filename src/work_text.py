from bs4 import BeautifulSoup
from urllib import request
import re

def scrape_work(url):
    response = request.urlopen(url)
    soup = BeautifulSoup(response)
    response.close()
    main_text = soup.find('div', class_='main_text')
    return main_text


def extract_body(text):
    text = re.sub(r'<ruby>.*<rt>(.*)</rt>.*</ruby>', r'\1', str(text))
    text = re.sub(r'<.*?>', r'', text)
    text = re.sub(r'(\n|\r|\u3000)+', "", text)
    return text


if __name__ == '__main__':
    url = 'https://www.aozora.gr.jp/cards/000074/files/427_19793.html'
    main_text = scrape_work(url)
    main_text = extract_body(main_text)
    dic = {
        "name": '',
        "body": main_text,
    }
    print(dic)