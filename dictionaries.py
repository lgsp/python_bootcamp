derek_dict = {"f_name": "Derek", "l_name": "Banas", "address": "123 Main St"}

print("My Name:", derek_dict["f_name"])
derek_dict["address"] = "215 North St"
derek_dict['city'] = "Pittsburgh"
print("Is there a city:", "city" in derek_dict)
print(derek_dict.values())
print(derek_dict.keys())
for k, v in derek_dict.items():
    print(k, v)
print(derek_dict.get("m_name", "Not Here"))
del derek_dict["f_name"]
for i in derek_dict:
    print(i)
derek_dict.clear()    

employees = []
f_name, l_name = input("Enter Employee Name: ").split()
employees.append({"f_name": f_name, "l_name": l_name})
print(employees)

customers = []
ans = True
while ans:
    ans = input("Enter Customer (Y|N): ").upper()
    if ans == 'Y' or ans == 'YES':
        f_name, l_name = input("Enter Customer Name: ").split()
        customers.append({"f_name": f_name, "l_name": l_name})
    else: ans = False
        
print(customers)
