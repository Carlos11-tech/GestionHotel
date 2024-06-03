package Libreria;
import java.util.Date;

public class Autor {
    public String nombreAutor;
    public Date fechaNacimiento;

    //Relaciones
    private Libros libros;
    private Revistas revistas;
}
