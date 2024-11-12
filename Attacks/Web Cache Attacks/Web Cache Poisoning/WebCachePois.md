# Summary
Introduce malicouse attack in respose of Cached site e.g.stored xss

## Find Cached Responses
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
## Find reflected Info
```
The Info cant be used as a key for the Cachig rule:
If the Info changes it is Cached different or not Cached at all
```
### Host Header
```
Find header with Param minre Reques->Extension->Param Miner-> Guess Header; Results in Extensions/Installed/Console
Host Header might be used to call other resources and could be injectable
Use Different Host Headers in list
Observe Caching changes and possible injection
```
### Cookies
```
Some Cookies are used in dynamic responses e.g. language=eng
If Cookies are reflected and not keyed try injection and check caching
```
### Different Header
```
Check for different Headers:
Find header with Param minre Reques->Extension->Param Miner-> Guess Header; Results in Extensions/Installed/Console
Check if the Headers are keyed (differently Cached)
Try to use Headers like x-forwarded-scheme, x-forwarded-proto, x-forwarded-host
For examlpe force redirects
```
### Parameter
#### Parameter cloaking
```
If excluded Parameter is found it might be able to be used for smuggiling a payload:
Find a delimiter e.g. ?
/?injectinoPara=asd?excludedParam=Payload
Cache might exclude the second Parameter while the server includes it
```
#### Parameter parsing
```
If an unkeyed Parameter is found it can be used with an excluded parameter in some cases e.g. Ruby rails to overwrite the keyed parameter:
/?keyedParam=asd&excludedParam=test;keyedParam=PAYLOAD 
```
