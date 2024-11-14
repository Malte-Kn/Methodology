# Find Parameters

## Tools
Populate Burp and use Paraminer

Use GAP to generate and finde different Parameters used copy into wordlist

## Wordlists
Combine specific Wordlist with seclist and arjuin list:
```
cat /usr/share/seclists/Discovery/Web-Content/Parameters.txt  params.txt > Comparams.txt 
```
Check for differetn params with arjun:
arjun -w Comparams.txt -u "https://www.TARGETDOMAIN.com/"
