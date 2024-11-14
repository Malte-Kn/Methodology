# FFUF in a request file (Burp Request)

```
ffuf -request req.txt -request-proto http  -w /usr/share/wordlists/seclists/Passwords/500-worst-passwords.txt:PASSFUZZ 
```
```
ffuf -request req.txt -request-proto http -mode clusterbomb -w email.txt:USERFUZZ -w pw.txt:PASSFUZZ -mc 200
```