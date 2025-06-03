installer=''

venv:
	@cd App && make venv

run:
	@cd App && make run

android:
	@cd App && make android

clean:
	@cd App && make clean

waydroid:
	waydroid app install $(installer)