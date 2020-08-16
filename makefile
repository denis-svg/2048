game: checker.py grabber.py main.py settings.py
	sudo apt install python3-pip
	sudo pip3 install pygame
	sudo pip3 uninstall pyinstaller
	sudo pip3 install https://github.com/pyinstaller/pyinstaller/archive/develop.zip 
	pyinstaller --onefile -w main.py
	rm -R build
	rm main.spec
	rm -R __pycache__
	mv ./dist/main .
	rm -R dist
	realpath main > exe.txt
	realpath logo.png > logo.txt
	echo -n "[Desktop Entry]\nVersion=1.0\nType=Application\nTerminal=false\nIcon=" > 2048.desktop
	cat logo.txt >> 2048.desktop
	echo -n "\nExec=" >> 2048.desktop
	cat exe.txt >> 2048.desktop
	echo -n "\nName=2048" >> 2048.desktop
	mv 2048.desktop ~/Desktop
	rm logo.txt
	rm exe.txt
.PHONY : clean
clean:
	rm main
	rm ~/Desktop/2048.desktop
