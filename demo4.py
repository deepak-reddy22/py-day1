app_name = "my application"

if 'flask' in app_name.lower():
    port = 5000
    
else:
    port = 8000
    
print(f"App Name: {app_name}, Port: {port}")