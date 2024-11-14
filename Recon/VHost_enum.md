# Vhost Enumaration


## NMAP with specific NEW scripts
```
nmap --script http-vhosts -p 80,443 --script-args http-vhosts.domain=TARGET.site,http-vhosts.filelist=/opt/SecLists/Discovery/DNS/subdomains-top1million-5000.txt www.TARGET.site
```

## Fuzzing Gobuster
```
gobuster vhost -k --append-domain -u crapi.site -w /opt/SecLists/Discovery/DNS/subdomains-top1million-20000.txt
```												

## VHOST detection via Subject Alternative Name (SAN) certificates

```
openssl s_client -connect www.TARGET.site:443 2>&1 < /dev/null | openssl x509 -noout -text | grep -i dns
```

More Info
https://danaepp.com/uncovering-elusive-api-targets-via-vhost-discovery
