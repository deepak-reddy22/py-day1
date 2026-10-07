Emp = ['101,john,sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']
total_cost = 0
for var in Emp:
    eid, name, dept,cost = var.split(',')
    print(f"emp name: {name.title()}\t  dept: {dept}\t ")
    total_cost = total_cost+int(cost)

print(f"Total cost: {total_cost}")