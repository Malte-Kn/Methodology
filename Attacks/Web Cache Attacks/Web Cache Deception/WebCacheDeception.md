# Summary
1. Identify possible sensitive Informaiton stored in the Web Cache
2. Find Requests that are Cached to understand the caching rules
3. Try to find different ways to store the sensitive Informaiton from 1. in the Cache

## ID target Information
```
 Sensitive Information that is generated dynamicly needs to be fetsch from the server
 e.g.  /user/{UserID}/profileInfo/
```
## ID Cache rules
### Cached Responses
```
Find different requestes that might be cached
Watch response-times cached responses are faster
Look at response Headders such as:
X-Cache hit //From cache
X-Cache miss //From server
X-Cache dynamic //should not by cached
X-Cache refresh //used to be cached but needed to be refreshed
Cache-Control  public, max-age=2419200 //might indicate Cache --> further testing response time
```
### Test Cache Rules
```
Check for different extensions: .js .css .ico .exe other seen in previos step
Check for different delimiters
```
### Path mapping exploit
```
No Change in respose if Ptach is Changed
/user/{UserID}/profileInfo/
/user/{UserID}/profileInfo/asd
/user/{UserID}/profileInfo/asd.js
/user/{UserID}/profileInfo/asd.css
```
### Delimiters
```
Find Delimiters that are used by the origen server not the cache
/profileInfo;asd.js
/profileInfo.css
/profileInfo%00asd.js
```
### Different encodings
```
/profileInfo%23asd.js 
Orinin server migh encode to /profileInfo#asd.js and serve info
Cache might not decode and interprets /profileInfo%23asd.js  
```
### Cache based on Path normalization
```
Some Caches use specific Path for Cache rules e.g.
/static
/assets
/scripts
/resources
Try Path Treversal to trick Cache make sure the extension is not the trigger for Caching(remove all else)
/assets/..%2fprofileInfo  // Check if Origin Server servers /profileInfo
/assets/..%2fprofileInfo/asd.css
Check Cache respose to Path Trevs choose already Cached Respose
/aaa/..%2fassets/js/stockCheck.js
If still read from Cache Path is normalized 
If it does not Chache there might be a rule based on the /assets Path 
Check after Needed Path
assets/..%2fjs/stockCheck.js
If Read from Cache the Cache normalizises the Url 
If Cached there migh be potetial for Web Cache deception
```
#### Exploit Path normalization
```
1.Origin Server normalizes Path Cache does not:
<static-CahceRule-Path>/..%2f<targetPath>
/assets/..%2fprofileInfo
2.Cache normalizes Path Origin Server does not:
<targetPath>%2f%2e%2e%2f<static-CacheRule-Path>
/profileInfo%2f%2e%2e/assets
If origin server returns error not Info we need a delimiter useed by the origin server not the Cache e.g.
/profileInfo;%2f%2e%2e/assets
```
## Filename Cache Rules
```
Some files such as robots.txt, index.html, favicon.ico might be cached
That can be exploited in similar fasion as the Path with different normalizations
/asd%2f%2e%2e%2frobots.txt
/profile;%2f%2e%2e%2f/favicon,ico
Cache server needs to resolve the PathTrev the Origen needs not to
```
