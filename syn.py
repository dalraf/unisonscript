#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
cmdssh = "ssh 192.168.0.1"
cmdmkdir = "mkdir -p"
dirdest = "/mnt/dados/share/"
dirlocal = "/home/share/"
dirfinal = "ssh://192.168.0.1//" + dirdest
param1 = "! pidof unison && /usr/local/bin/unison -perms 0 -logfile /var/log/log.unisync -auto -prefer"
diretorios=[
    'share/syncdir',
    ]

def execute(cmd):
    print "Executando " + cmd + "\n"
    saida = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, erro = saida.communicate()
    rc = saida.returncode
    if rc > 0:
        print "Erro ao executa " + cmd + "\n o erro foi\n" + output + erro + str(rc)

for dir in diretorios:
    cmd = cmdssh + " " + cmdmkdir + " " + dirdest + dir.replace("\\","\\\\")
    execute(cmd)
    cmd = param1 + " " + dirlocal + dir + " -batch " + dirlocal + dir + " " + dirfinal + dir
    execute(cmd)
