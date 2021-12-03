import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class day3 {
    static final int NUMBER_SIZE = 12;

    private static class Rate {
        List<Boolean> list = new ArrayList<>();

        public void addBit(boolean bit) {
            list.add(bit);
        }

        public String toString() {
            return list.stream().map(bit -> bit ? "1" : "0").collect(Collectors.joining());
        }

        public int getValue() {
            return Integer.parseInt(toString(), 2);
        }
    }

    private static long getLines(File file) {
        try (Stream<String> stream = Files.lines(file.toPath())) {
            return stream.count();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return 0;
    }

    private static long getZeroOccurrencesAt(File file, int i) {
        try (Stream<String> stream = Files.lines(file.toPath())) {
            return stream.map(line -> line.charAt(i)).filter(c -> c == '0').count();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return 0;
    }

    public static void main(String[] args) {
        //https://adventofcode.com/2021/day/3

        final File file = new File("resources/day3.1.txt");
        final long lines = getLines(file);

        Rate gamma = new Rate();
        Rate epsilon = new Rate();
        for (int i = 0; i < NUMBER_SIZE; i++) {
            long zeroOccurrences = getZeroOccurrencesAt(file, i);
            boolean zeroOcurrencesMostCommon = zeroOccurrences > lines / 2;
            gamma.addBit(!zeroOcurrencesMostCommon);
            epsilon.addBit(zeroOcurrencesMostCommon);
        }

        System.out.println(gamma.getValue() * epsilon.getValue());
    }
}