#!/usr/bin/env python3

# diffs male vs female PO and saves the result into CSV suitable for BGforge Weblate
# PO files MUST be identical - except for msgstr's (translations)

import polib
import csv
import sys

male_po = polib.pofile(sys.argv[1])
female_po = polib.pofile(sys.argv[2])
female_csv = sys.argv[3]

rows=[]

for i in range(0, len(male_po)-1):
  if male_po[i].msgstr != female_po[i].msgstr:
#    print(male_po[i].msgid)
#    print(male_po[i].msgstr)
#    print(female_po[i].msgstr)
    rows.append([male_po[i].msgid, female_po[i].msgstr])

rows = sorted(rows, key=lambda k: k[0])

with open(female_csv, 'w') as csvfile:
  writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
  writer.writerows(rows)
