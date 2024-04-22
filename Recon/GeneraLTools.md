

#RECON

##Finding SUBS and Directories

###subfinder
	-subfinder -d domain -rl ratelimit
	
	-passive subdomain enumeration 
###dirb 
	-dirb http(s)://www.domain.com
	
	-checks for different directories using wordlist showing CODEs

### ffuf
	-ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt  -u Domain/FUZZ -fs 1926

	.querrieys everithing
###http probr
	-▶ cat domains.txt | httprobe -t 20000(timeout)
###eyewitness for pictures
### amass
	-amass enum -d http://trip.com   
	-brute force (dc)
## js analyze
	-jswzl to analyze js 
	-linkfinder
#Sql Injection
	-sqlmap
#IDOR
	-autorize 2 diff acc
#	
	
