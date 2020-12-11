CREATE DATABASE IF NOT EXISTS mi_database;
use mi_database;

CREATE TABLE IF NOT EXISTS usuarios(
id          int(25) auto_increment not null;
nombre      varchar(15) not null,
apellido    varchar(15) not null,
email       varchar(50) not null,
password    varchar(200) not null,
fecha       date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS notas(
id              int(525) auto_increment not null,
usuario_id     int(25) not null,
titulo          varchar(25) not null,
descripcion     MEDIUMTEXT,
fecha           date not null,
CONSTRAINT      pk_notas    PRIMARY KEY(id),
CONSTRAINT      fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;