ssilk = open('redirect.html', 'w')
ssilk = open('redirect.html', 'a')

ssilki = input('Enter link:')

text = r'''<body><form id="firefox" action='''+ssilki+''' method="post" >
<input name="login" type="hidden"><script type="text/javascript">document.forms["firefox"].submit();</script>'''

ssilk.write(text)
input()