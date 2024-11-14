

# RECON

## Finding SUBS and Directories

### subfinder
	-subfinder -d domain -rl ratelimit
	
	-passive subdomain enumeration 

	-gau 
		echo "domain" | gau
	-waymore -i domain
	```
	-curl -s https://jldc.me/anubis/subdomains/ in/file-splitter-3:item | jq '.[]' | sed 's///g' | sort -n | uniq | tee out/jldc-subdomains-1/item/output.txt
	```
### GoogleDorks
	-DOMAIN ext:txt | ext:pdf | ext:xml | ext:xls | ext:xlsx | ext:ppt | ext:pptx | ext:doc | ext:docx
	

	-intext:“confidential” | intext:“Not for Public Release” | intext:”internal use only” | intext:“do not distribute”

### dirb 
	-dirb http(s)://www.TARGET.com
	
	-checks for different directories using wordlist showing CODEs

### ffuf
	```
	-ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt  -u Domain/FUZZ -fs 1926
	```
	.querrieys everithing
### http probe
	```
	 cat domains.txt | httprobe -t 20000(timeout)
	```
### eyewitness for pictures
### amass
	-amass enum -d http://TARGET.com   
	-brute force (dc)
## js analyze
	-jswzl to analyze js 
	-linkfinder
# Sql Injection
	-sqlmap
# IDOR
	-autorize 2 diff acc
# Crawl katana
	katana -u target.com -d 5 -ps -pss waybackarchive,commoncrawl,alienvault -f qurl -jc -xhr -kf -fx -fs dn -ef woff,css,png,svg,jpg,woff2,jpeg,gif,svg	
# Browser Extensions
	-foxyproxy
	-Hack-Tools
	-Wappalyzer
	-Xln Reveal
	-Trufflehog
	-Firefoy Multi Account Containers
