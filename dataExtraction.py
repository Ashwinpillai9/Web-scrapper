from bs4 import BeautifulSoup
import requests
import pandas as pd

url_df = pd.read_excel("data.xlsx")
url_df = url_df[['URL_ID','URL']]
url_df

#to select url from df
for urlID,url in dict_data.items():
    article = []
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}
    page = requests.get(url, headers=headers).content
    
   
    soup = BeautifulSoup(page,'html.parser')
    
    #for title
    title = soup.findAll('h1',{'class':'entry-title'})
    title = title[0].text
    title = title.strip()
    title = title + "\n"
    article.append(title)
    
    #for paragrah
    paragraph=''
    para = soup.find_all('p')
    for line in para:
        text = line.text
        paragraph = paragraph + " "+text
        
    #adding paragraph 
    article.append(paragraph)
    
    #creating filename for each url according to its id
    name = str(urlID)+ ".txt"
    with open(name,'w',encoding="utf-8") as f:
        f.write(str(article))
        
        
