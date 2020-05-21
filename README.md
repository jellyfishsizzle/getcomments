## Find comments in web pages

While participating in CTFs it's a common occurrence to come across pages that have comments buried in the HTML.  Nothing is perfect (including this spaghetti code), but I wanted something that would at least do some of the heavy lifting.  

It's not another dirburster, it won't do the scanning for you.  I don't think there's a need to reinvent the wheel, but it's good to have another pair of "eyes" searching for sometimes elusive comments.  Besides, more enumeration is always better.

The script just requires the output of gobuster or ffuf (other cli scanners may also work). It will just output the comments themselves with out the `<!--`

### Usage:
```
# cat ffuf.out
# ffuf -c -e ".html,.php,.txt,/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.138.175/FUZZ -t 75

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.0.2
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.138.175/FUZZ
 :: Extensions       : .html .php .txt /
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 75
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

images/                 [Status: 200, Size: 31, Words: 2, Lines: 2]
index.php               [Status: 200, Size: 9280, Words: 441, Lines: 243]
cgi-bin/                [Status: 403, Size: 210, Words: 15, Lines: 9]
media                   [Status: 301, Size: 235, Words: 14, Lines: 8]
templates/              [Status: 200, Size: 31, Words: 2, Lines: 2]
media/                  [Status: 200, Size: 31, Words: 2, Lines: 2]
icons/                  [Status: 200, Size: 74409, Words: 7427, Lines: 1007]
modules/                [Status: 200, Size: 31, Words: 2, Lines: 2]
includes/               [Status: 200, Size: 31, Words: 2, Lines: 2]
language                [Status: 301, Size: 238, Words: 14, Lines: 8]
language/               [Status: 200, Size: 31, Words: 2, Lines: 2]
README.txt              [Status: 200, Size: 4494, Words: 481, Lines: 73]
components/             [Status: 200, Size: 31, Words: 2, Lines: 2]
cache                   [Status: 301, Size: 235, Words: 14, Lines: 8]
cache/                  [Status: 200, Size: 31, Words: 2, Lines: 2]
libraries               [Status: 301, Size: 239, Words: 14, Lines: 8]
libraries/              [Status: 200, Size: 31, Words: 2, Lines: 2]
robots.txt              [Status: 200, Size: 836, Words: 88, Lines: 33]
tmp/                    [Status: 200, Size: 31, Words: 2, Lines: 2]
tmp                     [Status: 301, Size: 233, Words: 14, Lines: 8]
LICENSE.txt             [Status: 200, Size: 18092, Words: 3133, Lines: 340]
administrator/          [Status: 200, Size: 4846, Words: 227, Lines: 110]
configuration.php       [Status: 200, Size: 0, Words: 1, Lines: 1]
something.php           [Status: 200, Size: 0, Words: 1, Lines: 1]
blah.php                [Status: 200, Size: 0, Words: 1, Lines: 1]
htaccess.txt            [Status: 200, Size: 3005, Words: 438, Lines: 81]
cli/                    [Status: 200, Size: 31, Words: 2, Lines: 2]
cli                     [Status: 301, Size: 233, Words: 14, Lines: 8]
.html                   [Status: 403, Size: 207, Words: 15, Lines: 9]
/                       [Status: 200, Size: 9264, Words: 441, Lines: 243]

:: Progress: [1102730/1102730] :: Job [1/1] :: 436 req/sec :: Duration: [0:42:06] :: Errors: 0 ::
```


```
# ./getcomments.py ffuf.out http://127.0.0.1

[+] http://127.0.0.1/blah.php
COMMENT 111
COMMENT 222

some tricky comment here

flag1(F4F9F1AA4975C248C3F0E008CBA09D6E9166)

[+] http://127.0.0.1/configuration.php
div class="count-particles" - Im a comment!

flag1 (52E33F0E008CBA09D6E9166)

[+] http://127.0.0.1/index.php
COMMENT 1
COMMENT 2

some comment here

flag3 (52E37291AEDF6A46D76)

[+] http://127.0.0.1/secret.txt
COMMENT in txt file?

[+] http://127.0.0.1/something.php
COMMENT 1
COMMENT 2

Another sneaky
multiline comment
that would be hard
to find

some comment here

```
