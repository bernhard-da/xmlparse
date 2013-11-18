import csv
from lxml import etree

userinfo = "userinfo.csv"
eventinfo = "eventinfo.csv"

userinfo_data = []
eventinfo_data = []

parser = etree.XMLParser(recover=False, remove_blank_text=False)

inp_file = "user.xml"

# use lxml to read and parse xml
root = etree.parse(inp_file, parser)

# element names with data to keep
tag_list = [ "user_id", "name", "sur_name", "email_address" ]
event_list = [ "user_id", "type", "time", "source_id", "feature_id", "ad_id"]
 
# add field names by copying tag_list
userinfo_data.append(tag_list[:])
eventinfo_data.append(event_list[:])

# pull info out of each node
def get_info(u):
  info = []
  for tag in tag_list:
    node = u.find(tag)
    if node is not None and node.text:
        info.append(node.text)
        #info.append(node.text.encode("utf-8"))
    else:
      info.append("")
  return info

# pull info out of each node
def get_event(e, uid):
  info = []
  info.append(uid)
  for tag in event_list:
    if tag=="user_id":
      info.append(uid)
    else:
      node = e.find(tag)
      if node is not None and node.text:
        info.append(node.text)
      else:
        info.append("")
  return info

# write csv file
def write_csv(inp, outfile):
  f = open(outfile, 'w', encoding='utf-8')
  print("--> writing", outfile, "...", end="")
  csv_writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, delimiter=";")

  for row in inp:
    csv_writer.writerow(row)
  f.close()
  print("[finished]")

## start program
print("parsing xml file", inp_file, "...", end="")

# get all elements
users = root.findall(".//user")
for u in users:
  user_info = get_info(u)
  if user_info:
    userinfo_data.append(user_info)
    uid = user_info[0]
    events = root.findall(".//event")
    for e in events:
      event_info = get_event(e, uid)
      if ( event_info):
        eventinfo_data.append(event_info)

print("[finished]")
print("writing output files...")

write_csv(userinfo_data, userinfo)
write_csv(eventinfo_data, eventinfo)
