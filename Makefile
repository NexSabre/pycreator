clean:
	rm -rf dist/* build/* pycrator.egg-info

clean-dev: clean
	rm -rf src/pycreator/main/app_custom
