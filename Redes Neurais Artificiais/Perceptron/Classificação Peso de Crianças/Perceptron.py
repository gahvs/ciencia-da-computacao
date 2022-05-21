
from linearalg.vector import Vector

class Perceptron:

    def __init__(self, numero_entradas, taxa_aprendizagem, pesos=None, limiar=0) -> None:
        
        self.limiar = limiar
        
        if pesos is None:
            self.pesos = Vector(init_with=numero_entradas)
            self.pesos.randomize()
        else:
            self.pesos = pesos

        self.taxa_aprendizagem = taxa_aprendizagem

    def activate(self, valor): 
        return 1 if valor >= self.limiar else 0

    def training(self, entrada, saida_esperada):

        soma = Vector.product(entrada, self.pesos)
        valor_saida = self.activate(soma)
        
        erro = saida_esperada - valor_saida

        # p(n+1) = p(n) + (taxa_aprendizagem * entrada * erro)

        for i in range(len(entrada.values())):
            novo_peso = self.pesos.component(i + 1) + (self.taxa_aprendizagem * entrada.component(i + 1) * erro)
            self.pesos.set(i + 1, novo_peso)
        
        return erro

    # Execução com Descrição das iterações

    # def training(self, entrada, saida_esperada):

    #     print('======================================================================')
        
    #     print(f'Padrão de Entrada: {entrada.values()} - Saída Esperada: {saida_esperada}')

    #     soma = Vector.product(entrada, self.pesos)
    #     net = self.activate(soma)
        
    #     print(f'    net  = {net}')
        
    #     erro = saida_esperada - net

    #     print(f'    erro = {saida_esperada} - {net} = {erro}')
    #     if erro == 0: print('\nErro 0 - sem ajuste de pesos', end='\n\n')

    #     # p(n+1) = p(n) + (taxa_aprendizagem * entrada * erro)

    #     for i in range(len(entrada.values())):
    #         novo_peso = self.pesos.component(i + 1) + (self.taxa_aprendizagem * entrada.component(i + 1) * erro)
            
    #         if erro != 0:
    #             print('        W%d = %.1f + ( %.1f * %.1f * %.1f ) = %.1f' % ( (i+1), self.pesos.component(i+1), self.taxa_aprendizagem, entrada.component(i+1), erro, novo_peso))
    #             #print(f'        W{i+1} = {self.pesos.component(i + 1)} + ({self.taxa_aprendizagem} * {entrada.component(i + 1)} * {erro}) = {novo_peso}')

    #         self.pesos.set(i + 1, novo_peso)
        
    #     return erro

    def feedforward(self, entrada):
        
        soma = Vector.product(entrada, self.pesos)
        valor_saida = self.activate(soma)
        return valor_saida
        
        