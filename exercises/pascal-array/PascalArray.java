public class PascalArray {
  int limiteInferior;
  int limiteSuperior;
  int tamanho;
  private int[] arrayInterno;

  public PascalArray(int n1, int n2) {
    // Fazemos isso para suportar um array com indices ao "contrário"
    limiteSuperior = Math.max(n1, n2);
    limiteInferior = Math.min(n1, n2);

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
