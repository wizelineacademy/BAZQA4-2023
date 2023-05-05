Feature: LogIn


  @e2e
    Scenario: LOGIN_TO_THE_APP
      Given we are in the "LOGIN" screen
      When we fill the "Usuario" label
      And we fill the "Contraseña" label
      And we tap the "LOGIN" button
      Then we are in the "Productos" screen



      #Behave
       #Given:describe el estado inicial de la aplicacion(Dado que)
       # describe la pantalla en la que estamos
       # When:Describe la accion que esta siendo probada(Cuando)
       # Then: Describe el resultado esperado al finalizar la prueba(Entonces)
