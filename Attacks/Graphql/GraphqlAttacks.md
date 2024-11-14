# Basic Graphql Recon and exploitation

## Get Information about the Graphql setup via Introspection:
	Burp has special Graphql tab and helps to send the Introspection to gain Info about the Grphql Setup

## WORKFLOW in Burp:
1. In repeater > Graphql > Set introspection query(Set legacy intro quesry for older servers)  --> Get Info about schema
2.In response rightclick > Grphql > Save GraphQL queries to site map look at sitemap

## Find Graphql Endpoints:
	query{__typename}

Discovering schema info:
```
	query{__schema}
	-Introspection probe request
	{
		"query":"{__schema{queryType{name}}}"
	}
```
	Run full Interospection query
## Grphql uses similar Path/endmpoits such as apis:
	```
	/graphql/graphql
	/api
	/api/graphql
	/graphql/api
	/v1
	/v1/api/graphql
	/v1/graphql/api
	/v1/graphql/graphql
	```
## Introspection not working:
	Url encode different disallowed values
	add line breaks(%0A) or null bytes etc
  Use different request Methods 
	Most Graphql only allow POST with application/json
	some allow x-www-form-urlencoded or GET
  Get url encoded graphql query
	use get request on endpoit >> set query = query{__typename} >> set Introspection in Burp



## Test lika API with OWASP 10 such as IDOR
	If objects are directly accessed check for IDORs

##Tools
Clairvoyance:
	Uses suggestions to recover correct queries:
	ProductInfo -->  "ProductInfo" does not exists do you mean "ProductInformation"? 
