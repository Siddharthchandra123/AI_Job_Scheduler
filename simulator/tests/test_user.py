from simulator.generators.user_generator import UserGenerator

print("="*60)
print("USER TEST")
print("="*60)

generator = UserGenerator("ACCOUNT001")

user = generator.generate()

print(user)

assert user.account_id == "ACCOUNT001"

print("\nPASSED")
