package Libreria;
import java.util.Date;
import java.util.Scanner;

public abstract class Ejemplar {
    public String titulo;
    public String editorial;
    public Date fechaPublicacion;
    public boolean Prestable;

    //Metodos
    public static void agregarEjemplar(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Desea agregar un ejemplar?");
        System.out.println("1. Si");
        System.out.println("2. No");
        String respuesta = scanner.nextLine();
        if(respuesta.equals("1")) {
            System.out.println("De que tipo es el ejemplar que desea agregar?");
            System.out.println("Revista: 1");
            System.out.println("Libro: 2");
            String clasificarEjemplar= scanner.nextLine();
            System.out.println("Que ejemplar desea agregar?");
            String ejemplar = scanner.nextLine();
            System.out.println("Fecha de publicacion: ");
            String fechaDePublicacion = scanner.nextLine();
            System.out.println("Editorial:");
            String editorial = scanner.nextLine();
            System.out.println("Se puede prestar?");
            String prestable = scanner.nextLine();
            if (clasificarEjemplar.equals("1")){
                System.out.println("ejemplar de tipo Revista agregada");
            }else if (clasificarEjemplar.equals("2")){
                System.out.println("ejemplar de tipo Libro agregada");
            }
            System.out.println("Ejemplar agregado: " + ejemplar);
            System.out.println("Fecha de publicacion: " + fechaDePublicacion);
            System.out.println("Editorial: " + editorial);
            System.out.println("Prestable: " + prestable);
        }
    }


}
