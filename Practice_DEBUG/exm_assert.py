import logging

# Configuration of logging
logging.basicConfig(filename='Log_of_exm_assert.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# Def of Func
def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    logging.debug('    ' + str(stoplight))
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)


# Formal code
logging.debug('Start of program')
market_2nd = {'ns': 'green',
              'ew': 'red'}
mission_16th = {'ns': 'red',
                'ew': 'green'}

for i in range(10):
    logging.debug('switch_lights of market_2nd :')
    switch_lights(market_2nd)
    logging.debug('switch_lights of mission_16th :')
    switch_lights(mission_16th)
