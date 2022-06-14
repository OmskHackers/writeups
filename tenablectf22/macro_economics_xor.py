import re, os
os.environ['PWNLIB_NOTERM'] = 'True'
from pwn import xor

f = open('output_traffic', 'r')
str = f.read()
f.close()

data = re.findall("<html><body>[a-z0-9]+</body></html>GET /\?[A-Z0-9]+ HTTP/1.1", str)

for item in data:
    hex_str = re.search("<html><body>[a-z0-9]+</body></html>GET /\?([A-Z0-9]+) HTTP/1.1", item).group(1)
    key =  re.search("<html><body>([a-z0-9]+)</body></html>GET /\?[A-Z0-9]+ HTTP/1.1", item).group(1)

    #print(hex_str + "  " + key)

    print(xor(bytes.fromhex(hex_str.lower()), key.encode()).decode(), end="")