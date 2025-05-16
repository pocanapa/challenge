package br.com.fiap.bean;

import java.time.LocalDateTime;

public class Notificacao {
    private String destino;
    private String mensagem;
    private String canal;
    private LocalDateTime dataHoraEnvio;

    public Notificacao(String destino, String mensagem, String canal) {
        this.destino = destino;
        this.mensagem = mensagem;
        this.canal = canal;
        this.dataHoraEnvio = LocalDateTime.now();
    }

    public String getDestino() {
        return destino;
    }

    public String getMensagem() {
        return mensagem;
    }

    public String getCanal() {
        return canal;
    }

    public LocalDateTime getDataHoraEnvio() {
        return dataHoraEnvio;
    }

    public void exibirResumo() {
        System.out.println("[" + canal + "] Enviado para " + destino + " às " + dataHoraEnvio);
        System.out.println("Mensagem: " + mensagem);
    }
}

