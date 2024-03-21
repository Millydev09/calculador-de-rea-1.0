#Area de figuras planas
quard=7
quad=1
ret=2
tri=3
los=4
fig=['1-quadrado,2-retangulo,3-triangulo,4-losangulo']# variavel imutavel
#não esquecer que esse valor muda a conta
print("qual seu número de entrada para o funcionamento dos calculos?")

#não esqucer do parenteses antes do input
print("Okay, agora Escolha uma das figuras e digite o número:")
print(quad,"qudrado")
print(ret,"retagulo")
print(tri,"triangulo")
print(los,"losangulo")
#print(fig)
#print(quard[1])#teste de como usar uma variavel multavel

res=int(input("sua escolha:"))
#como usar if

if res==1:
# espaço diz quem ta fora e quem ta dentro do if e tem dois pontos
  print("você escolheu o quadrado!")
  lado=int(input("qual valor dos lados:"))
  a =0
  a =lado*lado
  print('resposta é', a)

  
if res==2:
  print("você escolheu o retangulo!")
  h=int(input("Digite a altura:"))
  b=int(input("digite a base:"))
  c=0
  c=h*b
  print('sua resposta é',c)

#int é IMPORTANTE PARA CALCULOSSS PORQUE SE NÃO O NEGOCIO NÃO RODA!
if res==3:
  print("você escolheu o triangulo!")
  al=int(input("Digite a altura:"))
  ba=int(input("digite a base:"))
  d=0
  d=al*ba/2
  print('sua resposta é',d)

if res==4:
  print("você escolheu o losango!")
  dm=int(input("digite a diagonal maior:"))
  dn=int(input("digite a diagonal menor:"))
  e=0
  e=dm*dn/2
  print('Aqui está sua respota',e)
#Código da Jamilly!
  