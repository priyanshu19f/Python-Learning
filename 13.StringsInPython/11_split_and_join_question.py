text = "priyanshu is a good coder and is learning python"
# python learning is and coder .... priyanshu

ans = text.split()
ans = ans[::-1]

ans = " ".join(ans)
print(ans)
