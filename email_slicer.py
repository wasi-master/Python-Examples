email  = input("Enter a email:\n")

parts = email.split("@")
user, domain = parts

print("\n")
print(f"Username: {user}")
print(f"Domain: {domain}")