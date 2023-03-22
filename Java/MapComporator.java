import java.util.Comparator;
import java.util.Map;
import java.util.TreeMap;

// Sort map by value



public class MapComparator {
    public static void main(String[] args) {

        Map<String,Integer> nonSortedMap = Map.of(
                "Two",2,
                "Three", 3,
                "Five", 5,
                "One", 1,
                "Four", 4
        );

        Map<String,Integer> sortedMap = sortByValue(nonSortedMap);

        sortedMap.entrySet().forEach(System.out::println);
    }


    static Map<String,Integer> sortByValue(Map<String,Integer> map) {

        TreeMap<String,Integer> temp = new TreeMap<>(new MyMapComporator(map));
        temp.putAll(map);

        return temp;
    }

    static class MyMapComporator implements Comparator<String> {
        private final Map<String,Integer> map;

        public MyMapComporator(Map<String, Integer> map) {
            this.map = map;
        }

        @Override
        public int compare(String o1, String o2) {
            return map.get(o1) - map.get(o2); //

        }
    }


}
