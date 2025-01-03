
# Data Science Learning and Projects
Este documento proporciona instrucciones detalladas para configurar y ejecutar el proyecto en su entorno local, cubriendo tanto sistemas Linux/Mac como Windows.

## Prerrequisitos

Antes de comenzar, asegúrese de tener instalados los siguientes componentes:

- **Python 3.x:** Puede descargarlo e instalarlo desde [python.org](https://www.python.org/downloads/).
- **pip:** Es una herramienta de gestión de paquetes para Python. Normalmente se instala junto con Python.

## Configuración del Proyecto

Siga estos pasos para configurar el entorno del proyecto:

### 1. Crear o acceder a una carpeta para el proyecto
Cree o acceda a una carpeta en su sistema donde almacenará todos los archivos relacionados con el proyecto. Navegue a esa carpeta en su terminal antes de ejecutar cualquier comando.

### 2. Verificar la Instalación de pip

En la mayoría de los casos, pip se instala junto con Python. Puede verificar si pip está instalado ejecutando:

```bash
pip --version
```

Si pip no está instalado, siga los pasos a continuación para instalarlo.

#### En Linux/MacOS

```bash
sudo apt-get install python3-pip
```

#### En Windows

pip se instala automáticamente con la instalación de Python. Si no está disponible, puede usar el instalador de Python para agregar pip a su sistema.

### 3. Crear un Entorno Virtual

Crear un entorno virtual ayuda a aislar las dependencias de su proyecto. Esto es útil para evitar conflictos de versión entre diferentes proyectos.

```bash
python3 -m venv .venv
```

### 4. Activar el Entorno Virtual

Active el entorno virtual para asegurarse de que las dependencias se instalan en el lugar correcto:

#### En Linux/MacOS

```bash
source .venv/bin/activate
```

#### En Windows

```bash
.venv\Scripts\activate
```

### 5. Instalar las Dependencias

Con el entorno virtual activado, instale todas las dependencias requeridas que se encuentran listadas en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 6. Ejecutar el Proyecto

Después de la configuración inicial, puede ejecutar su proyecto o abrir un notebook de Jupyter si es necesario. Asegúrese de que el entorno virtual esté activado al ejecutar comandos relacionados con el proyecto.

#### Ejecutar Jupyter Notebook

```bash
jupyter notebook
```

Esto abrirá una interfaz en su navegador donde podrá ver y ejecutar los notebooks del proyecto.

## Consideraciones Adicionales

**Actualización de Dependencias:** Si necesita agregar nuevas bibliotecas, puede hacerlo usando `pip install <package>` y luego actualizar `requirements.txt` usando:

```bash
pip freeze > requirements.txt
```

**Desactivar el Entorno Virtual:** Cuando haya terminado, puede desactivar el entorno virtual ejecutando:

```bash
  deactivate
```
- #### En Linux/MacOS

```bash
deactivate
```

- #### En Windows

```bash
.venv\Scripts\deactivate.bat
```

Siguiendo las instrucciones, debería poder configurar y ejecutar el proyecto de manera eficiente en su máquina local. Si tiene problemas, asegúrese de verificar que todas las dependencias estén instaladas correctamente y que el entorno virtual esté activado.
