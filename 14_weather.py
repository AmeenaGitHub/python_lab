# 14 Weather report
import json

# Sample nested JSON weather dataset
data = '''
{
  "cities": [
    {"name": "Kochi",     "country": "India",
     "main": {"temp": 31.5, "humidity": 78}},
    {"name": "Delhi",     "country": "India",
     "main": {"temp": 36.2, "humidity": 45}},
    {"name": "Mumbai",    "country": "India",
     "main": {"temp": 33.0, "humidity": 70}},
    {"name": "Bengaluru", "country": "India",
     "main": {"temp": 27.4, "humidity": 60}}
  ]
}
'''

# 1. Parse the JSON string
weather = json.loads(data)

# 2. Flatten the nested JSON into table rows
rows = []
for c in weather["cities"]:
    rows.append([c["name"], c["country"], c["main"]["temp"], c["main"]["humidity"]])

# 3. Display the table
print(f"{'City':<12}{'Country':<10}{'Temp(C)':<10}{'Humidity(%)'}")
print("-" * 43)
for r in rows:
    print(f"{r[0]:<12}{r[1]:<10}{r[2]:<10}{r[3]}")

# 4. Display the summary report
temps = [r[2] for r in rows]
humidity = [r[3] for r in rows]
hottest = max(rows, key=lambda r: r[2])
coldest = min(rows, key=lambda r: r[2])

print("\n--- Summary Report ---")
print("Cities reported   :", len(rows))
print(f"Average temp      : {sum(temps) / len(temps):.1f} C")
print(f"Average humidity  : {sum(humidity) / len(humidity):.1f} %")
print(f"Hottest city      : {hottest[0]} ({hottest[2]} C)")
print(f"Coldest city      : {coldest[0]} ({coldest[2]} C)")