maiden_party_price = float(input())
amount_love_messages = int(input())
amount_roses = int(input())
amount_keychain = int(input())
amount_caricatures = int(input())
amount_luck_surprises = int(input())

total_amount = amount_love_messages + amount_roses + amount_keychain + amount_caricatures + amount_luck_surprises

price_love_message = amount_love_messages * 0.60
price_roses = amount_roses * 7.20
price_keychain = amount_keychain * 3.60
price_caricatures = amount_caricatures * 18.20
price_luck_surprises = amount_luck_surprises * 22

total_price = price_love_message + price_roses + price_keychain + price_caricatures + price_luck_surprises

if total_amount >= 25:
    total_price = total_price - (total_price * 0.35)

hosting = total_price * 0.1
final_price = total_price - hosting
money_left = abs(final_price - maiden_party_price)

if final_price >= maiden_party_price:
    print(f"Yes! {money_left:.2f} lv left.")
elif final_price < maiden_party_price:
    print(f"Not enough money! {money_left:.2f} lv needed.")


