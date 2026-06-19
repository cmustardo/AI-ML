full_name = "CHIDI MUSTARD"

first_name = full_name.split()[0]
shift = len(first_name)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, shift):
    encrypt = ""

    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = (position + shift) % 26
            encrypt += alphabet[new_position]
        else:
            encrypt += character

    return encrypt
def decrypt(text, shift):
    decrypt = ""

    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            new_position = (position - shift) % 26
            decrypt += alphabet[new_position]
        else:
            decrypt += character

    return decrypt


encrypted_name = encrypt(full_name, shift)
decrypted_name = decrypt(encrypted_name, shift)




print("=" * 30)
print("      MY CIPHER REPORT")
print("=" * 30)
print("Original Name :", full_name)
print("Shift Value   :", shift)
print("Encrypted Name:", encrypted_name)
print("Decrypted Name:", decrypted_name)




# assignment 2


contacts = [
    "caleb","Tunde","Blessing","Emeka","John","Mary","Chinedu",
    "Mustard","Samuel","David","QUEEN",
    "tunde ","mary ","CALEB"," blessing ","Grace"
]

cleaned = []
seen = set()
duplicates = []
for c in contacts:
    name = c.strip().title()

    if name in seen:
        duplicates.append(name)
    else:
        seen.add(name)
        cleaned.append(name)

cleaned.sort()
print('=' * 20)
print("\nCLEANED CONTACTS")
print('=' * 20)
for i, name in enumerate(cleaned, 1):
    print(i, name)

print('=' * 20)
print("DUPLICATE REPORT ")
print('=' * 20)
if duplicates:
    for d in duplicates:
        print(d)
else:
    print("No duplicates found")




# assigment 3

receipt = [
    ("Rice", 1, 12500, "Food"),
    ("Spaghetti", 4, 950, "Food"),
    ("Milk", 2, 1800, "Food"),
    ("Toothpaste", 1, 2200, "Toiletries"),
    ("Soap", 4, 850, "Toiletries"),
    ("Detergent", 1, 6500, "Household"),
    ("Mop", 1, 7500, "Household"),
    ("Bulb", 3, 1800, "Electrical")
]

VAT = 0.075

subtotal = 0
vat = 0
categories = set()
category_total = {}

print("=" * 40)
print("      SUPERMARKET RECEIPT")
print("=" * 40)
print("Item        Qty   Price    Total")
print("-" * 40)

for item, qty, price, cat in receipt:

    total = qty * price
    subtotal += total
    categories.add(cat)

    category_total[cat] = category_total.get(cat, 0) + total

    if cat != "Food":
        vat += total * VAT

    mark = "*" if price > 5000 else ""

    print(f"{item:10} {qty:3} {price:7,} {total:8,}{mark}")

print("-" * 40)
print("\nCATEGORY TOTALS")
for cat, total in category_total.items():
    print(cat, ":", f"{total:,}")

grand_total = subtotal + vat

print("\nSUMMARY")
print("-" * 20)
print("Subtotal:", f"{subtotal:,}")
print("VAT:", f"{vat:,.2f}")
print("Grand Total:", f"{grand_total:,.2f}")
print("Unique Categories:", len(categories))
print("\nTHANK YOU FOR SHOPPING!")



buildings = [
    ("Blue House", "Residential", 1995),
    ("City Mall", "Commercial", 2005),
    ("Green Villa", "Residential", 1980),
    ("Ngwa high school", "Education", 1990),
    ("Grneral Hospital", "Health", 2010),
    ("Old Post Office", "Government", 1975),
    ("Sky Towers", "Commercial", 2018),
    ("Unity Church", "Religious", 1988)
]
current_year = 2026

types = set()
after_2000 = []
ages = []
oldest = buildings[0]

for name, btype, year in buildings:

    types.add(btype)

    age = current_year - year
    ages.append(age)

    if year > 2000:
        after_2000.append(name)

    if year < oldest[2]:
        oldest = (name, btype, year)

average_age = sum(ages) / len(ages)


print("\nBUILDING REPORT")
print("=" * 30)
print("Oldest Building:", oldest[0], "-", oldest[2])
print("\nUnique Types:", types)
print("\nBuilt After 2000:")
for b in after_2000:
    print("-", b)

print("\nAverage Age:", round(average_age, 1), "years") 