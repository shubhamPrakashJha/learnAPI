# USE API
shows you how to use api in real time

## INSTALL DEPENDENCIES
1. open cmd in administration mode
2. open script folder in python directory
3. copy script dir address in cmd
```angular2html
        cd C:\Python36\Scripts
```
4. You need to install HTTP library.
```angular2html
        pip install requests
```
5. In your Python code you need to import requests module

 >       import requests
 
 >       response = requests.get("http://api.open-notify.org/iss-now.json")
 >       print(response.status_code)

## STATUS CODES

> `200` – everything went okay, and the result has been returned (if any)

> `301` – the server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.

> `401` – the server thinks you’re not authenticated. This happens when you don’t send the right credentials to access an API (we’ll talk about authentication in a later post).

> `400` – the server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.

> `403` – the resource you’re trying to access is forbidden – you don’t have the right permissions to see it.

> `404` – the resource you tried to access wasn’t found on the server.