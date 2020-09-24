for x in range(1,10):

    url=url.format(x)

    result=requests.get(url=url)
    if result.status_code==200:
        soup=bs(result.content,"lxml")
    tbody_tr=soup.select('tbody tr ')

    #table=soup.find("table",{'movie_name':'movie_score'})
    new_table=[]
    for row in tbody_tr:
        name=""
        score=int
        review=""
        name=row.find('a').text
        score=int(row.find('em').text)
        tr_data = row.find("td", {"class", "title"})
        tr_data.find("a").extract()
        tr_data.find("a").extract()
        tr_data.find("div").extract()
        tr_data.find("br").extract()
        review=tr_data.text.strip()
        print(name,score,review)

        conn = sqlite3.connect("db.movie_review") 
        cur = conn.cursor()
        query='INSERT INTO movie_review_modify(name, score, review) VALUES(?,?,?)'
        conn.execute(query,(name,score,review)) 

        conn.commit() 
        conn.close()


