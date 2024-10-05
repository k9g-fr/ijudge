"""turnstile"""
ACTIONS = ""
while True:
    action = input()
    if action == "END":
        break
    ACTIONS += action
print(ACTIONS.count("CP"))
