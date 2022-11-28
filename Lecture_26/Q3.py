veggie_prices = dict( bananas=0.59, apples=0.89,
                      squash=2.99, broccoli=1.19,
                      lettuce=0.99 )
for veggie, price in sorted(veggie_prices.items()):
    print(f"${price:.2f}", end=' ')
