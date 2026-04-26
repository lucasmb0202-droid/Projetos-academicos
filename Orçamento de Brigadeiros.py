num_brig = int(input("N° de brigaeiros: "))
preco = float(input("Preço unitário (R$): "))
valor_compra = num_brig * preco
#Comprando mais de 10 brigadeiros, o cliente ganha 10% de desconto
if num_brig>10:
    print(f"Valor: R${valor_compra * 0.9:.2f}")
else:
    print(f"Valor: R${valor_compra:.2f}")