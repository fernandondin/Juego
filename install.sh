#!/bin/bash
w=$(whoami)
dr=/home/$w/.spacegame
mkdir $dr
for i in $(ls);
do
    cp -r $i $dr
done
cd $dr
rm install.sh
touch Jueguillo.desktop
echo "[Desktop Entry]" >> Jueguillo.desktop
echo "Version=1.0" >> Jueguillo.desktop
echo "Type=Application" >> Jueguillo.desktop
echo "Terminal=false" >> Jueguillo.desktop
echo "Icon=$dr/Imagenes/Marciano.png" >> Jueguillo.desktop
touch juego.sh
echo "#!/bin/bash" >> juego.sh
echo "cd $dr" >> juego.sh
echo "python $dr/Juego.py" >> juego.sh
chmod +777 juego.sh
echo "Exec=sh $dr/juego.sh" >> Jueguillo.desktop
echo "Name=Jueguillo" >> Jueguillo.desktop
sudo cp Jueguillo.desktop /usr/share/applications
