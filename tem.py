import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]  
    temp = sys.argv[1]         
    print("user provided inputs")
else:
    script_name = sys.argv[0]
    temp = "40"
    print("default inputs")


temp_int = int(temp)

if temp_int < 15:
    state = "cold"
elif temp_int >= 15 and temp_int <= 30:  
    state = "normal"
else:
    state = "hot"

print("Script Name:", script_name)
print("Temperature:", temp)
print("State:", state)
