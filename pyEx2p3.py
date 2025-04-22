age = int(input("Enter visitor age: "))
has_gold_pass = input("Has gold pass? (yes/no): ").lower() == "yes"
is_royal = input("Is royal? (yes/no): ").lower() == "yes"
is_blacklisted = input("Is blacklisted? (yes/no): ").lower() == "yes"
if age >= 18 and not is_blacklisted and (has_gold_pass or is_royal):
    print("✅ Visitor is allowed in.")
else:
    print("❌ Visitor is NOT allowed in.")