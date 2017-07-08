import re

topic = "@something"

username =  re.findall("@\w+", topic)

print username[0]
