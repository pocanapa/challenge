package br.com.fiap.domain;

public class Dispositivo {
    private String modelo;
    private boolean acessibilidadeAtivada;

    public Dispositivo(String modelo, boolean acessibilidadeAtivada) {
        this.modelo = modelo;
        this.acessibilidadeAtivada = acessibilidadeAtivada;
    }

    public String getModelo() {
        return modelo;
    }

    public boolean isAcessibilidadeAtivada() {
        return acessibilidadeAtivada;
    }

    @Override
    public String toString() {
        return modelo + " (Acessibilidade: " + (acessibilidadeAtivada ? "ativada" : "desativada") + ")";
    }
}
