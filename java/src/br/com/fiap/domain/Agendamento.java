package br.com.fiap.domain;

import java.time.LocalDateTime;

public class Agendamento {
        private Usuario usuario;
        private LocalDateTime dataHora;
        private String status; // agendado, confirmado, ausente

        public Agendamento(Usuario usuario, LocalDateTime dataHora) {
            this.usuario = usuario;
            this.dataHora = dataHora;
            this.status = "agendado";
        }

        public Usuario getUsuario() {
            return usuario;
        }

        public LocalDateTime getDataHora() {
            return dataHora;
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

        @Override
        public String toString() {
            return "Agendamento com " + usuario + " em " + dataHora + " [" + status + "]";
        }

    }
