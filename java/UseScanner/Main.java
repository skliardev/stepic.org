import java.io.ByteArrayInputStream;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        //Test
        ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream("1 2 3 4 5 6 7".getBytes());
        System.setIn(byteArrayInputStream);
        //Work
        Deque<Integer> intList = new ArrayDeque<>();
        Scanner scanner = new Scanner(System.in).useDelimiter("\\s"); // only space delimiter
        int index = 1;
        while(scanner.hasNext()) {
            if(scanner.hasNextInt() && (index % 2) == 0){
                intList.addFirst(scanner.nextInt());
            } else scanner.next();
            index++;
        }
        for (Integer n : intList)
            System.out.print(Integer.toString(n) + ' ');
    }
}
