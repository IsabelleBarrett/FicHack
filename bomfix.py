fp = open("urls.csv")
s = fp.read()
u = s.decode("utf-8-sig")

result = u.encode("utf-8")


newFile = open("urlsFixed.csv", "w")
newFile.write(result)