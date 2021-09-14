import java.io.ByteArrayInputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.Locale;
import java.util.Scanner;

public class Main1 {

    public static void main(String[] args) {
        Double sum = 0d;
        ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream("-1e3\n18 .111 11bbb .111".getBytes());
        System.setIn(byteArrayInputStream);
        Reader reader = new InputStreamReader(System.in);
        Scanner scanner = new Scanner(reader).useDelimiter("\\s|\\n").useLocale(Locale.ENGLISH);

        while(scanner.hasNext())
            if(scanner.hasNextDouble()) sum += scanner.nextDouble();
            else scanner.next();

        System.out.printf("%.6f", sum);
    }
}
