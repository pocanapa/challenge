package br.com.fiap.repositorio;

import br.com.fiap.bean.Agendamento;

public class RepositorioAgendamento {
    public void salvar(Agendamento agendamento) {
    System.out.println("[REPOSITÓRIO] Agendamento salvo: " + agendamento);
}

    public void buscarTodos() {
        System.out.println("[REPOSITÓRIO] Buscando todos os agendamentos... (nenhum armazenado)");
    }
}

