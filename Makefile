clean:
	@echo "Limpiando..."
	rm -rf test/test_calculadora.py.swp
t:
	@echo "Ejecutando pruebas..."
	python3 -m unittest -v test/test_calculadora.py
