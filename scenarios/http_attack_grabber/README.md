#Grabber
Information obtained from: [Kali Tool page](https://tools.kali.org/web-applications/grabber)

Grabber is a web application scanner. Basically it detects some kind of vulnerabilities in your website. Grabber is simple, not fast but portable and really adaptable. This software is designed to scan small websites such as personals, forums etc. absolutely not big application: it would take too long time and flood your network.

Features:

- Cross-Site Scripting
- SQL Injection (there is also a special Blind SQL Injection module)
- File Inclusion
- Backup files check
- Simple AJAX check (parse every JavaScript and get the URL and try to get the parameters)
- Hybrid analysis/Crystal ball testing for PHP application using PHP-SAT
- JavaScript source code analyzer: Evaluation of the quality/correctness of the JavaScript with JavaScript Lint
- Generation of a file [session_id, time(t)] for next stats analysis.

Source: http://rgaucher.info/beta/grabber/

- Author: Romain Gaucher
- License: BSD

```
root@kali:~# grabber -h
Usage: grabber [options]

Options:
  -h, --help            show this help message and exit
  -u ARCHIVES_URL, --url=ARCHIVES_URL
                        Adress to investigate
  -s, --sql             Look for the SQL Injection
  -x, --xss             Perform XSS attacks
  -b, --bsql            Look for blind SQL Injection
  -z, --backup          Look for backup files
  -d SPIDER, --spider=SPIDER
                        Look for every files
  -i, --include         Perform File Insertion attacks
  -j, --javascript      Test the javascript code ?
  -c, --crystal         Simple crystal ball test.
  -e, --session         Session evaluations
```

Spider the web application to a depth of 1 (–spider 1) and attempt SQL (–sql) and XSS (–xss) attacks at the given URL (–url http://192.168.1.224):

```
root@kali:~# grabber --spider 1 --sql --xss --url http://192.168.1.224
Start scanning... http://192.168.1.224
runSpiderScan @  http://192.168.1.224  |   # 1
Start investigation...
Method = GET  http://192.168.1.224
[Cookie]    0   :   <Cookie PHPSESSID=2742cljd8u6aclfktf1sh284u7 for 192.168.1.224/>
[Cookie]    1   :   <Cookie security=high for 192.168.1.224/>
Method = GET  http://192.168.1.224
[Cookie]    0   :   <Cookie PHPSESSID=2742cljd8u6aclfktf1sh284u7 for 192.168.1.224/>
[Cookie]    1   :   <Cookie security=high for 192.168.1.224/>
```