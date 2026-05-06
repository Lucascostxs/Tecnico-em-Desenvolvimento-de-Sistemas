programa {
  funcao inicio() {
    inteiro lado1, lado2, lado3

    escreva("digite o lado1 ")
    leia(lado1)

        escreva("digite o lado2 ")
        leia(lado2)

            escreva("digite o lado3 ")
            leia(lado3)

            se (lado1 == lado2 e lado1 == lado3 e lado3 == lado2){
            escreva("O triangulo é Equilátero")
            }
            senao se(lado1 != lado2 e lado1 != lado3 e lado2 != lado3){
              escreva(" o triangulo é escaleno")
            }
            senao se (lado1 == lado2 ou lado2 == lado3 ou lado3 == lado1){
              escreva("O triangulo é Isósceles")
        
  
          
            }

  }
}
