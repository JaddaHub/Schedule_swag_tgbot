import datetime

time_str = '14:10-16:00'
cur_datetime = datetime.datetime.now()
time_str = time_str.split('-')[0]
res = cur_datetime
print(time_str, res)

print(time_str[:time_str.find(':')])
print(time_str[time_str.find(':')+1])
res = res.replace(hour=int(time_str[:time_str.find(':')]),
                  minute=int(time_str[time_str.find(':') + 1:]))
print(res)
