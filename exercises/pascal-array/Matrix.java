// Implementation of a matrix using the PascalArray.

public class Matrix {
  private PascalArray matrix;
  int nLinhas;
  int nColunas;

  public Matrix(int i, int j) {
    nLinhas = i;
    nColunas = j;
    matrix = new PascalArray(1, i * j);
  }

  public void set(int linha, int coluna, int valor) throws Exception {
    matrix.set((linha - 1) * nColunas + coluna, valor);
  }

  public int get(int linha, int coluna) throws Exception {
    return matrix.get((linha - 1) * nColunas + coluna);
  }
}
