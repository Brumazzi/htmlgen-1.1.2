#!/usr/bin/env python2
# *-* coding:utf-8 *-*

class Route(object):
    __slots__ = ['rfile']

    def __init__(self):
        self.rfile = {}

    # Armazena o caminho do arquivo html
    def new_route(self,fname,path,alias):
        self.rfile[alias] = (
            fname,
            path,
        )

    # Escreve o arquivo caso exista.
    # Se o arquivo não existir, escreve uma mensagem de erro
    def call(self,alias,**vars):
        opt = self.rfile[alias]
        try:
            file = open(opt[1]+opt[0],'r')
        except:
            return '<p>Can\'t be find <span style="color: red;">%s</span></p>' %(opt[0])

        html = file.read()
        file.close()

        for x in vars:
            if html.count("{{"+str(x)+"}}") > 0:
                html = html.replace("{{%s}}" %(x), vars[x])
            if html.count("{{ "+str(x)+" }}") > 0:
                html = html.replace("{{ %s }}" %(x), vars[x])

        return html
