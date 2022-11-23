# Watchy

<img src="./assets/watchy_prose.jpg" width="300" />

## Development

The following steps are applicable only to development on Linux.

1. [Installing Poetry dependencies](#install-poetry-dependencies)
2. [Install MicroPython firmware](#install-micropython-firmware)
3. Understand the [file structure](#file-structure)
4. Use either [WebREPL](#webrepl) or [RShell](#rshell)

### Install Poetry dependencies

This project uses the Poetry dependency manager. Install that and run the following to install the poetry dependencies:

```bash
poetry install
```

### Install MicroPython firmware

Enter the virtualenv created by Poetry:

```bash
poetry shell
```

Identify the serial port your Watchy is connected to:

```bash
python -m serial.tools.list_ports
```

Example output:

```bash
/dev/ttyUSB0
1 ports found
```

If the serial port is inaccessible, you may need to give yourself the necessary permissions:

```bash
sudo usermod -aG tty $USER
sudo usermod -aG dialout $USER

# re-enter your shell
exec su -l $USER
cd watchy_py
poetry shell
```

Download the [latest stable MicroPython firmware](https://micropython.org/download/esp32/).

Proceed to install the new firmware:

```bash
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ~/Downloads/esp32-20220618-v1.19.1.bin
```

### File structure


There are 2 main MicroPython scripts:

- **boot.py**: this is run immediately after the Watchy boots up and by convention contains only code initialising debuggers, REPLs, etc.
- **main.py**: this is run immediately after `boot.py` runs and should contain your application code. You can import other dependencies in this file.

### WebREPL

You can use MicroPython's [webrepl](https://github.com/micropython/webrepl) to develop wirelessly over WiFi.

Install [RShell](#rshell) and run the RShell development scripts to install the MicroPython firmware and transfer the files from this repository onto the board.

Rename `src/secrets.example.py` to `src/secrets.py` and fill in the secrets appropriately.

### RShell

You can use [rshell](https://github.com/dhylands/rshell) to run Python scripts on the Watchy.

```bash
python shell
rshell
```

And then within rshell's interactive prompt, connect to the Watchy:

```bash
connect serial /dev/ttyUSB0
```

You can then access the Watchy's filesystem:

```bash
ls /pyboard
cp src/main.py /pyboard/
```

Or even edit a file directly on the Watchy:

```bash
edit /pyboard/main.py
```

You can get a Python REPL prompt over the serial port:

```shell
repl
```

The controls are emacs-style, so use `[C-x]`, i.e. <kbd>Ctrl-A</kbd> <kbd>Ctrl-X</kbd>.


Useful development commands:

```bash
./scripts/flash_micropython.sh # to re-flash micropython firmware if the MCU freezes up
./scripts/flash_src.sh # to transfer and run new files in a single command
```

#### Restarting

Since the reset pin on Watchy isn't easily accessible, you may want to do the following using rshell:

```bash
cp reset.py /pyboard/
repl ~ import reset ~
```

### Assets

- **Fonts**: [peterhinch/micropython-font-to-py](https://github.com/peterhinch/micropython-font-to-py)
  - `./scripts/font-to-py.py -x input.ttf <font_size> out.py`
- **Images**: [image2cpp](https://javl.github.io/image2cpp/)
