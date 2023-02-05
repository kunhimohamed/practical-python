symbols = 'AAPL,IBM,MSFT,YHOO,SCO'

symbols = symbols + ',GOOG'

# print(symbols)

symbols = "HPQ,"+symbols

print(symbols)

print('IBM' in symbols)
print('AA' in symbols)
print('CAT' in symbols)