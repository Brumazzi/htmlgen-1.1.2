#!/usr/bin/env python
# *-* coding:utf-8 *-*

class HTMLContent(object):
    __slots__ = ["tag", "properts", "context", "vcursor", "no_close"]

    def __init__(self):
        self.tag = None
        self.properts = None
        self.context = u"<!Doctype HTML>\n\n"
        self.vcursor = []
        self.no_close = ["input",
                    "meta",
                    "img",
                    "br",
                    "link",
                    "base",
                    "hr",
                    "track",
                    "source",
                    "area",
                    "rect",
                    "option",
                    "keygen",
                    "command",
        ]

    # Inicia uma nova tag
    # create('input',required=True, id='box', class='cbox', name='caixa')
    def create(self, tag, required=False, **properts):
        push = True
        indent = len(self.vcursor)
        __new__ = ""

        for x in self.no_close:
            if tag == x:
                push = False
                break
        if push:
            self.vcursor.append(tag)

        for x in range(indent):
            __new__ = "%s\t" % (__new__)

        __new__ = u"%s<%s" % (__new__, tag)
        for x in properts:
            __new__ = __new__ + u" %s=\"%s\"" % (x, properts[x])
        if required:
            __new__ = __new__ + u" required"
        __new__ = __new__ + u">\n"

        self.context = u"%s%s" % (self.context, __new__)
        return self

    # Fecha a tag atual
    def close(self):
        last = None
        if len(self.vcursor) is not 0:
            last = self.vcursor.pop()
            indent = len(self.vcursor)
            for x in range(indent):
                self.context = "%s\t" % (self.context)
            self.context = "%s</%s>\n" % (self.context, last)

        return self

    # Fecha todas as tags abertas
    def end_page(self):
        while(len(self.vcursor) != 0):
            self.close()

    # Inseri conteudo dentro da tag atual
    def innerHTML(self, context):
        indent = len(self.vcursor)
        for x in range(indent):
            self.context = "%s\t" % (self.context)
        self.context = u"%s%s\n" % (self.context, context)
        return self

    # Recolhe a pagina criada até
    def get_page(self):
        return self.context

    def get_page_min(self):
        min = ""
        for x in self.context:
            if x != '\t' and x != '\n':
                min = u"%s%s" % (min, x)
        return min

    # Retorna a tag atualmente aberta
    def cursor(self):
        return self.vcursor[len(self.vcursor) - 1]
