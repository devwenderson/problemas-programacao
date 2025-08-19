# Problema A - Substring
## Java
```java
    import java.util.Scanner;
    public class Main {
        public static void main(String[] args) throws Exception {
            Scanner scan = new Scanner(System.in);

            // LER UMA LINHA DE CHAR'S SEPARADAS POR ESPAÇO
            String linha = scan.nextLine();
            // CORTA A STRING linha NOS ESPAÇOS
            String[] partes = linha.split(" ");

            int n = Integer.parseInt(partes[0]);
            int a = Integer.parseInt(partes[1]);
            int b = Integer.parseInt(partes[2]);

            // LÊ UMA STRING
            String s = scan.next();

            // FECHAR SCANNER
            scan.close();

            String substring = s.substring(a, n-b);

            System.out.println(substring);
        }
    }
```