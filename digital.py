"""digital"""
def main(name, thai, home, age, income, save):
    """wallet"""
    if thai in ("Yes","True") and home in ("Yes", "True") \
        and age >= 16 and income <= 840000 and save <= 500000:
        print(f"Congratulations! {name} is qualified to receive a digital wallet \
amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main(str(input()),str(input()),str(input()),float(input()),float(input()),float(input()))
