#!/usr/bin/env python3

import os

env = {
    'PATH': '/usr/local/lib/mailmark'
}

def main():
    # Get settings from manual input
    settings = {}
    options = ['COMPANY_NAME', 'CAMPAIGN_TITLE']
    settings[options[0]] = input(options[0].lower()+': ')
    settings[options[1]] = input(options[1].lower()+': ')

    # Create new project directory
    dir = os.path.join(os.getcwd(), settings['COMPANY_NAME'])
    print('DIR:', dir)
    if not os.path.exists(dir):
        os.mkdir(dir)

    # Load template
    template = open('template.html', 'r')
    content = template.readlines()
    template.close()

    # Modify HTML template
    for key in settings.keys():
        content.reaplace(key, settings[key])

    # Create required files
    style = open('style.css', 'w+')
    style.close()
    base = open('index.html', 'w+')
    base.write(content + '\n')
    base.close()

if __name__ == '__main__':
    main()
    opt = input('Do you want to start a web server on port 80? (y/n)    ').lower()
    while opt != 'y' or opt != 'n':
        print(' ERROR:  Invalid input')
        opt = input('Do you want to start a web server on port 80? (y/n)    ').lower()
    if opt == 'y':
        os.system("clear;python -c SimpleHTTPServer 80")

