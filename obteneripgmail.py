import dns.resolver
import re

patron3= re.compile('\d+.\d+.\d+.\d+/\d+')
patron2 = re.compile ('\d?\S?\d?\S?\d?:\d?\S?\d?\S?\d?:\d?\S?\d?\S?\d?::/\d?\S?\d?\S?\d?')
patron = re.compile('_\S*\d?.google.com')
answers = dns.resolver.query('_spf.google.com', 'TXT')
for raw in answers:		
	
	lhosts=patron.findall(str(raw))
for host in lhosts:
	ips=dns.resolver.query(host, 'TXT')
	for ip in ips:
		ipraw=patron3.findall(str(ip))
		ipraw6=patron2.findall(str(ip))
		for ipr6 in ipraw6:
			print ipr6
		for ipr4 in ipraw:
			print ipr4
