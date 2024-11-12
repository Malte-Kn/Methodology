# AWS S3 Attacks
## More Info
```
https://rafa.hashnode.dev/exploiting-http-parsers-inconsistencies
```
## Via Host Header
```
AWS will ignore the requests Domain e.g.your.s3.amazonaws.com and uses the HostHeader my.s3.amazonaws.com

1. Only first Host Header counts rest ignored
2. These bytes are ignored \x1f, \x1d, \x0c, \x1e, \x1c, \x0b;

If cache includes the ignore bytes as part of header name treating it as invalid while S3 interprets it as valid host header

GET / HTTP/1.1
[\x1d]Host: evilbucket.com
Host: example.bucket.com
Connection: close


Cache will ignore wrong Header [\x1d]Host: evilbucket.com and chooses example.bucket.com as valid


When reachign the S3 bucket the header [\x1d]Host: evilbucket.com will be interpreted as valid and the other host headers are ignored

The final result is a complete cache poisoning of the page with arbitrary content.
```
