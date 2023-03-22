public class Fila {
  private int tamanho;
  private int nElementos = 0;
  private int inicio = 0;
  private int fim = 0;
  private int[] fila;

  public Fila(int tamanho) {
    this.tamanho = tamanho;
    this.fila = new int[tamanho];
  }

  public boolean cheia() {
    return this.nElementos == tamanho;
  }

  public boolean vazia() {
    return this.nElementos == 0;
  }

  public int sair() throws Exception {
    if (this.vazia()) {
      throw new Exception("Fila vazia");
    }

    int valor = this.fila[this.inicio];
    this.inicio = (this.inicio + 1) % this.tamanho;
    this.nElementos--;

    return valor;
  }

  public void entrar(int valor) throws Exception {
    if (this.cheia()) {
      throw new Exception("Fila cheia");
    }

    this.fila[this.fim] = valor;
    this.fim = (this.fim + 1) % this.tamanho;
    this.nElementos++;
  }
}
