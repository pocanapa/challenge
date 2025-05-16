package br.com.fiap.bean;

public class Usuario {

    private String nome;
    private String cpf;
    private String tipo;

    public Usuario(String nome, String cpf, String tipo) {
        this.nome = nome;
        this.cpf = cpf;
        this.tipo = tipo;
    }

    public String getNome() {
        return nome;
    }

    public String getCpf() {
        return cpf;
    }

    public String getTipo() {
        return tipo;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String descricao() {
        return nome + " (" + tipo + ")";
    }
}
