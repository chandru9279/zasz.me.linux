# zasz.me.linux
Migrate my website to linux. Deploy system to docker. 
Also .NET guy learns linux stack.

## Setup

### OS level setup

Needs python3 (python 3.4.3) and pip3 installed. For pip installing cairocffi (os x does not seem to need this)

Linux
```bash
sudo apt-get install libffi-dev python3.4-dev libcairo2-dev
```

OS X
```
brew install Caskroom/cask/xquartz
brew install cairo
```

Install all .ttf fonts in disorganizer into the OS

### App setup

```bash
pip3 install virtualenv
virtualenv zmv -p python3
source zmv/bin/activate
pip install -r requirements.pip
cd web && npm install
```

### Run with
```bash
./m runserver
python -m disorganizer
```





