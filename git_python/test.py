from pyowm import OWM

owm = OWM('81fb235f61b9cd19f5990f320ceca3a4')  # You MUST provide a valid API key

# Search for current weather in London (Great Britain)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('London,GB')
w = observation.weather
print(w)
