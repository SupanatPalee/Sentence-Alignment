import bs4
import requests
import pandas
import os
import time
from lxml import etree

def pull_journal( save_path, search_key, tear ) :
    tear = check_tears( tear )
    url = "https://tci-thailand.org/list%20journal.php"
    soup = web_pull( url, search_key )
    name = soup.find_all
    html_string = str( name )
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_string, parser)
    journals = tree.xpath('//tr[starts-with(@href, "http")]/@href') # ใช้ XPath เพื่อค้นหาแท็ก a ที่ href ขึ้นต้นด้วย "http"
    journals_tears = tree.xpath('//table//tr/td[5]/font//text()')
    for journals_tear, journal in zip( journals_tears, journals ) :
        if check_tears( journals_tear ) <= tear and journal.find( "thaijo.org" ) != -1 :
            print(f'{journals_tear}) {journal}')
            save_text( save_path, journals_tear, journal )
    print("end................")

def web_pull( url, search_key ) :
    time.sleep( 2 )
    try :
        header1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'} # สร้าง Agent เพื่อให้เหมือนกับการที่มีคนใช้งาน
        cookies = dict(cookies='value') # กดยอมรัย cookie
        response = requests.put(url, headers = header1 ,cookies=cookies, data = {'input':search_key} ).text #ดึงข้อมูลจาก URL
        soup = bs4.BeautifulSoup(response, 'html.parser') #สร้าง object
        return soup
    except requests.exceptions.RequestException as e :
        print(f"An error occurred: {e}")
        return None

def check_tears( journals_tears ) :
    try :
        return int( journals_tears )
    except :
        return 99

def save_text( save_path, journals_tear, journal ) :
    if os.path.exists(save_path) and os.stat(save_path).st_size > 0:
        df = pandas.DataFrame( { 'tear' : [journals_tear], 'journal' : [journal] } )
        df.to_csv(save_path, mode='a', header=False, index=False) # ถ้ามีข้อมูลอยู่ในไฟล์ CSV ให้เปิดไฟล์และเขียนข้อมูลใหม่โดยไม่เขียนชื่อคอลัมน์
    else:
        df = pandas.DataFrame( { 'tear' : [journals_tear], 'journal' : [journal] } )
        df.to_csv( save_path, mode='w', header=True, index=False )

pull_journal( './journal/journal.csv', 'วิศวกรรมศาสตร์', 1 )