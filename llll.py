import re

s1 = "wioandonaw1326651asd0127dawd13256510127   f3ff132asd66510127..wd"

res = re.findall("13266510127",s1)

print(res)


res = re.findall(r"\d",s1)

print(res)

res = re.findall(r"\D",s1)

print(res)

res = re.findall(r"\w",s1)

print(res)

res = re.findall(r"\W",s1)

print(res)

res = re.findall(r"\s",s1)

print(res)

res = re.findall(r"\S",s1)

print(res)

res = re.findall(r".",s1)

print(res)

res = re.findall(r"[abd?]",s1)

print(res)

res = re.findall(r"\d{5}",s1)

print(res)

res = re.findall(r"\d{4,}",s1)

print(res)

res = re.findall(r"\d{4,5}",s1)

print(res)

res = re.findall(r"\d{4,5}?",s1)

print(res)

res = re.findall(r"\d*",s1)

print(res)

res = re.findall(r"\d+",s1)

print(res)

res = re.findall(r"\d?",s1)

print(res)

res = re.findall(r"wd$",s1)

print(res)

s2 = "3213aaa3bbb4124"

res = re.findall(r"\d{3}|3|2",s2)

print(res)

s3 = "12345#phone#123467890987#pwd#6543244#member_id#4444"

res = re.findall(r"#(.*?)#",s3)

# print(res)

res = re.search(r"#(.*?)#",s3)

print(res)

# res = res.group()

res = res.group(1)

print(res)

# res = re.match(r"1234",s3)

# print(res)

# res.group()
#
# print(res)












