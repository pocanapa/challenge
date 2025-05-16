package br.com.fiap.bean;

public class Unidade {

    private String nome;
    private String endereco;

    public Unidade(String nome, String endereco) {
        this.nome = nome;
        this.endereco = endereco;
    }

    public String getNome() {
        return nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public String getResumo() {
        return nome + " - " + endereco;
    }
}

