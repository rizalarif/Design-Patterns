public class main {
    public static void main(String[] args) {

        CanadianAddress a = new CanadianAddress.Builder().apartmentNumber("1A")
                .streetNumber("123-2").streetName("Main")
                .streetType("Ave").city("Toronto").province("ON")
                .postalCode("M2K 7R1").build();

        System.out.println(a);

    }
}
