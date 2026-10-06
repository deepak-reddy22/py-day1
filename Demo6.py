# multi condition 

app_name = input("Enter the application name: ")

if (app_name == "flask"):
    port = 5000
elif(app_name == "fastAPI"):
    port = 8000
else:
    port = 9000

print(f"App Name: {app_name}, Port: {port}")
