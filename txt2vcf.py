import sys

if len(sys.argv) != 3:
    exit(f"error: invalid arguments\nusage: python3 {sys.argv[0]} contacts.txt contacts.vcf")

file = sys.argv[1]

try:
    nums = open(file).read().strip().split('\n')
except FileNotFoundError:
    exit(f"error: {file} not found.")

vcard = ""
for number in nums:
    vcard+="BEGIN:VCARD\n"
    vcard+="VERSION:2.1\n"
    vcard+="N:;"+str(number)+";;;\n"
    vcard+="FN:"+str(number)+"\n"
    vcard+="TEL;CELL:"+str(number)+"\n"
    vcard+="TEL;CELL:"+str(number)+"\n"
    vcard+="END:VCARD\n"

open(sys.argv[2], 'w').write(vcard)
