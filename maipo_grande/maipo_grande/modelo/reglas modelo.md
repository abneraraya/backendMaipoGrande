## Reglas modelo

## Entidad Subasta Transporte Nacional
.-Solamente se puede crear una subasta de transporte asociada a un pedido nacional ya que no se puede subastar 2 veces el mismo pedido de igual manera tiene asociado un id de administrador ya que toda subasta de transporte nacional debe ser creada por un administrador

## Entidad Subasta Pedido Nacional
.-Solamente se puede crear una subasta asociada a un pedido nacional ya que no se puede subastar 2 veces el mismo pedido de igual manera tiene asociado un id de administrador ya que toda subasta de transporte nacional debe ser creada por un administrador

## Entidad Postulacion Nacional
.-Solamente se puede crear una postulacion nacional  una vez exista una subasta de pedido nacional ademas debe postular un productor con sus productos

## Entidad Subasta Pedido Internacional
.-Solamente se puede crear una subasta asociada a un pedido internacional ya que no se puede subastar 2 veces el mismo pedido de igual manera tiene asociado un id de administrador ya que toda subasta de transporte nacional debe ser creada por un administrador

## Entidad informe Venta global
Esta entidad tiene las restricciones de que debe ser unico y  debe pertenecer a un contrato de venta extranjero y a un concretacion venta

## informe venta personal
acepta varios informes a la vez 