"""
Create a program that checks wheather a city's name begins with "SAINT"
"""
city = input("Where were you born? ").strip()
print(city[:5].upper() == "SAINT")
