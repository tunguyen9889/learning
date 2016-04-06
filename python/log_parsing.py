import re

f = open('sample.priv').read().splitlines()
result = dict()

for line in f:
    if line:
        regex = re.findall('^\[(.*?.na.intgdc.com)\] out: INFO - \d+ : (\d+) : (\w+) : (\d+) days', line)
        if regex:
            host = regex[0][0]
            pos = regex[0][1]
            proj_name = regex[0][2]
            age = regex[0][3]
            if host not in result:
                result[host] = dict()
            result[host][proj_name] = {'Age': age, 'Position': pos}

print result
