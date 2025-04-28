package br.com.fiap.bean;

public class ArCondicionado {
    // atributos
    private int temperatura;
    private String modo;
    // metodos getters/setters 15 26
    public String getModo() {
        return modo;
    }
    public void setModo(String modo) {
        if (modo.equals("Ventilar") || modo.equals("Aquecer") || modo.equals("Resfriar")){

        }else {
            System.out.println("Modo inválido! Modos permitidos: Ventilar, Aquecer ou Resfriar.");
        }
        this.modo = modo;
    }
    public int getTemperatura() {
        return temperatura;
    }
    public void setTemperatura(int temperatura) {
        try {
            if (temperatura >= 15 && temperatura <= 26){
                this.temperatura = temperatura;
            } else {
                throw new Exception("Temperatura fora da faixa permitida!\n(Min=15 Max=26");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
    // metodos da classe (particulares)
    public void aumentarTemperatura(){
        if (temperatura < 26){
            temperatura++;
        }
    }
    public void diminuirTemperatura(){
        if (temperatura > 15){
            temperatura--;
        }
    }
}
