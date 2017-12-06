package A6;
import java.util.*;
public class trees {

    public static int madeline (int n){
        if (n==1)
        return 1;
        else
        return n * madeline(n-1);
    }
    public static void main(String[] args) {
        System.out.println(madeline(15));


}}


