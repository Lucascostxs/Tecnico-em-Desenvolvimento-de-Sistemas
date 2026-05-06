programa {
  funcao inicio() {
    inteiro idade

    escreva(" Digite sua idade ")
    leia(idade)

    se(idade >= 0 e idade <= 12){
      escreva("você é uma Criança")
    }
    senao se(idade >= 13 e idade <= 17){
      escreva("você é um Adolescente")
    }
    senao se (idade >= 18 e idade <= 59){
      escreva("você é um Adulto")
    }
    senao se (idade >= 60)
    escreva("você é um Idoso")

  }
}
