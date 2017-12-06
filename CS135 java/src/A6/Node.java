package A6;

public class Node{
    public int key;
    public String value;
    public Node left;
    public Node right;

    public Node (int gKey, String gValue, Node gLeft, Node gRight){
        this.key = gKey;
        this.value = gValue;
        this.left = gLeft;
        this.right = gRight;
    }
}
