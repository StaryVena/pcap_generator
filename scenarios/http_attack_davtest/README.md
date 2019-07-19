# DAVTest
Information obtained from: [Kali Tool page](https://tools.kali.org/web-applications/davtest)

DAVTest tests WebDAV enabled servers by uploading test executable files, and then (optionally) uploading files which allow for command execution or other actions directly on the target. It is meant for penetration testers to quickly and easily determine if enabled DAV services are exploitable.

DAVTest supports:
- Automatically send exploit files
- Automatic randomization of directory to help hide files
- Send text files and try MOVE to executable name
- Basic and Digest authorization
- Automatic clean-up of uploaded files
- Send an arbitrary file

Source: https://code.google.com/p/davtest/

- Author: Sunera, LLC.
- License: GPLv3

```
root@kali:~# davtest

ERROR: Missing -url

/usr/bin/davtest -url <url> [options]

 -auth+     Authorization (user:password)
 -cleanup   delete everything uploaded when done
 -directory+    postfix portion of directory to create
 -debug+    DAV debug level 1-3 (2 & 3 log req/resp to
            /tmp/perldav_debug.txt)
 -move      PUT text files then MOVE to executable
 -nocreate  don't create a directory
 -quiet     only print out summary
 -rand+     use this instead of a random string for filenames
 -sendbd+   send backdoors:
            auto - for any succeeded test
            ext - extension matching file name(s) in 
                  backdoors/ dir
 -uploadfile+   upload this file (requires -uploadloc)
 -uploadloc+    upload file to this location/name 
                (requires -uploadfile)
 -url+      url of DAV location

Example: /usr/bin/davtest -url http://localhost/davdir
```

Scan the given WebDAV server (-url http://192.168.1.209):

```
root@kali:~# davtest -url http://192.168.1.209
********************************************************
 Testing DAV connection
OPEN        SUCCEED:        http://192.168.1.209
********************************************************
NOTE    Random string for this session: B0yG9nhdFS8gox
********************************************************
 Creating directory
MKCOL SUCCEED: Created http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox
********************************************************
 Sending test files
PUT asp FAIL
PUT cgi FAIL
PUT txt SUCCEED:    http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
                    davtest_B0yG9nhdFS8gox.txt
PUT pl  SUCCEED:    http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
                    davtest_B0yG9nhdFS8gox.pl
PUT jsp SUCCEED:    http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
                    davtest_B0yG9nhdFS8gox.jsp
PUT cfm SUCCEED:    http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
                    davtest_B0yG9nhdFS8gox.cfm
PUT aspx    FAIL
PUT jhtml   SUCCEED:    http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
                        davtest_B0yG9nhdFS8gox.jhtml
PUT php SUCCEED:    http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
                    davtest_B0yG9nhdFS8gox.php
PUT html    SUCCEED:    http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
                        davtest_B0yG9nhdFS8gox.html
PUT shtml   FAIL
********************************************************
 Checking for test file execution
EXEC    txt SUCCEED:    http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
                        davtest_B0yG9nhdFS8gox.txt
EXEC    pl  FAIL
EXEC    jsp FAIL
EXEC    cfm FAIL
EXEC    jhtml   FAIL
EXEC    php FAIL
EXEC    html    SUCCEED:    http://192.168.1.209/DavTestDir_
                            B0yG9nhdFS8gox/davtest_B0yG9nhdFS8gox.html

********************************************************
/usr/bin/davtest Summary:
Created: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox
PUT File: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
          davtest_B0yG9nhdFS8gox.txt
PUT File: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
          davtest_B0yG9nhdFS8gox.pl
PUT File: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
          davtest_B0yG9nhdFS8gox.jsp
PUT File: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
          davtest_B0yG9nhdFS8gox.cfm
PUT File: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
          davtest_B0yG9nhdFS8gox.jhtml
PUT File: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
          davtest_B0yG9nhdFS8gox.php
PUT File: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
          davtest_B0yG9nhdFS8gox.html
Executes: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
          davtest_B0yG9nhdFS8gox.txt
Executes: http://192.168.1.209/DavTestDir_B0yG9nhdFS8gox/
          davtest_B0yG9nhdFS8gox.html
```