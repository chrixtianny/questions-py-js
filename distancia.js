function calculoDistancia (){
    const distanciaTotal = 100;
    const pedagios = 2;
    const tempoPedagio = pedagios * (5/60);
    const velocidadeCarro = 110;
    const velocidadeCaminhao = 80;

    const tempoCarro = distanciaTotal / velocidadeCarro;
    const tempoCaminhao = distanciaTotal / velocidadeCaminhao + tempoPedagio;

    let encontroVeiculos = distanciaTotal / (velocidadeCarro + velocidadeCaminhao) + tempoPedagio;

    let distanciaCarro = encontroVeiculos * velocidadeCarro;
    let distanciaCaminhao = encontroVeiculos * velocidadeCaminhao;

    if (distanciaCarro > distanciaCaminhao){
        console.log("O carro está mais próximo de seu destino, que é Franca. \nEntão o caminhão tá mais perto de Ribeirão Preto")
    } else if (distanciaCaminhao > distanciaCarro){
        console.log("O caminhão está mais próximo de seu destino, Ribeirão Preto")
    } else {
        console.log("Os veículos estão na mesma distância")
    }
}

calculoDistancia();