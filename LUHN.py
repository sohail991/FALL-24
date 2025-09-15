def luhn_check(card_number):
    digits = [int(d) for d in str(card_number)]
    checksum = 0
    double = False
    for d in reversed(digits):
        if double:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d
        double = not double
    return checksum % 10 == 0

if __name__ == "__main__":
    number = input("Enter card number: ")
    if luhn_check(number):
        print("Valid card number.")