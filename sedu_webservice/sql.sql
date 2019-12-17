BEGIN;
--
-- Create model AgenciaTransporte
--
CREATE TABLE `denuncias_agencia_transporte` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL);
--
-- Create model Aluno
--
CREATE TABLE `denuncias_aluno` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL, `ra` varchar(200) NOT NULL, `cod_energia` varchar(200) NOT NULL);
--
-- Create model Escola
--
CREATE TABLE `denuncias_escola` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL, `cod_inep` varchar(200) NOT NULL);
--
-- Create model Papel
--
CREATE TABLE `denuncias_papel` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL);
--
-- Create model ReclamacaoStatus
--
CREATE TABLE `denuncias_reclamacao_status` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL);
--
-- Create model Reclamante
--
CREATE TABLE `denuncias_reclamante` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL, `email` varchar(255) NOT NULL UNIQUE, `sub_novo` char(32) NULL);
--
-- Create model Setor
--
CREATE TABLE `denuncias_setor` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL);
--
-- Create model SRE
--
CREATE TABLE `denuncias_sre` (`group_ptr_id` integer NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL);
--
-- Create model Turno
--
CREATE TABLE `denuncias_turno` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL);
--
-- Create model TipoReclamacao
--
CREATE TABLE `denuncias_tipo_reclamacao` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL, `setor_id` integer NOT NULL);
--
-- Create model Rota
--
CREATE TABLE `denuncias_rota` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL, `cod_linha` varchar(60) NOT NULL, `escola_id` integer NOT NULL, `turno_id` integer NOT NULL);
--
-- Create model Responsavel
--
CREATE TABLE `denuncias_responsavel` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `sre_id` integer NOT NULL, `usuario_id` integer NOT NULL);
--
-- Create model Reclamacao
--
CREATE TABLE `denuncias_reclamacao` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `texto` longtext NOT NULL, `outro_papel` varchar(255) NOT NULL, `protocolo` varchar(60) NOT NULL, `data_ocorrido` datetime(6) NOT NULL, `placa_veiculo` varchar(255) NOT NULL, `outro_tipo` varchar(255) NOT NULL, `agencia_transporte_id` integer NULL, `aluno_id` integer NULL, `papel_id` integer NOT NULL, `reclamante_id` integer NULL, `rota_id` integer NOT NULL, `status_id` integer NOT NULL, `tipo_id` integer NOT NULL);
--
-- Create model ParecerFinal
--
CREATE TABLE `denuncias_parecer_final` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `texto` longtext NOT NULL, `reclamacao_id` integer NOT NULL, `responsavel_id` integer NOT NULL);
--
-- Create model Municipio
--
CREATE TABLE `denuncias_municipio` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `nome` varchar(200) NOT NULL, `cod_ibge` varchar(200) NOT NULL, `sre_id` integer NOT NULL);
--
-- Add field municipio to escola
--
ALTER TABLE `denuncias_escola` ADD COLUMN `municipio_id` integer NOT NULL;
--
-- Create model Comentario
--
CREATE TABLE `denuncias_comentario` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created_on` datetime(6) NOT NULL, `updated_on` datetime(6) NOT NULL, `texto` longtext NOT NULL, `reclamacao_id` integer NOT NULL, `responsavel_id` integer NOT NULL);
--
-- Add field escola to aluno
--
ALTER TABLE `denuncias_aluno` ADD COLUMN `escola_id` integer NOT NULL;
--
-- Add field sre to agenciatransporte
--
CREATE TABLE `denuncias_agencia_transporte_sre` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `agenciatransporte_id` integer NOT NULL, `sre_id` integer NOT NULL);
ALTER TABLE `denuncias_sre` ADD CONSTRAINT `denuncias_sre_group_ptr_id_827c5f72_fk_auth_group_id` FOREIGN KEY (`group_ptr_id`) REFERENCES `auth_group` (`id`);
ALTER TABLE `denuncias_tipo_reclamacao` ADD CONSTRAINT `denuncias_tipo_recla_setor_id_495a8ccc_fk_denuncias` FOREIGN KEY (`setor_id`) REFERENCES `denuncias_setor` (`id`);
ALTER TABLE `denuncias_rota` ADD CONSTRAINT `denuncias_rota_escola_id_683833aa_fk_denuncias_escola_id` FOREIGN KEY (`escola_id`) REFERENCES `denuncias_escola` (`id`);
ALTER TABLE `denuncias_rota` ADD CONSTRAINT `denuncias_rota_turno_id_6f3ea715_fk_denuncias_turno_id` FOREIGN KEY (`turno_id`) REFERENCES `denuncias_turno` (`id`);
ALTER TABLE `denuncias_responsavel` ADD CONSTRAINT `denuncias_responsave_sre_id_8cab4ec8_fk_denuncias` FOREIGN KEY (`sre_id`) REFERENCES `denuncias_sre` (`group_ptr_id`);
ALTER TABLE `denuncias_responsavel` ADD CONSTRAINT `denuncias_responsavel_usuario_id_6be3c844_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `denuncias_reclamacao` ADD CONSTRAINT `denuncias_reclamacao_agencia_transporte_i_ba576f2d_fk_denuncias` FOREIGN KEY (`agencia_transporte_id`) REFERENCES `denuncias_agencia_transporte` (`id`);
ALTER TABLE `denuncias_reclamacao` ADD CONSTRAINT `denuncias_reclamacao_aluno_id_9d42af3e_fk_denuncias_aluno_id` FOREIGN KEY (`aluno_id`) REFERENCES `denuncias_aluno` (`id`);
ALTER TABLE `denuncias_reclamacao` ADD CONSTRAINT `denuncias_reclamacao_papel_id_48e86d30_fk_denuncias_papel_id` FOREIGN KEY (`papel_id`) REFERENCES `denuncias_papel` (`id`);
ALTER TABLE `denuncias_reclamacao` ADD CONSTRAINT `denuncias_reclamacao_reclamante_id_a07aeff1_fk_denuncias` FOREIGN KEY (`reclamante_id`) REFERENCES `denuncias_reclamante` (`id`);
ALTER TABLE `denuncias_reclamacao` ADD CONSTRAINT `denuncias_reclamacao_rota_id_d8e11be5_fk_denuncias_rota_id` FOREIGN KEY (`rota_id`) REFERENCES `denuncias_rota` (`id`);
ALTER TABLE `denuncias_reclamacao` ADD CONSTRAINT `denuncias_reclamacao_status_id_073007f3_fk_denuncias` FOREIGN KEY (`status_id`) REFERENCES `denuncias_reclamacao_status` (`id`);
ALTER TABLE `denuncias_reclamacao` ADD CONSTRAINT `denuncias_reclamacao_tipo_id_4fb5f6a9_fk_denuncias` FOREIGN KEY (`tipo_id`) REFERENCES `denuncias_tipo_reclamacao` (`id`);
ALTER TABLE `denuncias_parecer_final` ADD CONSTRAINT `denuncias_parecer_fi_reclamacao_id_f6c3961f_fk_denuncias` FOREIGN KEY (`reclamacao_id`) REFERENCES `denuncias_reclamacao` (`id`);
ALTER TABLE `denuncias_parecer_final` ADD CONSTRAINT `denuncias_parecer_fi_responsavel_id_dc8f74d2_fk_denuncias` FOREIGN KEY (`responsavel_id`) REFERENCES `denuncias_responsavel` (`id`);
ALTER TABLE `denuncias_municipio` ADD CONSTRAINT `denuncias_municipio_sre_id_6e404c42_fk_denuncias` FOREIGN KEY (`sre_id`) REFERENCES `denuncias_sre` (`group_ptr_id`);
ALTER TABLE `denuncias_escola` ADD CONSTRAINT `denuncias_escola_municipio_id_de9a0685_fk_denuncias_municipio_id` FOREIGN KEY (`municipio_id`) REFERENCES `denuncias_municipio` (`id`);
ALTER TABLE `denuncias_comentario` ADD CONSTRAINT `denuncias_comentario_reclamacao_id_bef34413_fk_denuncias` FOREIGN KEY (`reclamacao_id`) REFERENCES `denuncias_reclamacao` (`id`);
ALTER TABLE `denuncias_comentario` ADD CONSTRAINT `denuncias_comentario_responsavel_id_7018db04_fk_denuncias` FOREIGN KEY (`responsavel_id`) REFERENCES `denuncias_responsavel` (`id`);
ALTER TABLE `denuncias_aluno` ADD CONSTRAINT `denuncias_aluno_escola_id_8254ff8a_fk_denuncias_escola_id` FOREIGN KEY (`escola_id`) REFERENCES `denuncias_escola` (`id`);
ALTER TABLE `denuncias_agencia_transporte_sre` ADD CONSTRAINT `denuncias_agencia_tr_agenciatransporte_id_7b1e78ed_fk_denuncias` FOREIGN KEY (`agenciatransporte_id`) REFERENCES `denuncias_agencia_transporte` (`id`);
ALTER TABLE `denuncias_agencia_transporte_sre` ADD CONSTRAINT `denuncias_agencia_tr_sre_id_65a415f1_fk_denuncias` FOREIGN KEY (`sre_id`) REFERENCES `denuncias_sre` (`group_ptr_id`);
ALTER TABLE `denuncias_agencia_transporte_sre` ADD CONSTRAINT `denuncias_agencia_transp_agenciatransporte_id_sre_5b686f4d_uniq` UNIQUE (`agenciatransporte_id`, `sre_id`);
COMMIT;
