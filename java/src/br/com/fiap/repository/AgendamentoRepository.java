package br.com.fiap.repository;

import br.com.fiap.domain.Agendamento;

public class AgendamentoRepository {
    public void salvar(Agendamento agendamento) {
        // Simula salvar no banco
        System.out.println("[REPOSITÓRIO] Agendamento salvo: " + agendamento);
    }

    public void buscarTodos() {
        // Simula uma busca, como ainda não armazenamos, apenas imprime mensagem
        System.out.println("[REPOSITÓRIO] Buscando todos os agendamentos... (nenhum armazenado)");
    }
}
