# code54130-Proyecto-Final

El Proyecto consiste en una Web de una Pasteleria: Lupe Mesas Dulces

http://127.0.0.1:8000/

Dicha Web contiene una App denominada: Pedidos.

Home Pedidos: http://127.0.0.1:8000/pedidos/


En la barra de navegacion de la App de pedidos se puede ver en el extremo derecho el link para acceder al About Me : http://127.0.0.1:8000/pedidos/about/. 

LOGIN/LOGOUT:

    Para acceder a la App de Pedidos se debe ingresar com Usuario y Contraeña (Botón LogIn), ya que de otra manera no se habilitan los DropDown para navegar la web. 
    
    También existe la posibilidad de hacer LogOut una vez que se desee "salir" de la App.

    Los "botones" de LogIn / LogOut / Crear Usuario se encuentran en la barra de navegacion superior de la App Pedidos. 

    Si no hay Usuario Logueado en la Home de Pedidos se visualiza el botón LogIn, que lleva al formulario para realizar el LogIn (http://127.0.0.1:8000/pedidos/login/) y el boton de Crear Usuario , que lleva al formulario para la creación del mismo ( http://127.0.0.1:8000/pedidos/crear-usuario/), en el caso que la persona necesite generar uno.

    Si el Usuario esta Logueado aparece el boton de LogOut y al lado el nombre del usuario que se encuentra logueado. 

    Haciendo Click en el botón LogOut, nos lleva a la Home de la App Pedidos, donde en la barra de navegación se puede acceder al botón LogIn nuevamente.
    
    Asimismo se puede generar nuevos usuarios haciendo link en el botón "Crear Usuario"

    El super usuario generado es
        User: admin 
        Password: admin1234

        El mismo puede acceder a todas las urls diseñadas.

    Otros usuarios generados que tiene perfil de "Clientes": 

        User: Candela
        Password: MCC21071979

        User: Soledad
        Password: MSC13051975

        User: Francisco
        Password: FG16022011

        User: Felipe
        Password: FG07042015

        User: Cecilia
        Password: CIH28031980

  
    Haciendo click sobre el nombre del usuario logueado podemos editar la información del mismo (http://127.0.0.1:8000/pedidos/editar-perfil/)
   
AVATARS:

En la barra de navegacion se puede observar, al lado del nombre del usuario (si existe un usuario logueado), la imagen del Avatar seleccionado (si se ha agregado una).  La acción de agregar avatar se realiza con el botón Agregar Avatar: que lleva al formulario donde adjuntamos la imagen a ultizar (http://127.0.0.1:8000/pedidos/avatar/add/)


NAVEGACIÓN APP PEDIDOS: 

    La página principal de pedidos "Home" posee una barra de navegacion donde se pueden observa y navegar, a través de los DropDown, a traves de los 3 modelos que posee la App: 

    1. Los Pedidos: 
    I. Todos los Pedidos: http://127.0.0.1:8000/pedidos/list/

        Dentro de "Todos los Pedidos" se puede Editar, Eliminar y Ver (el detalle) de cada uno de los pedidos, así como también Crear Pedidos nuevos. 

    II. Crear Pedidos:http://127.0.0.1:8000/pedidos/crear-pedido-con-formulario/
    III. Buscar Pedidos: http://127.0.0.1:8000/pedidos/buscar-con-formulario/

    2. Los Productos: 
    I. Todos los Productos: http://127.0.0.1:8000/pedidos/producto/list/

            Dentro de "Todos los Productos" se puede Editar, Eliminar y Ver (el detalle) de cada uno de los productos, así como también Crear Productos nuevos. 

    II. Crear Productos:http://127.0.0.1:8000/pedidos/crear-producto-con-formulario/
    III. Buscar Productos:http://127.0.0.1:8000/pedidos/producto/buscar/

    En el caso de Producto se repiten las opciones 1 y 2 de navegacion tanto construidas "a mano" con funciones como las contruidas en VBC.

    Los Productos - VBC:
    I. Todos los Productos: http://127.0.0.1:8000/pedidos/producto/vbc/list

    Dentro de "Todos los Productos" se puede Editar, Eliminar y Ver (el detalle) de cada uno de los productos, así como también Crear Productos nuevos.

    II. Crear Productos: http://127.0.0.1:8000/pedidos/producto/vbc/create/
    

    3. Los Packagings: En este caso la contruccion fue unicamante a tracves de VBC:
    I. Todos los Packaging: http://127.0.0.1:8000/pedidos/packaging/vbc/packaging-list

    Dentro de "Todos los Packagings" se puede Editar, Eliminar y Ver (el detalle) de cada uno de los packaging, así como también Crear Packagings nuevos.

    II. Crear Packaging:http://127.0.0.1:8000/pedidos/packaging/vbc/create/





