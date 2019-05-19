package win.pineman.first;

import java.io.*;

// TODO: usar mysql e importar o Spring

public class First {
    public int publicField;
    public static final int publicStaticField = 2;
    protected static int protectedField;
    private static int BUFFER_SIZE = 100;

    static {
        protectedField = 42;
    }

    /**
     * Main Method
     * @param args Program command line arguments
     */
    public static void main(String[] args) {
        System.out.println(publicStaticField);
        System.out.println();
        First anObject = new First(49);
        System.out.println(anObject);
        short a = 2;
        int b = 3;
        anObject.printType(a);
        anObject.printType(b);
        anObject.printType(a - 1);
    }

    void printType(short i) {
        System.out.println(i + " Is a short");
    }
    void printType(int i) {
        System.out.println(i + " Is an int");
    }

    /**
     * Constructor
     * TODO: replace with static factory
     */
    First(int publicField) {
        this.publicField = publicField;
    }

    @Override
    public String toString() {
        return "This is a First object and its publicField is " + publicField;
    }

    // try-with-resources on multiple resources - short and sweet
    // Effective Java, Item 9
    static void copy(String src, String dst) throws IOException {
        try (InputStream in = new FileInputStream(src);
        OutputStream out = new FileOutputStream(dst)) {
            byte[] buf = new byte[BUFFER_SIZE];
            int n;
            while ((n = in.read(buf)) >= 0) {
                out.write(buf, 0, n);
            }
        }
    }
}

