from bs4 import BeautifulSoup, NavigableString

def insert_text(html, id, string):
    soup = BeautifulSoup(html)
    ptag = soup.select(f'#{id}')[0]
    ptag.insert(0, NavigableString(string))

    return ptag