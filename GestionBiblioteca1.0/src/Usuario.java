import java.util.Scanner;

public class Usuario {
    public String nombreUsuario;
    public String cedula;

    //Relaciones
    private Prestamo prestamo;
    private Biblioteca[] biblioteca;

    //Metodos
    public static void agregarUsuario(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Desea agregar un usuario?");
        System.out.println("1. Si");
        System.out.println("2. No");
        String respuesta = scanner.nextLine();
        if(respuesta.equals("1")) {
            System.out.println("Que usuario desea agregar?");
            String usuario = scanner.nextLine();
            System.out.println(("Ingrese la cedula del usuario: "));
            String cedula = scanner.nextLine();
            System.out.println("Usuario agregado: " + usuario);
            System.out.println("Cedula: " + cedula);
        }
    }

    public static void eliminarUsuario(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Desea eliminar un usuario?");
        System.out.println("1. Si");
        System.out.println("2. No");
        String respuesta = scanner.nextLine();
        if(respuesta.equals("1")) {
            System.out.println("Que usuario desea eliminar?");
            String usuario = scanner.nextLine();
            System.out.println(("Ingrese la cedula del usuario: "));
            String cedula = scanner.nextLine();
            System.out.println("Usuario eliminado: " + usuario);
        }
    }
}
