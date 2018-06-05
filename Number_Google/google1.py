import random

google1 = open("google1.txt", "w")

letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
          'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

# for a in range(100):  # # 10**8				<< File was 100MB >> 100 times
for b in range(100):  # # 10**6			<< File was 1MB >>	 1000 times
    for c in range(100):  # # 10**4		<< File was 10KB >>	 100 times
        for d in range(100):  # # 10**2	<< File was 100 byte >>
            l = random.choice(letter)
            google1.write(l)
