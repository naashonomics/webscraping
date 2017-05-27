import bs4 as bs
import urllib.request

#insider buys http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=1&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1 
url = input('Enter the url')

sauce = urllib.request.urlopen(url).read()

soup = bs.BeautifulSoup(sauce,'lxml')

temp = soup.select('table tbody tr td')

temp2=[]
for temp1 in temp:
	t=temp1.get_text().split()
	for t1 in t:
		print(t1)
		
