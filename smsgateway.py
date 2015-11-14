# -*- coding: utf-8 -*-
import requests

SEND_ENDPOINT = 'http://smsgateway.me/api/v3/messages/send'


class smsgateway:

    def __init__(self, username, password, device):
        self.username = username
        self.password = password
        self.device = device


    def send(self, number, msg):
        url = SEND_ENDPOINT
        args = {
            u'name': u'teste',
            u'email': self.username,
            u'password': self.password,
            u'device': self.device,
            u'number': number,
            u'message': msg,
        }
        response = requests.post(url, data=args)
        # TODO 1: Check response (13/11/2015 by: Jaime Alberto Sanchez Hidalgo)
        return response

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
