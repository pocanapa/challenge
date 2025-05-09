package br.com.fiap.service;

import br.com.fiap.domain.Agendamento;
import br.com.fiap.domain.AssistenteVirtual;
import br.com.fiap.repository.AgendamentoRepository;

public class AgendamentoService {
    private AgendamentoRepository repository;
    private AssistenteVirtual assistente;

    public AgendamentoService(AgendamentoRepository repository, AssistenteVirtual assistente) {
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
