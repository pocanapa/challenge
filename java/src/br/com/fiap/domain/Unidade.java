package br.com.fiap.domain;

public class Unidade {
    private String nome;
    private String endereco;

    public Unidade(String nome, String endereco) {
        this.nome = nome;
        this.endereco = endereco;
    }

    public String getResumo() {
        return nome + " - Endereço: " + endereco;
    }
}