import csv
from lxml import etree

adsinfo = "ads.csv"

adsinfo_data = []

parser = etree.XMLParser(recover=False, remove_blank_text=False)

inp_file = "ads.xml"

# use lxml to read and parse xml
root = etree.parse(inp_file, parser)

# element names with data to keep
tag_list = [ "ad_id", "category_id", "region_id", "ad_price" ]
 
# add field names by copying tag_list
adsinfo_data.append(tag_list[:])

# pull info out of each node
def get_info(a):
  info = []
  for tag in tag_list:
    node = a.find(tag)
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
ads = root.findall(".//ad")
for a in ads:
  ads_info = get_info(a)
  if ads_info:
    adsinfo_data.append(ads_info)

print("[finished]")
print("writing output files...")

write_csv(adsinfo_data, adsinfo)
