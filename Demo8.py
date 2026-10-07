host=[]
print(f"number of hosts: {len(host)}")

c=0
while c < 5:
    h=input("Enter host: ")
    host.append(h)
    c += 1
    
print(f"number of elements: {len(host)}")

for var in host:
    print(var)
    
host_name = input("Enter host name to search: ")
if host_name in host:
    host[-1] = host_name
else:
   host.append(host_name)

print("\n")
for var in host:
    print(var)