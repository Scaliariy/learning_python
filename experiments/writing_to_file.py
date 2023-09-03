member = input("Enter new member: ")

file = open("../files/members.txt", 'r')
members = file.readlines()
file.close()

members.append(member)

file = open('../files/members.txt', 'w')
file.writelines(members)
file.close()
