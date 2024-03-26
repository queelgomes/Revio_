v = int(input())
valor = v

if valor > 0:
    notas_100 = (valor - valor % 100) / 100
    valor -= notas_100 * 100

    notas_50 = (valor - valor % 50) / 50
    valor -= notas_50 * 50

    notas_20 = (valor - valor % 20) / 20
    valor -= notas_20 * 20

    notas_10 = (valor - valor % 10) / 10
    valor -= notas_10 * 10

    notas_5 = (valor - valor % 5) / 5
    valor -= notas_5 * 5

    notas_2 = (valor - valor % 2) / 2
    valor -= notas_2 * 2

    notas_1 = valor - valor % 1
    valor -= notas_1

print(f"""{v}
{notas_100:.0f} nota(s) de R$ 100,00
{notas_50:.0f} nota(s) de R$ 50,00
{notas_20:.0f} nota(s) de R$ 20,00
{notas_10:.0f} nota(s) de R$ 10,00
{notas_5:.0f} nota(s) de R$ 5,00
{notas_2:.0f} nota(s) de R$ 2,00
{notas_1:.0f} nota(s) de R$ 1,00""")
