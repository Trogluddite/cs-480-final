# cs-480-final

run `./decrypt_demo.py` from a system with python3 in `/usr/bin/env`
(should work for macos & linux; didn't test Windows)

##'Decrypt' class:
* `getText()` will by default read text from 'secret.txt'; this can be overridden w/ a keyword arg
* `getKey()` will by default set the key to 13; this can be overridden w/ a keyword arg
* `decipherMessage()` will decrypt and write to final.txt -- optionally, it can also print to the terminal


I've included a sample secret.txt and a terminal snippet of this running
