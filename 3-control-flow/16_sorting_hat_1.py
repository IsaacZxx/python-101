
# Sorting Hat 🧙‍♂️

Grifinória = 0
LufaLufa = 0
Corvinal = 0
Sonserina = 0

print ('O Chapéu Seletor')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~
print ('Q1) Você gosta de Grifinória ou Sonserina?')

print (' 1) Grifinória')
print (' 2)Sonserina')

Resposta = int(input('Coloque a resposta (1-2): '))

if Resposta == 1:
  Grifinória += 1
  corvinal += 1
elif Resposta == 2:
  Sonserina += 1
  LufaLufa += 1
else:
  ('resposta errada')

  # ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

  print('Q2) qual a melhor casa')

  print ('1)Grifinória')
  print('2)Sonserina')
  print('3)LufaLufa')
  print('4)Corvinal')

  Resposta = int(input('Coloque sua resposta (1-4): '))

if Resposta == 1:
 Lufalufa += 2
elif Resposta == 2:
 Sonserina += 2
elif Resposta == 3:
 Corvinal += 2
elif Resposta == 4:
 Grifinória += 2
else:
 print('Resposta Errada.')

print("Grifinória: ", Grifinória)
print("Corvinal: ", Corvinal)
print("Lufalufa: ", Lufalufa)
print("Sonserina:", Sonserina)




 if Grifinória >= Corvinal and Grifinória >= Lufalufa and Grifinória >= Sonserina:
  print('🦁 Grifinória!')
elif Corvinal >= Lufalufa and Corvinal >= Sonserina:
  print('🦅 Corvinal!')
elif Lufalufa >= Sonserina:
  print('🦡 Lufalufa!')
else:
  print('🐍 Sonserina!')
