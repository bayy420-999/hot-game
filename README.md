# HOT GAME AUTO CLAIMER

## Installation

### On Linux and Windows

- Clone this repository

```shell
git clone https://github.com/bayy420-999/hot-game.git
```

- Install python dependecies

```shell
pip install -r requirements.txt
```

### On Termux (Not recommended)

Since `py_near_primitives` inside `py_near` module require rust, and rust is quite hard to be installed on android then you need to install `Arch Linux` to emulate native Linux operating system first

- Install Arch Linux

```shell
pkg install wget
wget https://sdrausty.github.io/TermuxArch/setupTermuxArch.sh
bash setupTermuxArch.sh
```

- Start Arch Linux

```shell
./startarch
```

- Install required tools

Inside Arch Linux terminal, type following command to initialize and populate pacman PGP key

```shell
pacman-key --init
pacman-key --populate archlinux
```

then install python and git by typing following command in the terminal

```shell
pacman -Sy git
pacman -Sy python-pip
```

- Clone this repository

```shell
git clone https://github.com/bayy420-999/hot-game.git
```

- Install python dependecies

```shell
pip install -r requirements.txt
```

## Usage

- Open `.env` file using your favorite text editor
- Replace `ACCOUNT_ID` with your account id (eg: example.tg)
- Replace `PRIVATE_KEY` with your NEAR wallet private key (eg: ED25519:....) 
- For RPC you can use your own NEAR RPC or leave the default value
- Save your modified `.env` file
- Run the program by typing `python main.py` in terminal

