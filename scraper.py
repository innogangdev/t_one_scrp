import scraperwiki
import lxml.html
html = scraperwiki.scrape("http://www.filmibeat.com/tamil/news/")
root = lxml.html.fromstring(html)
node=root.cssselect("div.collection")
scraperwiki.sqlite.execute("delete from data");
c=0
for i in node:
    c=c+1
    #print lxml.html.tostring(i)
    root1=lxml.html.fromstring(lxml.html.tostring(i))
    node1=root1.cssselect("a");
    node2=root1.cssselect("a img");
    node3=root1.cssselect("h2 a");
    node4=root1.cssselect("div.coll-article-desc");
    if len(node1)>=1 :
        data={
            'index':c,
            'title':node3[0].text,
            'site':"http://www.filmibeat.com/" + node1[0].attrib['href'],
            'image':node2[0].attrib['src'],
            'source':"OneIndia",
            'detail':node4[0].text,
            'sourceSiteType':'IMAGE',
            'sourceUrl':'http://entertainment.oneindia.in',
            'sourceLogo':'http://entertainment.oneindia.in/img/oneindia-entertainment.jpg'
        }
        scraperwiki.sqlite.save(unique_keys=['index'], data=data)