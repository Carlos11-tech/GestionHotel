import java.util.Scanner;
public class Seccion {
    public String nombreSeccion;

    //Relaciones
    private Biblioteca biblioteca;
    private Estanteria[] estanteriaList;

    public static void agregarSeccion(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Desea agregar una seccion?");
        System.out.println("1. Si");
        System.out.println("2. No");
        String respuesta = scanner.nextLine();
        if(respuesta.equals("1")) {

            System.out.println("Que seccion desea agregar?");
            String seccion = scanner.nextLine();
            System.out.println("Seccion agregada: " + seccion);
        }
    }

    public static void eliminarSeccion(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Desea eliminar una seccion?");
        System.out.println("1. Si");
        System.out.println("2. No");
        String respuesta = scanner.nextLine();
        if(respuesta.equals("1")) {
            System.out.println("Que seccion desea eliminar?");
            String seccion = scanner.nextLine();
            System.out.println("Seccion eliminada: " + seccion);
        }
    }

}

