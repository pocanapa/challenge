package br.com.fiap.servico;

import br.com.fiap.bean.Agendamento;
import br.com.fiap.bean.AssistenteVirtual;
import br.com.fiap.repositorio.RepositorioAgendamento;

public class ServicoAgendamento {
    private RepositorioAgendamento repository;
    private AssistenteVirtual assistente;

    public ServicoAgendamento(RepositorioAgendamento repository, AssistenteVirtual assistente) {
        this.repository = repository;
        this.assistente = assistente;
    }

    public void agendar(Agendamento agendamento) {
        repository.salvar(agendamento);
        assistente.enviarLembrete(agendamento);
    }

    public void confirmar(Agendamento agendamento) {
        agendamento.confirmar();
        assistente.enviarAgradecimento(agendamento);
    }
}