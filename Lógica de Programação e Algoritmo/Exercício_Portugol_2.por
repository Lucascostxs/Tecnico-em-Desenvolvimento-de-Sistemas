programa {
  funcao inicio() {
    real raio, volume, pi=3.14, altura, area

    escreva("Digite o raio: ")
    leia(raio)

    escreva("coloque a altura:")
    leia(altura)

    area= (2*pi*raio*(raio+altura))
    escreva(" a area é: ", area)

    volume = (pi*(raio*raio)*altura)
    escreva ("Volume igual a: ", volume)



    
  }
}
