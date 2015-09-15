def Ticket(age):
    """

    :param age: Input age of ticket buyer
    :return: Price for ticket in SEK
    """

    if age < 0:
        return("INVALID INPUT, you age can't be less than 0","")
    elif age > 130:
        return("INVALID INPUT, you age can't be more than 130","")
    elif age >= 100:
        return("Hello old pal your ticket price is on its way",15)
    elif age >= 0 and age < 18:
        return("Hello child your ticket price will soon be ready",10)
    elif age >= 18 and age < 65:
        return("Hello adult your ticket price is about to be ready",20)
    elif age >= 65 and age < 100:
        return("Hello oldie your ticket price is on its way",15)