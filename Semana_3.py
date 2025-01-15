import numpy as np
class irmaos:
    def __init__(self, nome, formacao, horario, transporte):
        self.nome = nome
        self.formacao = formacao
        self.horario = horario
        self.transporte = transporte 

    def apresentacao_fem(self):
        return f'{self.nome} formada em {self.formacao} chegou em casa de {self.transporte} as {self.horario}'

    def apresentacao_mas(self):
        return f'{self.nome} formado em {self.formacao} chegou em casa de {self.transporte} as {self.horario}'

irmaos_1 = irmaos('Ana Luiza', 'Economia', '18:00', 'carona')
irmaos_2 = irmaos('Leonardo', 'Engenharia de produção', '20:00', 'onibus')

print(irmaos_1.apresentacao_fem())
print(irmaos_2.apresentacao_mas())