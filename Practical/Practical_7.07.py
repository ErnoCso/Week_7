# Task 7

# Write code based on the previous two examples,
# but use the equivalent method calls to achieve the same results.

staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}

if managers.issubset(staff):
    print("All managers are staff members")
if staff.issuperset(managers):
    print("All managers are staff members")

# Output:
#
# All managers are staff members
# All managers are staff members