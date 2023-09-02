import csv
a = open("test.csv",mode="r",encoding="utf-8")
html = ["<!DOCTYPE html>", "<head>","<title>Test</title>","</head>","<body>"]

rows = []
head = []
a = csv.reader(a) 
head = next(a)
for row in a :
    rows.append(row)
#print(head)


for i in range(len(rows)) :
    html.append("<div>")
    for col,items in enumerate(rows[i]) :
        if col == 0 :
            html.append('<p class = "time">' +  head[col] + ': ' +"</p>")
            html.append('<p class = "info">'+items+'</p>')
        else :
            html.append('<p class = "tags">' + head[col] + ': '+"</p>")
            html.append('<p class = "info">'+items+'</p>')
    html.append("</div>")
html.append("</body>")
b = open("test.html",mode="w",encoding="utf-8")
for thing in html :
    b.write(thing+'\n')
b.close()