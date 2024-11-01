import re


email = input("Enter email address \n")

text = "Please contact me at +91-123-549-4023 or via email at jda@gaml.com, astr strkes3@asr.vajr"
#+1 (123) 549-4023


pattern = r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]\d{1,3}[-.\s]?\d*"
patternemail = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"




matches = re.match(patternemail, email)
print(matches)



