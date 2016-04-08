import re

f = open('sample.priv').read().splitlines()
result = dict()

for line in f:
    if line:
        regex = re.search(r'^\[(.*?.na.intgdc.com)\] out: INFO - \d+ : (\d+) : (\w+) : (\d+) days', line)
        if regex:
            host = regex.group(1)
            pos = regex.group(2)
            proj_name = regex.group(3)
            age = regex.group(4)
            if host not in result:
                result[host] = dict()
            result[host][proj_name] = {'Age': age, 'Position': pos}

print result
