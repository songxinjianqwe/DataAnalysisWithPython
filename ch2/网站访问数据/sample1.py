import json;
from collections import Counter;

path = "../pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt";
with open(path) as data:
    records = [json.loads(line) for line in data];

# for record in records:
#     print(record['tz']);

timeZones = [record['tz'] for record in records if 'tz' in record];
# for timeZone in timeZones:
#     print(timeZone);
    
counts = Counter(timeZones);
print(counts.most_common(10));

