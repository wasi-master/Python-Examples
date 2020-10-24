email  = input("Enter a email:\n") # We take a email

parts = email.split("@") # We split the email by @ and get a list and save it as parts
user, domain = parts # We save to parts to 2 variables
# Same as:
# user   = parts[0]
# domain = parts[1]

print("\n") # We print a newline to add separation
print(f"Username : {user}") # We print the username
print(f"Domain   : {domain}") # We print the domain name