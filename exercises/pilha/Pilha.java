public class Pilha {
  int topo = -1;
  int tamanhoMax;
  private int[] arrayInterno;

  public Pilha(int t) {
    tamanhoMax = t;
    arrayInterno = new int[tamanhoMax];
  }

  public void checkFull() throws Exception {
    if (topo > tamanhoMax) {
      throw new Exception("Stack Overflow.");
    }
  }

  public void checkEmpty() throws Exception {
    if (topo == -1) {
      throw new Exception("Pilha vazia.");
    }
  }

  public void push(int value) throws Exception {
    checkFull();

    arrayInterno[topo + 1] = value;
    topo++;
  }

  public int pop() throws Exception {
    checkEmpty();

    int valorTopo = arrayInterno[topo];
    topo--;

    return valorTopo;
  }

  public int top() throws Exception {
    checkEmpty();

    return arrayInterno[topo];
  }

  public int size() {
    return topo + 1;
  }
}
