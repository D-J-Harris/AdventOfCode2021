import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;

class Day1 {

    public static void main(String[] args) throws IOException {

        List<Integer> inp = new ArrayList<>();
        Files.lines(Paths.get("input.txt")).forEach(line -> inp.add(Integer.valueOf(line)));

        int ans1 = 0;
        int ans2 = 0;

        ListIterator<Integer> it = inp.listIterator();
        while (it.hasNext()) {
            int index = it.nextIndex();
            int val = it.next();
            if (index > 0 && val > inp.get(index-1)) {
                ans1 += 1;
            }
            if (index > 2 && val > inp.get(index-3)) {
                ans2 += 1;
            }
        }

        System.out.println("answer to puzzle 1 is: " + ans1);
        System.out.println("answer to puzzle 2 is: " + ans2);
    }
}