print(sum([num for num in range(1, 18163106) if str(num).count("0") > len(str(num))//2]))
