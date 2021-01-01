# HTOTW
Hunt Target On The Web

## Install
```
git clone https://github.com/Neotoxic-off/HTOTW
cd HTOTW
pip3 install -r requirements.txt
```

## Usage
```
usage: HTOTW.py [-h] -u USERNAME [-a] [-s]

All commands availables

optional arguments:
  -h, --help            show this help message and exit
  -a, --adult           Check the adult hosts
  -s, --status          Check hosts status

Required settings:
  -u USERNAME, --username USERNAME
                        Username to hunt


```

## Examples
```
python3 HTOTW.py -u username
```
```
python3 HTOTW.py -u username -s
```
```
python3 HTOTW.py -u username -a
```
```
python3 HTOTW.py -u username -a -s
```

## Modules modification

- The name of the module file is important !
- `"method" : "GET"` modify the method type to grab the informations
- `"name" : "<HOST>"` enter the name of the website example: `google`
- `"origin" : "<HOST>"` enter the url of the main / home page
it will be used to check if the website is down
- `"timeout" : 5,` after this amount of time in sec, the link will be considered
as a timeout
- `"url" : ["<HOST URL>"]` enter the urls of the website, it must be an array !
example: `https://google.com`
The url must include '{}' the place where will be placed the username
- `"method" : "status_code"` status_code error type will check the status code of the page
- `"method" : "text"` text error will check result content (**in progress**)
- `"message" : "None"` the message will try to be grabbed in the result content in data mod only
- `header` the header is the headers content to send during the request
- `"adult" : false` if you consider that's an adult website set as true else false
if you don't use the `-a` the adult website won't be tested

```
"google" : {
  "method" : "GET",
    "name" : "google",
    "origin" : "https://www.google.com/",
    "timeout" : 5,
    "url" : [
      "https://google.com/{}"
    ],
    "error" : {
        "method" : "status_code",
        "status_code" : {
            "ok" : "ok"
        },
        "message" : "None"
    },
    "header" : {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
    },
    "adult" : false
}
```