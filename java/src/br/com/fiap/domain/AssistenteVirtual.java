package br.com.fiap.domain;

public class AssistenteVirtual {
    public void enviarLembrete(Agendamento agendamento) {
        System.out.println("Enviando lembrete para " + agendamento.getUsuario().getNome());
    }

    public void enviarAgradecimento(Agendamento agendamento) {
        System.out.println("Obrigado por participar do atendimento, " + agendamento.getUsuario().getNome());
    }
}
