FUNCTION
============
The purpose of this script is to create a RSA encrypted reverse shell.
The point of using an RSA encrypted tunnel instead of other common protocols like SSH and HTTPS, is because there are a multitude of network monitoring equipment than can perfrom SSH and HTTPS termination.
Incase you'd wish to use other RSA keys, other than the ones provided in the scripts, you can use the keygen.py script to generate them, just run "python keygen.py".


PREREQUISITES
=============
You should have python 2.7 and the pycrypto 2.6 installed.

MODIFICATIONS
=============
Feel free to fork this script and modify it to your heart's content.

