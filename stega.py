def b10to2(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

input_file = open('Mission.txt', 'wt')
input_file.write("ThE MISSIOn is to Be A naTlonal volce tHAt sUpPOrTs aND enCOurAgES aCadEMIC tAleNT ANd AchleveMEnt. iT aLSO INCLUDES ENGAGING in Teaching The wORld's MOST CapaBLE YOUNG PEOPLE.WE PREPAre sTuDeNts to MAKE siGnIFiCanT future contrlButiONs to OuR worLD.WE CHALLenge them")
input_file.close()
input_file = open('Mission.txt', 'rt')


text = input_file.read()
input_file.close()

text.replace(" ",'')
print(text)
secret_bits = []
for i in range(0, int(len(text) / 8)):
  for j in range(8):
    secret_bits.append('')
    if text[i * j].isalpha() == True:
      secret_bits[i] += '1'
    elif text[i * j].islower() == True:
      secret_bits[i] += '0'
print(secret_bits)

words = ''
for m in range(0, len(secret_bits)):
  words += str((chr(int(secret_bits[m], 2))))
  if int(secret_bits[m], 2) == 0:
    break
print(words)
  
      
    