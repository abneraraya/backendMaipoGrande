create database MaipoGrande;
use MaipoGrande;


CREATE TABLE administrador (
    idadministrador int not null auto_increment primary key ,
    run             VARCHAR(12) NOT NULL,
    nombre          VARCHAR(100) NOT NULL,
    puesto          VARCHAR(50) NOT NULL,
    username        VARCHAR(50) NOT NULL,
    userpass        VARCHAR(50) NOT NULL
);



CREATE TABLE clienteextranjero (
    idclienteextranjero int not null auto_increment primary key ,
    nombre              VARCHAR(100) NOT NULL,
    direccion           VARCHAR(100) NOT NULL,
    username            VARCHAR(50) NOT NULL,
    userpass            VARCHAR(100) NOT NULL
);



CREATE TABLE clientenacional (
    idclientenacional int not null auto_increment primary key,
    nombre            VARCHAR(100) NOT NULL,
    direccion         VARCHAR(100) NOT NULL,
    username          VARCHAR(50) NOT NULL,
    userpass          VARCHAR(50) NOT NULL
);



CREATE TABLE concretacionventa (
    idconcretacionventa       int not null auto_increment primary key,
    embalaje                  VARCHAR(100) NOT NULL,
    cantidad                  int NOT NULL,
    fechapago                 DATE NOT NULL,
    nombreseguro              VARCHAR(100) NOT NULL,
    tipoenvio                 VARCHAR(100) NOT NULL,
    costostransportes         int NOT NULL,
    impuestosaduanero         int NOT NULL,
    pagodeservicios           int NOT NULL,
    comisionempresa           int  NOT NULL,
    idcontratoventaextranjero int not null ,
    idinformeventaglobal      int  NOT NULL
);

CREATE UNIQUE INDEX concretacionventa__idx ON
    concretacionventa (
        idinformeventaglobal
    ASC );

CREATE UNIQUE INDEX concretacionventa__idxv1 ON
    concretacionventa (
        idcontratoventaextranjero
    ASC );

CREATE TABLE contratoproductor (
    idcontratoproductor int   NOT NULL auto_increment primary key,
    fechainicio         DATE NOT NULL,
    fechatermino        DATE NOT NULL,
    esrenovable         bool,
    fechadepago         DATE NOT NULL,
    obligaciones        text(50000) NOT NULL,
    idproductor         int  NOT NULL
);


CREATE TABLE contratoventaextranjero (
    idcontratoventaextranjero int  NOT NULL auto_increment primary key,
    fechainicio               DATE NOT NULL,
    fechatermino              DATE NOT NULL,
    esrenovable               bool,
    fechadepago               DATE NOT NULL,
    obligaciones              text(50000) NOT NULL,
    idadministrador           int  NOT NULL,
    idpedidointernacional     int  NOT NULL,
    idclienteextranjero       int  NOT NULL
);

CREATE UNIQUE INDEX contratoventaextranjero__idx ON
    contratoventaextranjero (
        idpedidointernacional
    ASC );

CREATE UNIQUE INDEX contratoventaextranjero__idxv3 ON
    contratoventaextranjero (
        idclienteextranjero
    ASC );


CREATE TABLE informeventaglobal (
    idinformeventaglobal      int  NOT NULL auto_increment primary key,
    precioventa               int  NOT NULL,
    cantidadvendida           int  NOT NULL,
    gananciatotal             int  NOT NULL,
    idcontratoventaextranjero int  NOT NULL,
    idproductor               int  NOT NULL,
    idconcretacionventa       int  NOT NULL
);

CREATE UNIQUE INDEX informeventaglobal__idx ON
    informeventaglobal (
        idproductor
    ASC );

CREATE UNIQUE INDEX informeventaglobal__idxv1 ON
    informeventaglobal (
        idcontratoventaextranjero
    ASC );

CREATE UNIQUE INDEX informeventaglobal__idxv2 ON
    informeventaglobal (
        idconcretacionventa
    ASC );


CREATE TABLE informeventapersonal (
    idinformeventapersonal    int  NOT NULL auto_increment primary key,
    precioventa               int  NOT NULL,
    cantidadvendida           int  NOT NULL,
    gananciapersonal          int  NOT NULL,
    idcontratoventaextranjero int  NOT NULL,
    idproductor               int  NOT NULL,
    idconcretacionventa       int  NOT NULL
);


CREATE TABLE pedidointernacional (
    idpedidointernacional int  NOT NULL auto_increment primary key,
    idclienteextranjero   int  NOT NULL,
    producto1             VARCHAR(100) NOT NULL,
    cantidad1             int  NOT NULL,
    embalaje1             VARCHAR(50) NOT NULL,
    producto2             VARCHAR(100),
    cantidad2             int  NOT NULL,
    embalaje2             VARCHAR(50),
    producto3             VARCHAR(100),
	cantidad3             int  NOT NULL,
    embalaje3             VARCHAR(50),
    producto4             VARCHAR(100),
	cantidad4             int ,
    embalaje4             VARCHAR(50),
    producto5             VARCHAR(100),
	cantidad5             int ,
    embalaje5             VARCHAR(50),
    producto6             VARCHAR(100),
    cantidad6             int ,
    embalaje6             VARCHAR(50),
    producto7             VARCHAR(100),
	cantidad7             int ,
    embalaje7             VARCHAR(50),
    producto8             VARCHAR(100),
	cantidad8             int ,
    embalaje8             VARCHAR(50),
    producto9             VARCHAR(100),
    cantidad9             int ,
    embalaje9             VARCHAR(50),
    producto10            VARCHAR(100),
    cantidad10            int ,
    embalaje10            VARCHAR(50)
);

CREATE UNIQUE INDEX pedidointernacional__idx ON
    pedidointernacional (
        idclienteextranjero
    ASC );


CREATE TABLE pedidonacional (
    idpedidonacional  int  NOT NULL auto_increment primary key,
    idclientenacional int  NOT NULL,
    producto1         VARCHAR(100) NOT NULL,
	cantidad1         int NOT NULL,
    embalaje1         VARCHAR(100) NOT NULL,
    producto2         VARCHAR(100),
	cantidad2         int,
    embalaje2         VARCHAR(100),
    producto3         VARCHAR(100),
	cantidad3         int,
    embalaje3         VARCHAR(100),
    producto4         VARCHAR(100),
	cantidad4         int,
    embalaje4         VARCHAR(100),
    producto5         VARCHAR(100),
	cantidad5         int,
    embalaje5         VARCHAR(100),
    producto6         VARCHAR(100),
	cantidad6         int,
    embalaje6         VARCHAR(100),
    producto7         VARCHAR(100),
	cantidad7         int,
    embalaje7         VARCHAR(100),
    producto8         VARCHAR(100),
    cantidad8         int,
    embalaje8         VARCHAR(100),
    producto9         VARCHAR(100),
	cantidad9         int,
    embalaje9         VARCHAR(100),
    producto10        VARCHAR(100),
    cantidad10        int,
    embalaje10        VARCHAR(100)
);

CREATE UNIQUE INDEX pedidointernacionalv1__idx ON
    pedidonacional (
        idclientenacional
    ASC );

CREATE TABLE postulacioninternacional (
    idpostulacioninternacional   int not null auto_increment primary key,
    idproductor                  int not null ,
    idsubastapedidointernacional int not null ,
    fruta1                       VARCHAR(50) NOT NULL,
    cantidad1                    int NOT NULL,
    embalaje1                    VARCHAR(50) NOT NULL,
    precio1                      int NOT NULL,
    fruta2                       VARCHAR(50),
    cantidad2                    int,
    embalaje2                    VARCHAR(50),
    precio2                      int,
    fruta3                       VARCHAR(50),
    cantidad3                    int,
    embalaje3                    VARCHAR(50),
    precio3                      int,
    fruta4                       VARCHAR(50),
    cantidad4                    int,
    embalaje4                    VARCHAR(50),
    precio4                      int,
    fruta5                       VARCHAR(50),
    cantidad5                    int,
    embalaje5                    VARCHAR(50),
    precio5                      int,
    fruta6                       VARCHAR(50),
    cantidad6                    int,
    embalaje6                    VARCHAR(50),
    precio6                      int,
    fruta7                       VARCHAR(50),
    cantidad7                    int,
    embalaje7                    VARCHAR(50),
    precio7                      int,
    fruta8                       VARCHAR(50),
    cantidad8                    int,
    embalaje8                    VARCHAR(50),
    precio8                      int,
    fruta9                       VARCHAR(50),
    cantidad9                    int,
    embalaje9                    VARCHAR(50),
    precio9                      int,
    fruta10                      VARCHAR(50),
    cantidad10                   int,
    embalaje10                   VARCHAR(50),
    precio10                     int,
    ganadora                     bool NOT NULL default false
);

CREATE UNIQUE INDEX postulacioninternacional__idx ON
    postulacioninternacional (
        idsubastapedidointernacional
    ASC );

CREATE TABLE postulacionnacional (
    idpostulacionnacional   int not null auto_increment primary key,
    idproductor             int not null ,
    idsubastapedidonacional int not null ,
    fruta1                  VARCHAR(50) NOT NULL,
    cantidad1               int NOT NULL,
    embalaje1               VARCHAR(50) NOT NULL,
    precio1                 int NOT NULL,
    fruta2                  VARCHAR(50),
    cantidad2               int,
    embalaje2               VARCHAR(50),
    precio2                 int,
    fruta3                  VARCHAR(50),
    cantidad3               int,
    embalaje3               VARCHAR(50),
    precio3                 int,
    fruta4                  VARCHAR(50),
    cantidad4               int,
    embalaje4               VARCHAR(50),
    precio4                 int,
    fruta5                  VARCHAR(50),
    cantidad5               int,
    embalaje5               VARCHAR(50),
    precio5                 int,
    fruta6                  VARCHAR(50),
    cantidad6               int,
    embalaje6               VARCHAR(50),
    precio6                 int,
    fruta7                  VARCHAR(50),
    cantidad7               int,
    embalaje7               VARCHAR(50),
    precio7                 int,
    fruta8                  VARCHAR(50),
    cantidad8               int,
    embalaje8               VARCHAR(50),
    precio8                 int,
    fruta9                  VARCHAR(50),
    cantidad9               int,
    embalaje9               VARCHAR(50),
    precio9                 int,
    fruta10                 VARCHAR(50),
    cantidad10              int,
    embalaje10              VARCHAR(50),
    precio10                int,
    ganadora                bool NOT NULL default false
);
#comentarios donde quede revisando las tablas

CREATE TABLE postulaciontransinternacional (
    idpostulacion               int not null auto_increment primary key,
    idtransportista             int not null ,
    idsubastatransinternacional int not null ,
    tipovehiculo1               VARCHAR(100) NOT NULL,
    patente1                    VARCHAR(100) NOT NULL,
    cadenadefrio1               VARCHAR(100),
    tipovehiculo2               VARCHAR(100),
    patente2                    VARCHAR(100),
    cadenadefrio2               VARCHAR(100),
    tipovehiculo3               VARCHAR(100),
    patente3                    VARCHAR(100),
    cadenadefrio3               VARCHAR(100),
    tipovehiculo4               VARCHAR(100),
    patente4                    VARCHAR(100),
    cadenadefrio4               VARCHAR(100),
    tipovehiculo5               VARCHAR(100),
    patente5                    VARCHAR(100),
    cadenadefrio5               VARCHAR(100),
    ganadora                    bool NOT NULL default false
);


CREATE TABLE postulaciontransnacional (
    idpostulacionnacional       int not null auto_increment primary key,
    idtransportista             int not null ,
    idsubastatransportenacional int not null ,
    tipovehiculo1               VARCHAR(100) NOT NULL,
    patente1                    VARCHAR(100) NOT NULL,
    cadenadefrio1               VARCHAR(100),
    tipovehiculo2               VARCHAR(100),
    patente2                    VARCHAR(100),
    cadenadefrio2               VARCHAR(100),
    tipovehiculo3               VARCHAR(100),
    patente3                    VARCHAR(100),
    cadenadefrio3               VARCHAR(100),
    tipovehiculo4               VARCHAR(100),
    patente4                    VARCHAR(100),
    cadenadefrio4               VARCHAR(100),
    tipovehiculo5               VARCHAR(100),
    patente5                    VARCHAR(100),
    cadenadefrio5               VARCHAR(100),
    ganadora                    bool NOT NULL default false
);

CREATE TABLE productor (
    idproductor int not null auto_increment primary key,
    rut         VARCHAR(50) NOT NULL,
    nombre      VARCHAR(100) NOT NULL,
    alias       VARCHAR(100),
    direccion   VARCHAR(200) NOT NULL,
    telefono    int NOT NULL,
    username    VARCHAR(50) NOT NULL,
    userpass    VARCHAR(50) NOT NULL
);


CREATE TABLE productos (
    idproductos          int not null auto_increment primary key,
    descripcion VARCHAR(200) NOT NULL,
    calidad     VARCHAR(20) NOT NULL,
    precio      int NOT NULL,
    estado      VARCHAR(50) NOT NULL,
    embalaje    VARCHAR(100) NOT NULL,
    cantidad    int NOT NULL,
    idproductor int not null 
);


CREATE TABLE subastapedidointernacional (
    idsubastapedidointernacional int not null auto_increment primary key,
    fechainicio                  DATE NOT NULL,
    fechatermino                 DATE,
    fechaentregadeproductos      DATE,
    idadministrador              int not null ,
    idpedidointernacional        int not null
);


CREATE UNIQUE INDEX subpedidointernacional__idx ON
    subastapedidointernacional (
        idpedidointernacional
    ASC );


CREATE TABLE subastapedidonacional (
    idsubastapedidonacional int not null  auto_increment primary key,
    fechainicio             DATE NOT NULL,
    fechatermino            DATE,
    fechaentregadeproductos DATE,
    idadministrador         int not null ,
    idpedidonacional        int not null 
);

CREATE UNIQUE INDEX subastapedidonacional__idx ON
    subastapedidonacional (
        idpedidonacional
    ASC );

CREATE TABLE subastatransinternacional (
    idsubastatransinternacional int not null auto_increment primary key,
    fechainicio                 DATE NOT NULL,
    fechatermino                DATE NOT NULL,
    fecharealizacion            DATE NOT NULL,
    direccionorigen             VARCHAR(100) NOT NULL,
    idcontratoventaextranjero   int not null ,
    direccionentrega            VARCHAR(100) NOT NULL,
    idadministrador             int NOT NULL
);

 
CREATE UNIQUE INDEX subtransinternacional__idx ON
    subastatransinternacional (
        idsubastatransinternacional
    ASC );

CREATE TABLE subastatransportenacional (
    idsubastatransportenacional int not null auto_increment primary key,
    fechainicio                 DATE NOT NULL,
    fechatermino                DATE NOT NULL,
    fecharealizacion            DATE NOT NULL,
    direccionorigen             VARCHAR(100) NOT NULL,
    idcontratoventaextranjero   int not null ,
    direccionentrega            VARCHAR(100) NOT NULL,
    idadministrador             int not null ,
    idpedidonacional            int not null 
);

CREATE UNIQUE INDEX subastatransportenacional__idx ON
    subastatransportenacional (
        idpedidonacional
    ASC );

CREATE TABLE transportista (
    idtransportista int not null auto_increment primary key,
    rut             VARCHAR(50) NOT NULL,
    nombre          VARCHAR(100) NOT NULL,
    direccion       VARCHAR(100) NOT NULL,
    username        VARCHAR(50) NOT NULL,
    userpass        VARCHAR(50) NOT NULL
);


CREATE TABLE vehiculo (
    idvehiculo      int not null auto_increment primary key,
    tipovehiculo    VARCHAR(100) NOT NULL,
    patente         VARCHAR(100) NOT NULL,
    cargamaxima     int,
    tipodecarga     VARCHAR(100),
    cadenadefrio    bool NOT NULL default false,
    idtransportista int not null 
);


#--
ALTER TABLE concretacionventa
    ADD CONSTRAINT concretacionventafk FOREIGN KEY ( idcontratoventaextranjero )
        REFERENCES contratoventaextranjero ( idcontratoventaextranjero );

ALTER TABLE contratoproductor
    ADD CONSTRAINT contratoproductorfk FOREIGN KEY ( idproductor )
        REFERENCES productor ( idproductor );


ALTER TABLE contratoventaextranjero
    ADD CONSTRAINT contratoventaextranjerofk1 FOREIGN KEY ( idadministrador )
        REFERENCES administrador ( idadministrador );


ALTER TABLE contratoventaextranjero
    ADD CONSTRAINT contratoventaextranjerofk2 FOREIGN KEY ( idclienteextranjero )
        REFERENCES clienteextranjero ( idclienteextranjero );

#--
ALTER TABLE contratoventaextranjero
    ADD CONSTRAINT contratoventaextranjerofk3 FOREIGN KEY ( idpedidointernacional )
        REFERENCES pedidointernacional ( idpedidointernacional );

 
ALTER TABLE informeventaglobal
    ADD CONSTRAINT informeventaglobalfk1 FOREIGN KEY ( idconcretacionventa )
        REFERENCES concretacionventa ( idconcretacionventa );

#--
ALTER TABLE informeventaglobal
    ADD CONSTRAINT informeventaglobalfk2 FOREIGN KEY ( idcontratoventaextranjero )
        REFERENCES contratoventaextranjero ( idcontratoventaextranjero );

 
ALTER TABLE informeventaglobal
    ADD CONSTRAINT informeventaglobalfk3 FOREIGN KEY ( idproductor )
        REFERENCES productor ( idproductor );


ALTER TABLE informeventapersonal
    ADD CONSTRAINT informeventapersonalfk1 FOREIGN KEY ( idconcretacionventa )
        REFERENCES concretacionventa ( idconcretacionventa );

#-- 
ALTER TABLE informeventapersonal
    ADD CONSTRAINT informeventapersonalfk2 FOREIGN KEY ( idcontratoventaextranjero )
        REFERENCES contratoventaextranjero ( idcontratoventaextranjero);

 
ALTER TABLE informeventapersonal
    ADD CONSTRAINT informeventapersonalfk3 FOREIGN KEY ( idproductor )
        REFERENCES productor ( idproductor );


ALTER TABLE pedidointernacional
    ADD CONSTRAINT pedidointernacionalfk1 FOREIGN KEY ( idclienteextranjero )
        REFERENCES clienteextranjero ( idclienteextranjero );


ALTER TABLE pedidonacional
    ADD CONSTRAINT pedidonacionalfk2 FOREIGN KEY ( idclientenacional )
        REFERENCES clientenacional ( idclientenacional );

 
ALTER TABLE postulacioninternacional
    ADD CONSTRAINT postulacioninternacionalfk1 FOREIGN KEY ( idproductor )
        REFERENCES productor ( idproductor );


ALTER TABLE postulacioninternacional
    ADD CONSTRAINT postulacioninternacionalfk2 FOREIGN KEY ( idsubastapedidointernacional )
        REFERENCES subastapedidointernacional ( idsubastapedidointernacional );

 
ALTER TABLE postulacionnacional
    ADD CONSTRAINT postulacionnacionalfk1 FOREIGN KEY ( idproductor )
        REFERENCES productor ( idproductor );


ALTER TABLE postulacionnacional
    ADD CONSTRAINT postulacionnacionalfk2 FOREIGN KEY ( idsubastapedidonacional )
        REFERENCES subastapedidonacional ( idsubastapedidonacional );


ALTER TABLE postulaciontransinternacional
    ADD CONSTRAINT ptransporteinternacionalfk1 FOREIGN KEY ( idsubastatransinternacional )
        REFERENCES subastatransinternacional ( idsubastatransinternacional );

#--
ALTER TABLE postulaciontransinternacional
    ADD CONSTRAINT ptransporteinternacionalfk2 FOREIGN KEY ( idtransportista )
        REFERENCES transportista ( idtransportista );


ALTER TABLE postulaciontransnacional
    ADD CONSTRAINT ptransportenacionalfk1 FOREIGN KEY ( idsubastatransportenacional )
        REFERENCES subastatransportenacional ( idsubastatransportenacional );

 
ALTER TABLE postulaciontransnacional
    ADD CONSTRAINT ptransportenacionalfk FOREIGN KEY ( idtransportista )
        REFERENCES transportista ( idtransportista );

ALTER TABLE productos
    ADD CONSTRAINT productos_productor_fk FOREIGN KEY ( idproductor )
        REFERENCES productor ( idproductor );


ALTER TABLE subastapedidointernacional
    ADD CONSTRAINT subastapedidointernacionalfk1 FOREIGN KEY ( idadministrador )
        REFERENCES administrador ( idadministrador );


ALTER TABLE subastapedidointernacional
    ADD CONSTRAINT subastapedidointernacionalfk2 FOREIGN KEY ( idpedidointernacional )
        REFERENCES pedidointernacional ( idpedidointernacional );


ALTER TABLE subastapedidonacional
    ADD CONSTRAINT subastapedidonacionalfk1 FOREIGN KEY ( idadministrador )
        REFERENCES administrador ( idadministrador );


ALTER TABLE subastapedidonacional
    ADD CONSTRAINT subastapedidonacionalfk2 FOREIGN KEY ( idpedidonacional )
        REFERENCES pedidonacional ( idpedidonacional );


ALTER TABLE subastatransinternacional
    ADD CONSTRAINT subastatransinsternacionalfk1 FOREIGN KEY ( idcontratoventaextranjero )
        REFERENCES contratoventaextranjero ( idcontratoventaextranjero );


ALTER TABLE subastatransinternacional
    ADD CONSTRAINT subatransporteinternacionalfk2 FOREIGN KEY ( idadministrador )
        REFERENCES administrador ( idadministrador );


ALTER TABLE subastatransportenacional
    ADD CONSTRAINT subastatransportenacionalfk1 FOREIGN KEY ( idadministrador )
        REFERENCES administrador ( idadministrador );


ALTER TABLE subastatransportenacional
    ADD CONSTRAINT subastatransportenacionalfk2 FOREIGN KEY ( idpedidonacional )
        REFERENCES pedidonacional ( idpedidonacional );

ALTER TABLE vehiculo
    ADD CONSTRAINT vehiculo_transportista_fk FOREIGN KEY ( idtransportista )
        REFERENCES transportista ( idtransportista );

