# Running Volatility Community plugins

Find community plugins in the repo [here][community].

[community]:https://github.com/volatilityfoundation/community

## 1. Clone the Community repo locally.  

`git clone https://github.com/volatilityfoundation/community.git`

## 2. Initialize a environment variable

`export PLUGINSPATH=/home/ubuntu/community`

## 3. Run `vol.py` with a community plugin and the `--plugins` argument

Because not all plugins are in the Community repo, you need to specify the path
down to the author of the plugin you wish to use.

In this example, I'm using the `saveconfig` plugin by Andrew Cook.

`vol.py --conf-file=volatilityrc/sample004 --plugins=$PLUGINSPATH/AndrewCook saveconfig`

You can also add a `plugins =` line in your volatilityrc configuration file.

For example:
```
[DEFAULT]
PROFILE=WinXPSP3x86
LOCATION=file:///cases/lab4/sample004.bin
KDGB=0x8054cde0
plugins=/home/ubuntu/community/AndrewCook
```
