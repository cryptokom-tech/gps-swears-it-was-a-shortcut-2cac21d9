# The GPS Swears It Was a Shortcut

[![The GPS Swears It Was a Shortcut](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/c/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![Rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/cryptokom-tech/gps-swears-it-was-a-shortcut-2cac21d9/rank.svg)](https://make.fun/c/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![Reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/cryptokom-tech/gps-swears-it-was-a-shortcut-2cac21d9/reward.svg)](https://make.fun/c/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

One excuse, in the GPS's own voice, for sending the driver down the
wrong road — written by a small Python program for [The GPS Swears It
Was a Shortcut](https://make.fun/c/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
on [make.fun](https://make.fun).

## The excuse

> I didn't take a wrong turn, I took a shortcut the road hasn't
> finished yet. The map drew the bridge; the river just drew the lake
> first.

The GPS stays smug and blames the map: the wrong turn was a shortcut
the road hadn't finished, the map drew the bridge, and the river —
not the GPS — drew the lake first.

## How it works

`main.py` writes the excuse to `/output/entry.txt` (1–200 characters,
UTF-8, one line). No network, no dependencies, no secrets — just the
excuse.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
