Get Information about the Graphql setup via Introspection:
	Burp has special Graphql tab and helps to send the Introspection to gain Info about the Grphql Setup


In repeater > Graphql > Set introspection query(Set legacy intro quesry for older servers)  --> Get Info about schema
		In response rightclick > Grphql > Save GraphQL queries to site map

Find Graphql Endpoints:
	query{__typename}

Discovering schema info:
	query{__schema}
	#Introspection probe request
	{
		"query":"{__schema{queryType{name}}}"
	}

	Run full Interospection query
Grphql uses similar Path/endmpoits such as apis:
	/graphql
	/api
	/api/grphql
	...
Use different request Methods 
	Most Graphql only allow POST with application/json
	some allow x-www-form-urlencoded or GET

IDOR
	If objects are directly accessed check for IDORs

Tools
Clairvoyance:
	Uses suggestions to recover correct queries:
	ProductInfo -->  "ProductInfo" does not exists do you mean "ProductInformation"? 