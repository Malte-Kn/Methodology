# Javascript files from waybackurls

## Get all javascript files for the specific domain that ever existed
```
echo "domain" | waybackurls | grep -P ".*\.js" | wget
```
## Check all jsfiles for specific path such as /api/search/auth-token
```
grep -RoP "(\/[a-zA-Z0-9_\-]+)+"       
```
