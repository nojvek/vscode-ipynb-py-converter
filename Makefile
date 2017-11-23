.PHONY: build clean upload-test upload
build: clean
	python setup.py bdist_wheel --universal

clean:
	rm -rf build dist

upload-test:
	twine upload -r pypitest dist/*

upload:
	twine upload dist/*
