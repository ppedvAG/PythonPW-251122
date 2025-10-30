text = "Das ist ein Text!"

def countCase(input: str):
	gross, klein, sonder = 0, 0, 0
	for x in input:
		if x.isupper(): gross += 1
		elif x.islower(): klein += 1
		else: sonder += 1
	print(f"Sonderzeichen: {sonder}, Groß: {gross}, Klein: {klein}")

if __name__ == "__main__":
	countCase(text)