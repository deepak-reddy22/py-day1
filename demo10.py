hosts = {}

print("Number of items:", len(hosts))

i = 0
while i < 5:
	hostname = input("Enter hostname: ")
	ip_address = input("Enter IP: ")
	hosts[hostname] = ip_address
	i += 1

print("Number of items:", len(hosts))

for hostname, ip_address in hosts.items():
	print(hostname, ip_address)

search_hostname = input("Enter a hostname: ")
if search_hostname in hosts:
	hosts[search_hostname] = "127.0.0.1"
else:
	hosts[search_hostname] = "127.0.0.1"

print("Updated dict details:")
for hostname, ip_address in hosts.items():
	print(hostname, ip_address)
