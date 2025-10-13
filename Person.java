public class Person implements Comparable<Person>{
    private int age;
    private String lastName;
    private String firstName;

    public Person(String FirstName, String lastName, int age){
        this.age = age;
        this.lastName = lastName;
        this.firstName = firstName;
    }

    @Override
    public int compareTo(Person p){
        int compared = Integer.compare(this.age, p.age);
        if (compared == 0) compared = this.lastName.compareTo(p.lastName);
        if (compared == 0) compared = this.firstName.compareTo(p.firstName);
        return compared;
    }

    @Override
    public String toString(){
        return "Person{" + firstName + ", " + lastName + ", " + age + "}";
    }

    public static void main(String[] args){
        Person p = new Person("John", "Doe", 12);
        Person q = new Person("Jane", "Doe", 13);

        System.out.println(p.compareTo(q));
        System.out.println("p" + (p instanceof Person));
        System.out.println("q" + (q instanceof Person));


    }
}
