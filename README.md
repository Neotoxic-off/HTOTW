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
usage: HTOTW.py [-h] -u USERNAME [-a] [-o OUTPUT]

All commands availables

optional arguments:
  -h, --help            show this help message and exit
  -a, --adult           Check the adult hosts

Required settings:
  -u USERNAME, --username USERNAME
                        Username to hunt

```

## Examples
```
python3 HTOTW.py -u username
```
```
python3 HTOTW.py -u username -a
```

## Modules modification

- The name of the module file is important !
- `"method" : "GET"` modify the method type to grab the informations
- `"name" : "<HOST>"` enter the name of the website example: `google`
- `"url" : "<HOST URL>"` enter the url of the website example: `https://google.com`
- `"method" : "code"` code error type will check the status code of the page
- `"method" : "data"` data error will check result content (**in progress**)
- `"message" : "None"` the message will try to be grabbed in the result content in data mod only
- `header` the header is the headers content to send during the request
- `"adult" : false` if you consider that's an adult website set as true else false
if you don't use the `-a` the adult website won't be tested

```
{
  "method" : "GET",
    "name" : "google",
    "url" : "https://google.com/{}",
    "error" : {
        "method" : "code",
        "code" : {
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