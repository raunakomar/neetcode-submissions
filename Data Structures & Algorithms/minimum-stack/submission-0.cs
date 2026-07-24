public class item{
    public int value;
    public int min_val;
}
public class MinStack {

    Stack<item> s ;
    public MinStack() {
        s =  new Stack<item>();
    }
    
    public void Push(int val) {
        if(s.Count==0)
        {
            item i = new item();
            i.value = val;
            i.min_val = val;
            s.Push(i);
        }
        else
        {
            item i = new item();
            i.value =val;
            i.min_val = Math.Min(s.Peek().min_val,val);
            s.Push(i);
        }
    }
    
    public void Pop() {
        s.Pop();
    }
    
    public int Top() {
       return s.Peek().value;
        
    }
    
    public int GetMin() {
       return s.Peek().min_val;
    }
}
