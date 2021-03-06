#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Faraday Penetration Test IDE
Copyright (C) 2013  Infobyte LLC (http://www.infobytesec.com/)
See the file 'doc/LICENSE' for the license information
'''

import sys,StringIO, urllib, urllib2, cgi, re, socket
from urlparse import urlparse
from plugins import core

class google_Hosts(core.PluginBase):

	def __init__(self):
        	core.PluginBase.__init__(self)
        	self.id = "Google"
        	self.name = "Google Plugin"
        	self.plugin_version = "0.0.1"
        	self.version = "2.1.1"
        	self.host = "google.com"
	
        def parseOutputString(self, output, debug = False):
		url = 'https://www.google.com/xhtml?'		
		q = 'site:'+self.host
		start=0
		num=100
		gws_rd = 'ssl'
		query_string = { 'q':q, 'start':start, 'num':num, 'gws_rd':gws_rd }
		data = urllib.urlencode(query_string)
		url = url + data
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)', 'Referer' : 'http://127.0.0.1/'} # $
		try:
                	req = urllib2.Request(url, None, headers)
                	google_reply = urllib2.urlopen(req).read()
                	regex = '<h3 class="r"><a href="/url(.+?)">'
                	pattern = re.compile(regex)
                	url_links = re.findall(pattern, google_reply)
        	except urllib2.URLError:
                	pass

		hosts=[]
		ips=[]
		for url in url_links:
			url2=url.strip('?q=')
			try:
				d=urlparse(url2)
				if d.netloc not in hosts:

		         		ip = socket.gethostbyname(d.netloc)
            	         		puerto = 80 
			 		host_id = self.createAndAddHost(ip)
			 		iface_id = self.createAndAddInterface(host_id, ip, ipv4_address = ip)
			 		serv_id  = self.createAndAddServiceToInterface(host_id, iface_id, "http", protocol = "http", ports = puerto, status= null)
			 		self.createAndAddNoteToService(host_id, serv_id, 'Host List', d.netloc)
						
                	except socket.error:
                        	pass
			

def createPlugin():
	return google_Hosts() 

