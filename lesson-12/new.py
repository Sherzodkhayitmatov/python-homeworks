from bs4 import BeautifulSoup 

html_doc = """
<html>
<head>
<title>Test Page</title>
</head>
<body>
<p>This is a paragraph</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())