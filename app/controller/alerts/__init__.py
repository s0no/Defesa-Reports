from app.controller.alerts.data import data
from app.controller.alerts.save import save
from ..folder import folder

import logging
import imgkit
import os

__OPTIONS = {
    'xvfb': '',
    'width': 1920,
    'height': 1080
}

__NAME = 'alert'


def alerts():

    path = '{}/{}-*.png'.format(folder('Alerts'), __NAME)

    alerts = []

    contents = data()

    for content in contents:
        out = path.replace('*', content['web'])

        if(not os.path.isfile(out)):
            alerts.append(save(out, content))
    
    results = [result.result() for result in alerts]

    return results

if __name__ == "__main__":
    alerts()
