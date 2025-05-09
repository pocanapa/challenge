package br.com.fiap.domain;

public class Usuario {
    private String nome;
    private String cpf;
    private String tipo; // paciente, cuidador, profissional

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

    @Override
    public String toString() {
        return nome + " (" + tipo + ")";
    }
}

