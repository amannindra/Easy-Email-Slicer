email = "Test@gmail.com"
for i in range(len(email)):
    if email[i] == "@":
        before = email[slice(0, i)]
        after = email[slice(i+1,None)]
print("Your Username is " + before + " and " + "domain is " + after)
