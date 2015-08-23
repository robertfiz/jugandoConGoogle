import sys,StringIO, urllib, urllib2, cgi, re, socket
from urlparse import urlparse

if len(sys.argv) != 2:
	print "Debe pasarle un argumento"
	print "Ejemplo de uso: python hosts-google.py ejemplo.com"
	exit(1)
else:
	url = 'https://www.google.com/xhtml?'		
	q = 'site:'+str(sys.argv[1])
	start=0
	num=100
	gws_rd = 'ssl'
	query_string = { 'q':q, 'start':start, 'num':num, 'gws_rd':gws_rd }
	data = urllib.urlencode(query_string)
	url = url + data
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)', 'Referer' : 'http://127.0.0.1/'} # $
	req = urllib2.Request(url, None, headers)
	google_reply = urllib2.urlopen(req).read()
	regex = '<h3 class="r"><a href="/url(.+?)">' # search urls on google's $
	pattern = re.compile(regex)
	url_links = re.findall(pattern, google_reply)
	hosts=[]
	ips=[]
	for url in url_links:
		url2=url.strip('?q=')
		try:
			d=urlparse(url2)
			if d.netloc not in hosts:
				hosts.append(d.netloc)	
                except socket.error:
                        pass


	archi=open("host-google","a")
	for host in hosts:
		try:
			aux=host.strip('http://');
			print host+" "+socket.gethostbyname(aux)
			archi.write(host+" "+socket.gethostbyname(aux)+"\n")
		except socket.error:
			pass
	archi.close()
