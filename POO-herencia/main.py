import clases

persona=clases.Persona()
persona.setNombre("Gianluca")
persona.setApellido("Pastore")
persona.setAltura("160cm")
persona.setEdad(20)
print(f"la persona es: {persona.getNombre()} {persona.getApellido()}")
print(persona.hablar())

programador=clases.Informatico()
programador.setNombre("Nicole")
programador.setApellido("ferreira")
print(f"la programadora es: {programador.getNombre()} {programador.getApellido()}")
print(programador.getLenguaje())
print("---------------")

tecnico=clases.TecnicoRedes()
tecnico.setNombre("miguel")
print(f"el tecnico es: {tecnico.getNombre()} \n Experiencia: {tecnico.getLenguaje()}")
print(tecnico.auditoria())