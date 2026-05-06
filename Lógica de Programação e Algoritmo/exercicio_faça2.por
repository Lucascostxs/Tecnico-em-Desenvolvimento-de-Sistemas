programa {
  funcao inicio() {
    inteiro numero, fatorial = 1

    escreva("Digite qualquer numero: ")
    leia(numero)

   para(inteiro i = numero; i >= 1; i--){
      fatorial = fatorial * i
    }
  escreva("\n o Resultado", numero," é: ", fatorial)
}
}
  
