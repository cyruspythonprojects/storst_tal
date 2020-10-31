# Fråga användaren om två olika tal och låt programmet skriva ut vilket som är det största talet.
while True:
    try:
        tal_1 = int(input("Skriv in det första talet: "))
        tal_2 = int(input("Skriv in det andra talet: "))
        print("Största talet är:", max(tal_1,tal_2))
    except:
        print("Fel, SKRIV ETT TAL!")   