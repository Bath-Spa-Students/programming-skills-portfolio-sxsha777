guests=["Lily", "Maria", "Annie", "Minie", "Star", "Nene"]
print(f'{guests[2]} and {guests[3]} can not make it to dinner..')
guests.remove("Annie")
guests.remove("Minie")
guests.append("Kairi")
guests.append("Mary")
print(guests)
for i in guests:
    print(f'Hello {i}!! Would you join me for dinner today?')