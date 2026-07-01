from simulator.generators.account_generator import AccountGenerator

print("="*60)
print("ACCOUNT TEST")
print("="*60)

account = AccountGenerator().generate()

print(account)

assert account.organization_name != ""

print("\nPASSED")
