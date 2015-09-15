from tickets.tickets import Ticket

print("")

print("Stringtest"); x, y = Ticket("stringtest"); print x, y
print("")

print("Floattest,17,9"); x, y = Ticket(17.9); print x, y
print("")

print("Valuetest")
for i in range(-10, 133):
    print i; x,y = Ticket(i); print x, y

