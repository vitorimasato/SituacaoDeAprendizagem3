valCompraTotal = float(input("Digite o valor da compra: "))
valPagamento = float(input("Digite o valor do pagamento: "))
valTroco = round(valPagamento - valCompraTotal, 2)
print("Valor total da compra: R${}"
      "\nValor do pagamento: R${}"
      "\nValor do troco: R${}".format(valCompraTotal, valPagamento, valTroco))

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
moedas1 = 0
moedas50 = 0
moedas25 = 0
moedas10 = 0
moedas05 = 0

if valTroco >= 100.00:
    notas100 = valTroco // 100.00
    valTroco = valTroco - (100 * notasCem)

if valTroco >= 50.00:
    notas50 = valTroco // 50
    valTroco = valTroco - (50 * notas50)

if valTroco >= 20.00:
    notas20 = valTroco // 20
    valTroco = valTroco - 20 * notas20

if valTroco >= 10.00:
    notas10 = valTroco // 10
    valTroco = valTroco - 10 * notas10

if valTroco >= 5.00:
    notas5 = valTroco // 5
    valTroco = valTroco - 5 * notas5

if valTroco >= 2.00:
    notas2 = valTroco // 2
    valTroco = valTroco - 2 * notas2

if valTroco >= 1.00:
    moedas1 = valTroco // 1
    valTroco = valTroco - moedas1

if valTroco >= 0.50:
    moedas50 = valTroco // 0.50
    valTroco = valTroco - 0.50 * moedas50

if valTroco >= 0.25:
    moedas25 = valTroco // 0.25
    valTroco = valTroco - 0.25 * moedas25

if valTroco >= 0.10:
    moedas10 = valTroco // 0.10
    valTroco = valTroco - 0.10 * moedas10

if valTroco >= 0.05:
    moedas05 = valTroco // 0.05
    valTroco= valTroco - 0.05 * moedas05

print("Notas de R$100,00: {}"
      "\nNotas de R$50,00: {}"
      "\nNotas de R$20,00: {}"
      "\nNotas de R$10,00: {}"
      "\nNotas de R$5,00: {}"
      "\nNotas de R$2,00: {}"
      "\nMoedas de R$1,00: {}"
      "\nMoedas de R$0,50: {}"
      "\nMoedas de R$0,25: {}"
      "\nMoedas de R$0,10: {}"
      "\nMoedas de R$0,05: {}".format(notas100, notas50, notas20, notas10, notas5, notas2, moedas1, moedas50, moedas25, moedas10, moedas05))
