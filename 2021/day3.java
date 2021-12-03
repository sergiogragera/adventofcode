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

        public void setBinary(String binary) {
            list = Stream.of(binary.split("")).map(bit -> bit.equals("1")).collect(Collectors.toList());
        }
    }

    private static long getLines(File file) {
        return getLines(file, "");
    }

    private static long getLines(File file, String prefix) {
        try (Stream<String> stream = Files.lines(file.toPath()).filter(line -> line.startsWith(prefix))) {
            return stream.count();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return 0;
    }

    private static String getLine(File file, String prefix) {
        try (Stream<String> stream = Files.lines(file.toPath()).filter(line -> line.startsWith(prefix))) {
            return stream.findAny().get();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return "";
    }

    private static long getZeroOccurrencesAt(File file, int i) {
        return getZeroOccurrencesAt(file, i, "");
    }

    private static long getZeroOccurrencesAt(File file, int i, String prefix) {
        try (Stream<String> stream = Files.lines(file.toPath()).filter(line -> line.startsWith(prefix))) {
            return stream.map(line -> line.charAt(i)).filter(c -> c == '0').count();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return 0;
    }

    public static void main(String[] args) {
        //https://adventofcode.com/2021/day/3#part1

        final File file = new File("2021/resources/day3.1.txt");
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

        //https://adventofcode.com/2021/day/3#part2
        
        final File file2 = new File("2021/resources/day3.2.txt");

        Rate o2 = new Rate();
        Rate co2 = new Rate();
        for (int i = 0; i < NUMBER_SIZE; i++) {
            long zeroOccurrencesO2 = getZeroOccurrencesAt(file2, i, o2.toString());
            long zeroOccurrencesCo2 = getZeroOccurrencesAt(file2, i, co2.toString());
            long linesO2 = getLines(file2, o2.toString());
            if (linesO2 <= 1) {
                o2.setBinary(getLine(file2, o2.toString()));
            }
            else {
                o2.addBit(zeroOccurrencesO2 <= linesO2 / 2);
            }

            long linesCo2 = getLines(file2, co2.toString());
            if (linesCo2 <= 1) {
                co2.setBinary(getLine(file2, co2.toString()));
            }
            else {
                co2.addBit(zeroOccurrencesCo2 > linesCo2 / 2);
            }
        }

        System.out.println(o2.getValue() * co2.getValue());
    }
}