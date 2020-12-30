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
usage: HTOTW.py [-h] -u USERNAME [-a]

All commands availables

optional arguments:
  -h, --help            show this help message and exit
  -a, --adult           Check the adult hosts

Required settings:
  -u USERNAME, --username USERNAME
                        Username to hunt
```

## Example
```
python3 HTOTW.py -u username
```

```go
888  888 888888888 88888888 888888888 8d8   d88
88888888    '88d   888  888    '88d   888,o.d88
88P  888   '888    888  888   '888    888P`Y8b8
88P  888 '88p      888oo888 '88p      88P   YP8

Hunt Target On The Web 0.1.0

loading settings...
loading hosts...
Starting the hunt...

[1/5] ✗ twitch
[2/5] ✓ github
[3/5] ✓ youtube
[4/5] ✓ instagram
[5/5] ✗ twitter

```

## Modules modification

- The name of the module file is important !
- `"method" : "GET"` modify the method type to grab the informations
- `"url" : "<HOST URL>"` enter the url of the website example: `https://google.com`
- `"method" : "code"` code error type will check the status code of the page
- `"method" : "data"` data error will check result content (**in progress**)
- `"message" : "None"` the message will try to be grabbed in the result content in data mod only
- `header` the header is the headers content to send during the request
- `"adult" : 0` if you consider that's an adult website put a 1 else put a 0
if you don't use the `-a` the adult website won't be displayed

```
{
    "method" : "GET",
    "url" : "<HOST URL>",
    "error" : {
        "method" : "code",
        "message" : "None"
    },
    "header" : {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
    },
    "adult" : 0
}
```