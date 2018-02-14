# Github Trends

Application for getting of most Trending Repositories.
By default it printing 20 most Trending Repositories, created in less a week.
You can change period and quantity of interesting repositories:
 - use optional parameter **-q** for change quantity
 - use optional parameter **-d** for change period
 
Application is printing a list of most Trending Repositories:
 - URL
 - Creating date
 - Stars quantity
 - Opened issue quantity
 
# Quickstart
Run with command line:
 ```
$ python github_trending.py -d 5 -q 5
HTML URL of the Trending Repository                             Was created     Stars   Opened issues
https://github.com/vektah/gqlgen                                2018-02-11        588               2
https://github.com/truedread/netflix-1080p                      2018-02-11        391               0
https://github.com/raphael-ernaelsten/Aura                      2018-02-12        340               6
https://github.com/Eplox/TCP-Starvation                         2018-02-12        277               3
https://github.com/mitchellh/go-server-timing                   2018-02-12        233               1
```
or get help:
```
$ python github_trending.py -h
usage: github_trending.py [-h] [-q QUANTITY] [-d DAYS]

GitHub Trending

optional arguments:
  -h, --help            show this help message and exit
  -q QUANTITY, --quantity QUANTITY
                        How much repositories to displayUsing 20 by default
  -d DAYS, --days DAYS  How long ago repositories were createdUsing 7 days by
                        default
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
