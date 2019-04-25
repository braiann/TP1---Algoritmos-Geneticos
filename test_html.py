import webbrowser

f = open('test.html', 'w')

mensaje = """<html>
<head></head>
<body><p>HOla</p></body>
</html>"""

f.write(mensaje)
f.close()

webbrowser.open_new_tab('test.html')