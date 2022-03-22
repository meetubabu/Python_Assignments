#Find the domain name in email
email="abc.aaa.123@gmail.com"
print(email[email.find('@')+1:])
email="abc_aaa@yahoo.co.in"
print(email[email.find('@')+1:])
email="abc_______123@testing.in"
print(email[email.find('@')+1:])

#get the name of the person from the string
content="Dear User1, welcome to the program"
print(content[content.index("U"):content.index(",")])
content="Dear SuperUser2, welcome to the program"
print(content[content.index("S"):content.index(",")])
