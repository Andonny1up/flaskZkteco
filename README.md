# Flask ZKteco

Microservicio para manejar dispositivos Biometricos ZKteco. Version previa

## Requisitos

- Python > 3.11

## Instalación

Clonar el proyecto:

```bash
  git clone https://github.com/Andonny1up/flaskZkteco.git
```

Crear un entornor virtual desde la carpeta raiz del proyecto:

```bash
  python -m venv venv
```

Activar el entorno virtual

```bash
  ./venv/Scripts/activate
```

Instalar las dependencias

```bash
  pip install -r requirements.txt
```

Correr el programa:

```bash
  python run.py
```

## Referencia de la API

### obtener asistencias

Conten type: json

```http
  POST /asistencias
```

#### Ejemplo de Cuerpo:

```http
{
  "ip": "192.xxx.xxx.xx",
  "port": 4370,
  "password": xxxxx
}
```

### Borrar asistencias

Conten type: json

```http
  POST /asistencias/borrar
```

#### Ejemplo de Cuerpo:

Se necesita enviar la cantidad exacta de los registros por seguridad, se puede obtener de /asistencias

```http
{
  "ip": "192.xxx.xxx.xx",
  "port": 4370,
  "password": xxxxx,
  "quantity": x
}
```
