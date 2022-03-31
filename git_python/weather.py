from pyowm import OWM

owm = OWM('81fb235f61b9cd19f5990f320ceca3a4')
mgr = owm.weather_manager()

place = input('Введите город: ')
observation = mgr.weather_at_place(place)
w = (observation.weather)
temp = w.temperature('celsius')['temp']

print('В городе', place, 'сейчас:', w.detailed_status)
print( 'Температура воздуха: ', temp)
print()

if temp < 0 and temp > -5:
  print('Сегодня прохладно, оденься тепло!')
elif temp < -5 and temp > -15:
  print('Сегодня холодно! Одевайся тепло!')
elif temp < -15:
  print('Осторожно очень холодно!!!')
elif temp > 0 and temp < 10:
  print('Сегодня тепло но не очень, возьмите куртку')
elif temp > 10 and temp < 20:
  print('Сегодня комфортная погода')
elif temp > 20:
  print('Начинается жара')
else:
  print('Аномальные температуры')
