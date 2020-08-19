import requests as req
import re

class Entry():
    """An entry from website called eksisozluk."""

    def __init__(self, number):
        # super(Entry, self).__init__():
        self.number = number
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.url = 'https://www.eksisozluk.com/entry/{}'.format(self.number)
        self.content = self.getPage()
        self.title = self.getTitle()
        self.date = self.getDate()
        self.author = self.getAuthor()
        self.entrytext = self.getEntry()


    def getPage(self):
            return req.get(self.url,allow_redirects=True,headers = self.headers).text
    def getEntry(self):
            self.patternentry = re.compile(r'<meta property="og:description" content=\"(.+?)\">', re.DOTALL)
            return re.findall(self.patternentry,self.content)
    def getAuthor(self):
            self.patternauthor = re.compile(r'<a class="entry-author" href="/biri/(.+?)\">')
            return re.findall(self.patternauthor,self.content)
    def getDate(self):
            self.patterndate = re.compile(r'<a class="entry-date permalink" href="/entry/(.+?)\">(.+?)</a>')
            return re.findall(self.patterndate,self.content)
    def getTitle(self):
        self.patterntitle = re.compile(r'<title>(.+?) -')
        return re.findall(self.patterntitle,self.content)
    def debug(self):
            print("""entry number:{}
            headers:{}
            url:{}
            content:{}\n... continues\n
            title:{}
            date:{}
            author:{}
            entry:{}""".format(self.number,
    self.headers,
    self.url,
    self.content[:234],
    self.title,
    self.date,
    self.author,
    self.entrytext))
