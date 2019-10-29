import pandas

data_comma = pandas.read_csv("supermarkets-commas.txt")
print(data_comma)

data_semicolon = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
print(data_semicolon)
