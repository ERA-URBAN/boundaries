# download_weather_boundaries
Needs an ECMWF web user ID.
Register at: https://www.ecmwf.int/registration/?back=http://www.ecmwf.int/user/login/sso

Personal api key should be added to $HOME/.ecmwfapirc. Once you are logged in with your persional ECMWF web user ID, get your personal key from https://api.ecmwf.int/v1/key/

Content of $HOME/.ecmwfapirc 	

{
    "url"   : "https://api.ecmwf.int/v1",
    "key"   : "xxxxxxxxxxxxxxxxxxxxxxxx",
    "email" : "xxx@xxx.com"
}

### Installation
```
pip install git+https://github.com/ERA-URBAN/boundaries
```

### Dependencies
```
pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz
```

### Usage
usage: download_interim [-h] [--pl PL] [--sfc SFC] [--date2 DATE2]
                  [--datadir DATADIR] --date DATE

Download ERA-Interim fields (pl and sfc) to be used as WRF boundaries.

optional arguments:
  -h, --help         show this help message and exit
  --pl PL            download pressure level fields [boolean, default: true]
  --sfc SFC          download surface level fields [boolean, default: true]
  --date2 DATE2      Optional second date YYYY-MM-DD. Data will be downloaded
                     between --data and --data2 in used.
  --datadir DATADIR  destination directory [default:
                     /data/github/ERA_URBAN/scripts/boundaries/ERAI]

required arguments:
  --date DATE        Date YYYY-MM-DD
################################################################################
