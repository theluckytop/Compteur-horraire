import time

def compteur():
	n=0
	m=0
	h=0
	while True:
		
		print(f"{h} heure(s) {m} minute(s) {n} seconde(s)")
		time.sleep(1)
		if n==59:
			m=m+1
			n=n-60
		if m==60:
			h=h+1
			m=m-60
		n=n+1

compteur()
