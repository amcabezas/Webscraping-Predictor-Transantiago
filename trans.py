#!/usr/bin/python
# -*- coding:UTF-8 -*-
import requests
import json
import sys

if len(sys.argv) < 2:
    sys.exit()
paradero = ' '.join(sys.argv[1:])

rs = requests.session()
url = 'http://www.transantiago.cl/predictor/prediccion?codsimt='
ser = '&codser='
url_final = '%s%s%s' % (url,paradero.upper(),ser)
micro = web.json()
x = 0
busesno = []
def disponibilidad(x):
    if '00' == micro['servicios']['item'][x]['codigorespuesta'] and '' == micro['servicios']['item'][x]['respuestaServicio']:
        recorrido(x)
        sec_recorrido(x)
    elif '01' == micro['servicios']['item'][x]['codigorespuesta'] and '' == micro['servicios']['item'][x]['respuestaServicio']:
        recorrido(x)

    elif '10' == micro['servicios']['item'][x]['codigorespuesta'] and "No hay buses que se dirijan al paradero." == micro['servicios']['item'][x]['respuestaServicio']:
        print 'No hay buses que se dirijan al paradero.'
        nodisponibilidad(x)
        print '---------------------------------'

    elif '11' == micro['servicios']['item'][x]['codigorespuesta'] and "Fuera de horario de operacion para este paradero" == micro['servicios']['item'][x]['respuestaServicio']:
        frecuencia(x)
        print '---------------------------------'

def nodisponibilidad(x):
    print 'Servicio:',micro['servicios']['item'][x]['servicio'].encode('ascii')
    return

def frecuencia(x):
    print 'Servicio:',micro['servicios']['item'][x]['servicio']
    print 'Frecuencia:',micro['servicios']['item'][x]['respuestaServicio']
    return

def sec_recorrido(x):
    print 'Aproxima micro!!!'
    print 'Servicio:',micro['servicios']['item'][x]['servicio']
    print 'Destino:',micro['servicios']['item'][x]['destino']
    print 'Patente:',micro['servicios']['item'][x]['ppubus2']
    print 'Cuando llega:',micro['servicios']['item'][x]['horaprediccionbus2']
    print '--------------------------------'
    return

def recorrido(x):
    print 'Servicio:',micro['servicios']['item'][x]['servicio']
    print 'Destino:',micro['servicios']['item'][x]['destino']
    print 'Patente:',micro['servicios']['item'][x]['ppubus1']
    print 'Cuando llega:',micro['servicios']['item'][x]['horaprediccionbus1']
    print '--------------------------------'
    return

print 'En cuanto tiempo llegara tu micro al paradero?'
if 'Paradero invalido.' == micro['respuestaParadero']:
    print 'Paradero:Invalido'
else:
    print 'Paradero:',micro['paradero']
    print 'Ubicacion:',micro['nomett']
    print 'Hora:',micro['horaprediccion']
    print '************************************'
    while x < len(micro['servicios']['item']):
        disponibilidad(x)
        x = x + 1
