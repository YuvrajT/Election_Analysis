# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100

# if (percentage_votes > 50.1 then print "WON"


# print(f"I received {percentage_votes} % of the total votes.")

# from typing import Counter


counties = ["Arapahoe","Denver","Jefferson"]
# if counties[2] == 'Denver':
#     print(counties[2])

# temperature = int(input("what is the temperature outside ?"))

# if temperature >= 80:
#     print("Turn on the AC")
# else:
#     print("Go outside")

# What is the score ?

# score = int(input("Enter your test score to find out your grade: "))

# if score >= 90:
#     print("Your grade is an A")
# else:
#     if score >= 80:
#         print("Your grade is B")
#     else:
#         if score >= 70:
#             print("Your grade is C")
#         else:
#             if score >= 60:
#                 print("Your grade is D")
#             else:
#                 print("FAIL")

# if score >= 90:
#     print("Your grade is an A")
# elif score >= 80:
#     print("Your grade is B")
# elif score >= 70:
#     print("Your grade is C")
# elif score >= 60:
#     print("Your grade is D")
# else:
#     print("FAIL")              


## Membership Operators

# countries = ["India", "Canada", "US"]

# if "India" in countries:
#     print ("True")
# else:
#     print("False")

# if "Montreal" not in countries:
#     print ("Montreal is not in countries")
# else:
#     print("Montreal is in countries")

## Logical Operatos

# x = 5
# y = 9

# if not(x>=y):
#     print ("True")
# else:
#     print("False")

# x = 6
# while x <= 7:
#     print(x)
#     x = x + 1

# for a in counties:
#     print(a)


# number = (0,1,2,3,4,5,6)
# for a in range(9):
#     print(a)


# for b in range(len(counties)):
#     print(b)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for c in counties_dict.keys():
#     print(c)

# for c in counties_dict.values():
#     print(c)

# for c in counties_dict.keys().Values():
#     print(c)

# for c in counties_dict:
#     print(counties_dict[c])

# for c in counties_dict:
#     print(counties_dict.get(c))

# for a, b in counties_dict.items():
#     print(f"{a} county has {b} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},   
               {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

# voting_data = {"county":"Arapahoe", "registered_voters": 422829}
# # print(voting_data)    

# # for g in voting_data:
# #     print(g)

# print(f"{voting_data['county']['registered_voters']}")




