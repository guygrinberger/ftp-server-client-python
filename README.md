# FTP-Server-Client-Python
A very simple FTP server and client written in python and designed to work on your local machine or a remote server.

***
## **Prerequisites**

To use ftplib in your code you'll ned to install Pyftpdlib.
TO install via pip, simply run:
```
$ pip install pyftpdlib
```

***
## **Run**
To test the server, first run the server like so:
```
$ python ftp_server.py
```
Don't forget to change the host and directory in the code!

Next, create a simple text file and save it as 'testfile.txt'.
In the 'ftp_client.py' code, change the testfile location to yours and run:
```
$ python ftp_client.py
```
You should see in your server terminal that the test file has been uploaded:
```
[I 2018-11-08 14:52:04] 127.0.0.1:54362-[anonymous] USER 'anonymous' logged in.
[I 2018-11-08 14:52:04] 127.0.0.1:54362-[anonymous] CWD /home/user 250
[I 2018-11-08 14:52:04] 127.0.0.1:54362-[anonymous] STOR /home/user/testfile.txt completed=1 bytes=9 seconds=0.0
[I 2018-11-08 14:52:04] 127.0.0.1:54362-[anonymous] FTP session closed (disconnect).
```

Then to complete the test, delete the testfile.txt, comment the upload function and uncomment the download function as such:
```
#uploadFile()
downloadFile()
```
and run 'ftp_client.py' again. you should see that the testfile.txt has been downloaded and in the server terminal:
```
[I 2018-11-08 14:52:33] 127.0.0.1:54386-[anonymous] USER 'anonymous' logged in.
[I 2018-11-08 14:52:33] 127.0.0.1:54386-[anonymous] CWD /home/user 250
[I 2018-11-08 14:52:33] 127.0.0.1:54386-[anonymous] RETR /home/user/testfile.txt completed=1 bytes=9 seconds=0.0
[I 2018-11-08 14:52:33] 127.0.0.1:54386-[anonymous] FTP session closed (disconnect).
```

