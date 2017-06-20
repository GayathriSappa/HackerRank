from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("-> %s > %s" % (attr[0], attr[1]))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("-> %s > %s" % (attr[0], attr[1]))

html = ""
N = int(input())
for _ in range(N):
    html += input().rstrip()
    html + '\n' 

parser = MyHTMLParser()
parser.feed(html)
