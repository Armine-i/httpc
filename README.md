github link: https://github.com/Armine-i/httpc
# httpc
**Steps before using the command line tool:**

$ source v2/bin/activate

$ pip install --editable .

**Examples:**
- GET command:

"httpc get -v http://httpbin.org/status/418"

![ScreenShot](https://raw.github.com/Armine-i/httpc/master/getexample.png)

- POST command:

"httpc post -h Content-Type:application/json  --d "Assignment":1 http://httpbin.org/post"

![ScreenShot](https://raw.github.com/Armine-i/httpc/master/postexample.png)
