# setup for raspberry pi 4 with grove-base-hat
<h2> install module grove-hat </h2>
curl -sL http://github.com/Seeed-Studio/grove.py/raw/master/install.sh |sudo bash -s -

<h2> install dht </h2>
pip3 install seeed-python-dht
<h2> install paho-mqtt</h2>
pip3 install paho-mqtt
<h2> update py3 </h2>
sudo apt-get update
<h2> check py --version </h2>
python3 --version

<h2>cai dat supervisor<h2>
        <p>
             sudo apt-get install supervisor   
        </p>


<h2> run node-red auto </h2>
<p>
        cai node red :
        bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
</p>
run this:
        enable:  sudo systemctl enable nodered.service
        disable: sudo systemctl disable nodered.service

<h2> lenh cho he thong </h2>

<p>Enable System Supervisor: sudo systemctl enable supervisor</p> 
<p>Update Supervisor: sudo supervisorctl update</p>
<p>Restart Supervisor: sudo service supervisor restart</p>
<p>Check: sudo supervisorctl </p>


sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.x 1
