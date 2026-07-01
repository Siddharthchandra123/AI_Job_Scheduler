from simulator.generators.user_generator import UserGenerator

gen = UserGenerator("ACCOUNT-001")

user = gen.generate()

print(user)

assert user.account_id == "ACCOUNT-001"

print("User Generator Passed")
