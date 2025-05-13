package br.com.fiap.domain;

import java.time.LocalDateTime;

public class Agendamento {
    private Usuario usuario;
    private LocalDateTime dataHora;
    private String especialidade;
    private String status;

    public Agendamento(Usuario usuario, LocalDateTime dataHora, String especialidade) {
        this.usuario = usuario;
        this.dataHora = dataHora;
        this.especialidade = especialidade;
        this.status = "agendado";
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public LocalDateTime getDataHora() {
        return dataHora;
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public String getStatus() {
        return status;
    }

    public void confirmar() {
        this.status = "confirmado";
    }

    public void marcarComoAusente() {
        this.status = "ausente";
    }

    public String toString() {
        return String.format(
                "Agendamento:\n- Paciente: %s\n- Data e Hora: %s\n- Especialidade: %s\n- Status: %s",
                usuario.getNome(),
                dataHora.toString(),
                especialidade,
                status
        );
    }
}
