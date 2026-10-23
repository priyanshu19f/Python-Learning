text = "           Priyanshu Gupta          "
print(text.strip())

text1 = "           Hello  h     "
print(text1.lstrip())

text2 = "        Priyu                  "
print(text2.rstrip())


url = "https://www.priyututor.com/"
clean_url = url.strip("https:/")
print(clean_url)


text = "###important###"
clean_msg = text.strip("#")
print(clean_msg)
