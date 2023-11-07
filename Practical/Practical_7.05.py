# Task 5

# Create the two initial sets, staff and directors as shown in the first example above.
# Perform the four mathematical set operations shown,
# but use the equivalent method calls to achieve the same results. For example:
# staff = staff | {"Mark", "Ringo"}
#
# # becomes …
#
# staff = staff.union({"Mark", "Ringo"})

staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}

staff_union = staff.union({"Mark", "Ringo"})
director_staff = staff.intersection(directors)
externals = directors.difference(staff)
staff_or_external = directors.symmetric_difference(staff)

print(f"Union: {staff_union}")
print(f"Intersection: {director_staff}")
print(f"Difference: {externals}")
print(f"Symmetric difference: {staff}")


# Output:
#
# Union: {'Kelly', 'Pete', 'Paul', 'Ringo', 'Jon', 'Sally', 'Mark', 'Sue'}
# Intersection: {'Kelly', 'Jon'}
# Difference: {'Cyril', 'Rupert'}
# Symmetric difference: {'Kelly', 'Pete', 'Paul', 'Jon', 'Sally', 'Sue'}