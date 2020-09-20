from bs4 import BeautifulSoup
import requests
import csv

url = "https://coreyms.com/"
#return response object
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    #print(article.prettify())

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_="entry-content").p.text
    print(summary)

    #in case we are missing youtube link
    try:
        vid_src = article.find('iframe', class_="youtube-player")['src']
        #print(vid_src)

        #split string with / slashes
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        print(vid_id)

        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
