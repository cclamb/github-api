#!/usr/bin/env python3

__author__ = 'cclamb'

import requests
import urllib.parse as parse

from random import Random


base_url = 'https://api.github.com/users'
cclamb_url = base_url + '/cclamb'
auth = ('cclamb', 'ab212719')


def random_control_chars():
    floor, ceiling = 0, 32
    return chr(Random().randint(floor, ceiling))


def random_unicode(base=8):
    floor, ceiling = 33, 2**base
    return chr(Random().randint(floor, ceiling))


def print_header(headers):
        print('HTTP Headers on response:')
        for header in headers.keys():
            print('\t%s : %s' % (header, headers[header]))


def decorate_url_js(url):
    return url + '/"var x = 1"'


def decorate_url_with_ctrls(url, cnt):
    for i in range(cnt):
        url += random_control_chars()
    return url


def decorate_url_with_unicode(url, cnt):
    for i in range(cnt):
        url += random_unicode()
    return url


def decorate_url(url, cnt):
    for i in range(cnt):
        if Random().randint(0, 9) <= 5:
            url = decorate_url_with_ctrls(url, 1)
        else:
            url = decorate_url_with_unicode(url, 1)
    return url


def attack(url):
    print('URL: %s' % url)
    response = requests.get(url, auth=auth)
    print_header(response.headers)
    print(response.text)


attack_url = decorate_url(base_url, 100)
q = parse.quote(attack_url)
uq = parse.unquote(q)
print(attack_url)
print(q)
print(uq)

# attack(attack_url)

