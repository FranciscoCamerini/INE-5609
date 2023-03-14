public class PascalArray {
  int limiteInferior;
  int limiteSuperior;
  int tamanho;
  int[] arrayInterno;

  public PascalArray(int n1, int n2) {
    if (n1 > n2) {
      limiteSuperior = n1;
      limiteInferior = n2;
    } else { // Fazemos isso para suportar um array ao "contrário"
      limiteSuperior = n2;
      limiteInferior = n1;
    }

    tamanho = limiteSuperior - limiteInferior + 1;
    arrayInterno = new int[tamanho];
  }

  public void checaIndice(int i) throws Exception {
    if (i > limiteSuperior || i < limiteInferior) {
      throw new Exception("Indice fora dos limites do array.");
    }
  }

  public int get(int i) throws Exception {
    checaIndice(i);

    return arrayInterno[i - limiteInferior];
  }

  public void set(int i, int valor) throws Exception {
    checaIndice(i);

    arrayInterno[i - limiteInferior] = valor;
  }
}
