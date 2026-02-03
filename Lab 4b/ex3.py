# Name: Ethan Mayer
# Date: Feb. 3, 2026

url = input("Enter a full URL:")

cleaned_url = url.replace("http://","")

print("Cleaned URL:", cleaned_url)

parts = cleaned_url.split(".")

domain = parts[1]
print("Domain name:", domain)

TLD = parts[2]

# We might get a trailing / character, so we need to remove it
# TLD_clean = TLD.split("/")
TLD_clean = TLD.replace("/","")
print("Top-level domain:", TLD_clean)