#SMB Attack

Pleas read the SMB Normal chapter first. The SMB Attack client has the same operations as the SMB Client,
but with different settings.

There are three types of operation settings.

- usual - see the SMB Normal chapter for more information.
```
python crawler_client.py -t usual -n 60 -s shares
```


- attacker - behaves as usual clients but also tries to download non existent files defined in 
`src/smb/client/secret_files.txt`.
```
python crawler_client.py -t attacker -n 60 -s shares
```
- attacker2  - tries to connect to server with usernames and passwords defined in `src/smb/client/users.txt` 
and `src/smb/client/passwords.txt`. 

```
python crawler_client.py -t attacker2 -n 60 -s shares
```
